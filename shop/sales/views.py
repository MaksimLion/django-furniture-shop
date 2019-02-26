from django.shortcuts import render
from .models import Sale


def sales(request):
    sales = Sale.objects.all()
    context = {
        'sales' : sales
    }
    return render(request, 'sales.html', context)

