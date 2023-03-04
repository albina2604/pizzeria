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
