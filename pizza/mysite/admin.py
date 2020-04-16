from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Order)
admin.site.register(FinalOrder)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Platter)
admin.site.register(SubExtra)
admin.site.register(Sub)
admin.site.register(PizzaTopping)
admin.site.register(Pizza)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)

admin.site.register(PastaOrder)
admin.site.register(SaladOrder)
admin.site.register(PlatterOrder)
admin.site.register(SubOrder)
admin.site.register(PizzaOrder)
