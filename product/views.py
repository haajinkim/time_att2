
from django.shortcuts import render
from .models import Category, Drink
# Create your views here.
def home_view(requset):
    if requset.method == 'POST':

        category = requset.POST.get('category', None)
        all = Category.objects.get(id=category)
        all_drink = Drink.objects.filter(category=all).values()
        
        return render(requset,'index.html',{'all_drink':all_drink})

    elif requset.method == 'GET':
        return render(requset,'index.html')
