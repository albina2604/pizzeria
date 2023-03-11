from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Домашня сторінка
    path('', views.index, name='index'),
    # Сторінка з переліком усіх тем
    path('pizza_types/', views.pizza_types, name='pizza_types'),
    # Сторінка з складниками до піци
    path('pizza_type/<int:pizza_type_id>/',
         views.pizza_type, name='pizza_type'),

]
