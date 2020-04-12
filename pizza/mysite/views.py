from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import *
import json
import os

# Create your views here.
def homepage(request):
    return render(request, "mysite/home.html")

def get_item_names(request):
    name = request.GET['name']
    name_to_model = {
        'pizza': RegularPizza,
        'sub': Sub,
        'pasta': Pasta,
        'salad': Salad,
        'platter': Platter,
    }
    data = []
    for obj in name_to_model[name].objects.all():
        data.append({
            'name': obj.name,
            'im_path': f'./static/mysite/img/{name}.png',
            }
        )
    return HttpResponse(json.dumps(data), content_type='application/json')
