from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import *
import json
import os
import copy
import datetime

name_to_model = {
    'pizza': Pizza,
    'reg_pizza': RegularPizza,
    'sic_pizza': SicilianPizza,
    'sub': Sub,
    'pasta': Pasta,
    'salad': Salad,
    'platter': Platter,
}

name_to_order = {
    'pizza': PizzaOrder,
    'reg_pizza': PizzaOrder,
    'sic_pizza': PizzaOrder,
    'sub': SubOrder,
    'pasta': PastaOrder,
    'salad': SaladOrder,
    'platter': PlatterOrder,
}

# Create your views here.
def homepage(request):
    return render(request, "mysite/home.html")

def get_item_names(request):
    name = request.GET['name']
    data = []
    name_to_model1 = copy.deepcopy(name_to_model)
    name_to_model1['pizza'] = RegularPizza
    for obj in name_to_model1[name].objects.all():
        data.append({
            'type': name,
            'name': obj.name,
            'im_path': f'./static/mysite/img/{name}.png',
            }
        )
    return HttpResponse(json.dumps(data), content_type='application/json')

def cart(request):
    return render(request, "mysite/cart.html")

def get_toppings(request):
    data = {
        'pizza': [t.name for t in PizzaTopping.objects.all()],
        'sub': [t.name for t in SubExtra.objects.all()]
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def add_to_cart(request):
    name = request.GET['name']
    name_item = request.GET['item_name']
    attrs = request.GET['attr']
    toppings = request.GET['extra']

    item = name_to_model[name_item].objects.get(name=name)
    order = name_to_order[name_item](**attrs, time=datetime.datetime.now())
    order.save()
    if name_item in ['pizza', 'reg_pizza', 'sic_pizza']:
        for t in toppings:
            order.toppings.add(PizzaToppings.objects.get(name=t))
