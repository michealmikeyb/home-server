from django.db import models

# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=64)
    total = models.IntegerField(default=0)

class Recipe(models.Model):
    name = models.CharField(max_length=128)

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=256)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Step(models.Model):
    step = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
