from django.shortcuts import render
from .models import Drink, Category
from time_att.product.models import Drink

# Create your views here.
def home_view(requset):
    if requset.method == 'POST':
        col = requset.POST.get('col', None)
        ese = requset.POST.get('ese', None)
        bld = requset.POST.get('bld', None)

        me = Drink.objects.all()
        if col:
            col_me = me.objects.get(category)
        return render(requset,'index.html')