from django.db import models

# Create your models here.


class Pizza(models.Model):
    """Тема, що вивчає користувач"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Повертає символьне представлення моделі"""
        return self.text


class Topping(models.Model):
    """Інформація, що вивчив користувач за темою"""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Повертає символьне представлення моделі"""
        return f'{self.text[:50]}...'
