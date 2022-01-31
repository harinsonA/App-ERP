from pyexpat import model
from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.erp.forms import CategoryForm

from core.erp.models import Category, Product

def category_list(request):
    data = {
        'title': 'Listar categorias',
        'category': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as error:
            data['error'] = str(error)
        return JsonResponse(data)
    

    # def get_queryset(self):
    #     return Product.objects.all()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'Listado de Categorías'
        #context['object_list'] = Product.objects.all()
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'Crear Categorías'
        #context['object_list'] = Product.objects.all()
        return context
    
    def post(self, request: HttpResponse, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)