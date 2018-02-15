from django.contrib.auth.models import User, UserManager
from django.db import models
from django.utils import timezone


# Create your models here.


class Ingredients(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Recipes(models.Model):
    ingredients = models.ManyToManyField('Ingredients', max_length=150, through='RecipesInside', through_fields=('recipe','ingredient'))
    title = models.CharField(max_length=150)
    value = models.CharField(max_length=150)
    complexity = models.IntegerField(choices=(
        (1,'Легко'),
        (2,'Средне'),
        (3,'Сложно'),
    ),default=2)
    speed = models.IntegerField(choices=(
        (1,'Очень медленно'),
        (2,'Медленно'),
        (3,'Быстро'),
        (4,'Очень быстро'),
    ),default=3)
    meal_time = models.IntegerField(choices=(
        (0,'Перекус'),
        (1,'Завтрак'),
        (2,'Обед'),
        (3,'Ужин'),
    ),default=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, max_length=50,
                             default=User.objects.get(username='admin').id)

    def __str__(self):
        return self.title

class RecipesInside(models.Model):
    recipe = models.ForeignKey(Recipes,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients,on_delete=models.CASCADE)
    amount = models.CharField(max_length=64)



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class CustomUser(models.Model):
    user = models.OneToOneField('auth.User', unique=True, on_delete=models.DO_NOTHING)
    user_info = models.CharField(max_length=500, default='')
    objects = UserManager()
