from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')

def gnocchi(request):
    return render(request, 'home/gnocchi.html')

def banSeagulls(request):
    return render(request, 'home/banSeagulls.html')