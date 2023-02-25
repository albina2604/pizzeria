from django.db import models

# Create your models here.


class Pizza(models.Model):
    """Тема, що вивчає користувач"""

    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def str(self):
        """Повертає символьне представлення моделі"""
        return self.name


class Topping(models.Model):
    """Інформація, що вивчив користувач за темою"""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def str(self):
        """Повертає символьне представлення моделі"""
        return f'{self.name[:50]}...'
