from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost
from .models import Product

def members(request):
  mymembers = BlogPost.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = BlogPost.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


# def all_products(request):
#   products = Product.objects.all()
#   template = loader.get_template('products.html')
#   data = {
#     'products': products,
#   }
#   return HttpResponse(template.render(data, request))

def product_list_view(request):
  products = Product.objects.all()
  template = loader.get_template('product_list.html')
  data = {
    'products': products,
  }
  return HttpResponse(template.render(data, request))



