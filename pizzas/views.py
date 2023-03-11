from django.shortcuts import render
from .models import Pizza

# Create your views here.


def index(request):
    """Головна сторінка додатку Learning Log"""
    return render(request, 'pizzas/index.html')


def pizza_types(request):
    """Виводить список тем"""
    pizza_types = Pizza.objects.order_by('date_added')
    context = {'pizza_types': pizza_types}
    return render(request, 'pizzas/pizza_types.html', context)


def pizza_type(request, pizza_type_id):
    """Виводить одну тему і всі ії записи"""
    pizza_type = Pizza.objects.get(id=pizza_type_id)
    toppings = pizza_type.topping_set.order_by('-date_added')
    context = {'pizza_type': pizza_type, 'toppings': toppings}
    return render(request, 'pizzas/pizza_type.html', context)
