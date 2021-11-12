from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from erp.forms import CategoryForm
from erp.models import *

# Create your views here.

def category_list(request):
    data = {
        'title':'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request,'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            print("Se ha mandado GET")
        elif request.method == "POST":
            print("Se ha enviado POST")
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk= request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)        
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Categoría'
        return context