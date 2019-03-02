from django.shortcuts import render
from .models import Kromka, Leafs, LDSP, FurnitureAccessories

def materials(request):
    kromka = Kromka.objects.all()
    context = {
        'kromka' : kromka
    }
    return render(request, 'materials.html', context)


def leafs(request):
    leafs = Leafs.objects.all()
    context = {
        'products' : leafs
    }
    return render(request, 'products.html', context)


def kronospan(request):
    kronospans = LDSP.objects.filter(option='Kronospan')
    context = {
        'products' : kronospans
    }
    return render(request, 'products.html', context)


def swisspan(request):
    swisspans = LDSP.objects.filter(option='Swisspan')
    context = {
        'products' : swisspans
    }
    return render(request, 'products.html', context)


def swisspan_natur(request):
    swisspans_natur = LDSP.objects.filter(option='Swisspan_natur')
    context = {
        'products' : swisspans_natur
    }
    return render(request, 'products.html', context)


def blum(request):
    blums = FurnitureAccessories.objects.filter(option='Blum')
    context = {
        'products' : blums
    }
    return render(request, 'products.html', context)


def hettich(request):
    hettichs = FurnitureAccessories.objects.filter(option='Hettich')
    context = {
        'products' : hettichs
    }
    return render(request, 'products.html', context)