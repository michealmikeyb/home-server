import json

from django.http import JsonResponse

from home.models import Poll
from home.models import Recipe
from home.models import Ingredient
from home.models import Step

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