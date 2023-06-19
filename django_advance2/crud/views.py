from django.shortcuts import render
from .forms import GoodsCreateForm, GoodsUpdataForm, ImageSizeLimitationForm
from .models import Goods

class GoodCreate(generic.CreateView):
    model = Goods
    form_class = GoodsCreateForm
    template_name = 'crud/goods_create.html'
    success_url = '/crud/goods_create'

class GoodList(generic.ListView):
    model = Goods
    template_name = 'crud/goods_list.html'

class GoodsDelete(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'