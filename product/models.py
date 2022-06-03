from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=15, null=False)
    category = models.ForeignKey('category', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=20)

