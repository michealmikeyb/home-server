from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')

def gnocchi(request):
    return render(request, 'home/gnocchi.html')

def banSeagulls(request):
    return render(request, 'home/banSeagulls.html')

def leashem(request):
    return render(request, 'home/leashem.html')

def justi(request):
    return render(request, 'home/justi.html')

def homeControl(request):
    return render(request, 'home/homeControl.html')

def truth(request):
    return render(request, 'home/fediversePredictions.html')