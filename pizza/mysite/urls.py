from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('ajax/get_item_names/', views.get_item_names, name="get_item_names"),
    path('ajax/get_toppings/', views.get_toppings, name="get_toppings"),
    path('ajax/add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('cart',views.cart),
]
