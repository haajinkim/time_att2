from django.db import models

# Create your models here.

class Drink(models.Model):
    name = models.CharField(max_length=15, null=False)
    drink_category = models.CharField(max_length=15, null=False)


class Category(models.Model):
    category = models.ForeignKey(Drink, on_delete=models.CASCADE)

