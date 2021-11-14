from core.erp.models import Category, Product
from django.shortcuts import render

# Create your views here.

def myfirstview(request):
    data = {
        'name': 'Harinson',
        'categories': Category.objects.all()
    }
    return render(request, 'home.html', data)


def mysecondview(request):
    data = {
        'name': 'Harinson',
        'categories': Category.objects.all(),
        'productos': Product.objects.all()
    }
    return render(request, 'second.html', data)