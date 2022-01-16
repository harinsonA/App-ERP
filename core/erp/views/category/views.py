from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

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

    # def get_queryset(self):
    #     return Product.objects.all()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'Listado de Categorías'
        #context['object_list'] = Product.objects.all()
        return context