from django.http import HttpResponse
from django.shortcuts import render,redirect
from mysite.models import *
import json
import os
import copy
import datetime

class DecimalEncoder(json.JSONEncoder):
    def _iterencode(self, o, markers=None):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self)._iterencode(o, markers)

name_to_model = {
    'pizza': Pizza,
    'regular': RegularPizza,
    'sicilian': SicilianPizza,
    'sub': Sub,
    'pasta': Pasta,
    'salad': Salad,
    'platter': Platter,
}

name_to_order = {
    'pizza': PizzaOrder,
    'regular': PizzaOrder,
    'sicilian': PizzaOrder,
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

def load_cart(request):
    cust_name = request.GET['name']
    forder = sorted(FinalOrder.objects.filter(cust_name=cust_name, finished=False), key=lambda x: x.get_time(), reverse=True)
    if forder:
        forder = forder[0]

        table = []
        for order in forder.orders.all():
            row = []
            s = order.order.name + ' ' + str(order.order.__class__.__name__)
            if order.order.__class__.__name__ in ['Pizza']:
                if order.toppings.all():
                    s += ' with '
                    for top in order.toppings.all():
                        s += top.name + ', '

            elif order.order.__class__.__name__ in ['Sub']:
                if order.extra.all():
                    s += ' with '
                    for top in order.extra.all():
                        s += top.name + ', '

            row.append(s)
            row.append(str(float(order.get_price())))
            table.append(row)

        data = {
            'num': forder.order_num,
            'total': str(float(forder.get_price())),
            'table': table
        }
    else:
        data = {
            'num': '',
            'total': 0,
            'table': []
        }

    return HttpResponse(json.dumps(data), content_type='application/json')

def close_cart(request):
    cust_name = request.GET['name']
    forder = sorted(FinalOrder.objects.filter(cust_name=cust_name, finished=False), key=lambda x: x.get_time(), reverse=True)
    if forder:
        forder = forder[0]
    forder.finished = True
    forder.save()
    return redirect('/')

def get_toppings(request):
    data = {
        'pizza': [t.name for t in PizzaTopping.objects.all()],
        'sub': [t.name for t in SubExtra.objects.all()]
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def add_to_cart(request):
    cust_name = request.GET['cust_name']
    item_name = request.GET['name']
    item_type = request.GET['item_type']
    size_small = eval(request.GET['size'])
    if item_type in ['pizza']:
        type = request.GET['type']
    if item_type in ['pizza','sub']:
        extras = request.GET.getlist('extra')

    if item_type == 'pizza':
        item = name_to_model[type].objects.get(name=item_name)
        order = name_to_order[type](order=item, size_small=size_small, time=datetime.datetime.now())
    elif item_type not in ['salad', 'pasta']:
        item = name_to_model[item_type].objects.get(name=item_name)
        order = name_to_order[item_type](order=item, size_small=size_small, time=datetime.datetime.now())
    else:
        item = name_to_model[item_type].objects.get(name=item_name)
        order = name_to_order[item_type](order=item, time=datetime.datetime.now())
    order.save()
    if item_type in ['pizza']:
        for extra in extras:
            order.toppings.add(PizzaTopping.objects.get(name=extra))
    elif item_type in ['sub']:
        for extra in extras:
            order.extra.add(SubExtra.objects.get(name=extra))
    order.save()

    forder = sorted(FinalOrder.objects.filter(cust_name=cust_name, finished=False), key=lambda x: x.get_time(), reverse=True)
    if not forder:
        forder = FinalOrder(cust_name=cust_name)
        forder.save()
    else:
        forder = forder[0]

    forder.orders.add(order)
    return redirect('/')
