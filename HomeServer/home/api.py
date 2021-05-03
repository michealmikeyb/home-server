import json

from django.http import JsonResponse

from home.models import Poll

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
