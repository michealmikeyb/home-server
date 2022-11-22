import json

from django.http import JsonResponse
import asyncio
from kasa import SmartPlug

from home.models import Poll
from home.models import Recipe
from home.models import Ingredient
from home.models import Step
from home.utils import get_switch
from home.utils import get_all_switches
from home.utils import SWITCHES



def poll(request):
    if request.method == 'GET':
        poll_name = request.GET.get('name', None)
        if poll_name is not None:
            try:
                poll = Poll.objects.get(name=poll_name)
                return JsonResponse({'total': poll.total})
            except Poll.DoesNotExist as e:
                return JsonResponse({'error': 'poll not found'})
        else:
            return JsonResponse({'error': 'no name given'})

    if request.method == 'POST':
        post_data = json.loads(request.body.decode("utf-8"))
        poll_name = post_data.get('name', None)
        if poll_name is not None:
            try:
                poll = Poll.objects.get(name=poll_name)
                total = poll.total +1
                poll.total = total
                poll.save()
            except Poll.DoesNotExist as e:
                poll = Poll.objects.create(name=poll_name)
                poll.total = 1
                poll.save()
            return JsonResponse({'id': poll.id})
        else:
            return JsonResponse({'error': 'no name given'})

def recipe(request):
    if request.method == 'GET':
        name = request.GET.get('name', None)
        if name is not None:
            recipes = Recipe.objects.filter(name__icontains=name)
            recipe_dict = []
            for recipe in recipes:
                recipe_dict.append({
                    'name': recipe.name,
                    'ingredients': [i.ingredient for i in recipe.ingredient_set.all()],
                    'steps': [s.step for s in recipe.step_set.all()]
                })
            return JsonResponse({'recipes': recipe_dict})
        else:
            return JsonResponse({'error': 'no name given'})

    if request.method == 'POST':
        post_data = json.loads(request.body.decode("utf-8"))
        name = post_data.get('name', None)
        if name is not None:
            recipe = Recipe.objects.create(name=name)

            ingredients = post_data.get('ingredients', [])
            for i in ingredients:
                Ingredient.objects.create(recipe=recipe, ingredient=i)

            steps = post_data.get('steps', [])
            for s in steps:
                Step.objects.create(recipe=recipe, step=s)
            
        else:
            return JsonResponse({'error': 'no name given'})

def switch(request):
    if request.method == 'POST':
        post_data = json.loads(request.body.decode("utf-8"))
        plug_name = post_data.get('name', None)
        try:
            switch = get_switch(plug_name)
        except ValueError:
            return JsonResponse({'error': 'invalid name'})
        
        command = post_data.get('command', None)
        if command == 'on':
            if switch.is_on:
                return JsonResponse({'error': 'already on'})
            asyncio.run(switch.turn_on())
            return JsonResponse({'success': f"{plug_name} turned on"})

        elif command == 'off':
            if not switch.is_on:
                return JsonResponse({'error': 'already off'})
            asyncio.run(switch.turn_off())
            return JsonResponse({'success': f"{plug_name} turned off"})
        else:
            print(command)

    if request.method == 'GET':
        switches = get_all_switches()
        if not switches:
            switches = []
            for s in SWITCHES:
                switch = SmartPlug(s['ip'])
                asyncio.run(switch.update())
                switches.append(switch)
        switches = [{'name': switch.alias, 'is_on': switch.is_on} for switch in switches]
        return JsonResponse({'switches': switches})



