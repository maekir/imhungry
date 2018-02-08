from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Ingredients(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Recipes(models.Model):
    ingredients = models.ManyToManyField('Ingredients', max_length=150, )
    title = models.CharField(max_length=150)
    value = models.CharField(max_length=150)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, max_length=50,
                             default=User.objects.get(username='admin').id)

    def __str__(self):
        return self.title
