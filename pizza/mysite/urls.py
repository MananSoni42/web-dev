from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('ajax/get_item_names/', views.get_item_names, name="get_item_names"),
]
