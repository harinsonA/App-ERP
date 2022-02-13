from multiprocessing import context
from pyexpat import model
from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse, HttpRequest
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
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorías'
        #context['object_list'] = Product.objects.all()
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Categorías'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'add'
        #context['object_list'] = Product.objects.all()
        return context
    
    def post(self, request: HttpResponse, *args: str, **kwargs: Any) -> HttpResponse:
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado por ninguna opción'
        except Exception as error:
            data['error'] = str(error)
        return JsonResponse(data)
        # form = CategoryForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return HttpResponseRedirect(self.success_url)
        # self.object = None
        # context = self.get_context_data(**kwargs)
        # context['form'] = form
        # return render(request, self.template_name, context)

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def dispatch(self, request, *args: Any, **kwargs: Any):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado por ninguna opción'
        except Exception as error:
            data['error'] = str(error)
        return JsonResponse(data)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Categorías'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'edit'
        #context['object_list'] = Product.objects.all()
        return context

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('erp:category_list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Categorías'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('erp:category_list')
        return context