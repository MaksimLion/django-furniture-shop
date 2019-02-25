from django.shortcuts import render
from .models import Furniture


def categories(request):
    return render(request, 'categories.html')


def kitchens(request):
    kitchens = Furniture.objects.filter(option='kitchens')
    for img in kitchens:
        print(img.photo)
    context = {
        'products' : kitchens
    }
    return render(request, 'products.html', context)


def showcases(request):
    showcases = Furniture.objects.filter(option='showcases')
    context = {
        'products' : showcases
    }
    return render(request, 'products.html', context)


def wardrobes(request):
    wardrobes = Furniture.objects.filter(option='wardrobes')
    context = {
        'products' : wardrobes
    }
    return render(request, 'products.html', context)


def offices(request):
    offices = Furniture.objects.filter(option='offices')
    context = {
        'products' : offices
    }
    return render(request, 'products.html', context)


def hallways(request):
    hallways = Furniture.objects.filter(option='hallways')
    context = {
        'products' : hallways
    }
    return render(request, 'products.html', context)


def lounges(request):
    lounges = Furniture.objects.filter(option='lounges')
    context = {
        'products' : lounges
    }
    return render(request, 'products.html', context)


def child(request):
    child = Furniture.objects.filter(option='child')
    return render(request, 'products.html', {
        'products': child
    })


def closets(request):
    closets = Furniture.objects.filter(option='closets')
    context = {
        'products' : closets
    }
    return render(request, 'products.html', context)


def others(request):
    others = Furniture.objects.filter(option='others')
    context = {
        'products' : others
    }
    return render(request, 'products.html', context)
