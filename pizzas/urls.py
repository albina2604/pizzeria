from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Домашня сторінка
    path('', views.index, name='index'),
    # Сторінка з переліком усіх тем
    path('pizza_types/', views.pizza_types, name='pizza_types'),
]
