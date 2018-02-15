# Generated by Django 2.0.2 on 2018-02-14 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladybugs', '0007_recipes_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='complexity',
            field=models.IntegerField(choices=[(1, 'Легко'), (2, 'Средне'), (3, 'Сложно')], default=2),
        ),
        migrations.AddField(
            model_name='recipes',
            name='meal_time',
            field=models.IntegerField(choices=[(0, 'Перекус'), (1, 'Завтрак'), (2, 'Обед'), (3, 'Ужин')], default=0),
        ),
        migrations.AddField(
            model_name='recipes',
            name='speed',
            field=models.IntegerField(choices=[(1, 'Очень медленно'), (2, 'Медленно'), (3, 'Быстро'), (4, 'Очень быстро')], default=3),
        ),
    ]
