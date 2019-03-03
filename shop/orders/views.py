from django.shortcuts import render
from .forms import OrderForm


def orders(request):

    if request.method == 'GET':
        form = OrderForm()
        context = dict(
            forms=form
        )
        return render(request, 'contact.html', context)

    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            new_form = OrderForm()
            context = dict(message='Ваша заявка принята', forms=new_form)
            return render(request, 'contact.html', context)
