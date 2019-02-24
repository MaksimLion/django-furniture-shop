from django.shortcuts import render
from .models import Furniture



def main(request):
    return render(request, 'base.html')


def categories(request):
    return render(request, 'categories.html')


def kitchens(request):
    kitchens = Furniture.objects.filter(option='kitchens')
    context = {
        'kitchens' : kitchens
    }
    return render(request, 'products.html', context)


def showcases(request):
    showcases = Furniture.objects.filter(option='showcases')
    context = {
        'showcases' : showcases
    }
    return render(request, 'products.html', context)


def wardrobes(request):
    wardrobes = Furniture.objects.filter(option='wardrobes')
    context = {
        'wardrobes' : wardrobes
    }
    return render(request, 'products.html', context)


def offices(request):
    offices = Furniture.objects.filter(option='offices')
    context = {
        'offices' : offices
    }
    return render(request, 'products.html', context)


def hallways(request):
    hallways = Furniture.objects.filter(option='hallways')
    context = {
        'hallways' : hallways
    }
    return render(request, 'products.html', context)


def lounges(request):
    lounges = Furniture.objects.filter(option=lounges)
    context = {
        'lounges' : lounges
    }
    return render(request, 'products.html', context)


def child(request):
    child = Furniture.objects.filter(option=child)
    context = {
        'child' : child
    }
    return render(request, 'products.html', context)


def closets(request):
    closets = Furniture.objects.filter(option=closets)
    context = {
        'closets' : closets
    }
    return render(request, 'products.html', context)


def others(request):
    others = Furniture.objects.filter(option=others)
    context = {
        'others' : others
    }
    return render(request, 'products.html', context)
    
