from django.shortcuts import render
from .models import Kromka, Leafs, LDSP, FurnitureAccessories

def materials(request):
    kromka = Kromka.objects.all()
    context = {
        'kromka' : kromka
    }
    return render(request, 'materials.html', context)

def photoprint(request):
    photoprint = Leafs.objects.filter(option='photoprint')
    context = {
        'products' : photoprint
    }
    return render(request, 'products.html', context)

def eco_leather(request):
    eco = Leafs.objects.filter(option='ekokozha')
    context = {
        'products' : eco
    }
    return render(request, 'products.html', context)

def sandblast(request):
    sandblast = Leafs.objects.filter(option='sandblast')
    context = {
        'products' : sandblast
    }
    return render(request, 'products.html', context)

def decorative_partitions(request):
    decorative_partition = Leafs.objects.filter(option='decorated')
    context = {
        'products' : decorative_partition
    }
    return render(request, 'products.html', context)

def lamination_dsp(request):
    dsp = Leafs.objects.filter(option='laminirovanie')
    context = {
        'products' : dsp
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