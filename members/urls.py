from django.urls import path
from .views import product_list_view
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('products/', views.product_list_view, name='product_list'),
    path('members/details/<int:id>', views.details, name='details'),

]