from django.shortcuts import render
from django.views import generic
from .models import Article
from .models import Tag

class Home(generic.TemplateView):
    template_name = 'blog/home.html'

class ArticleListView(generic.ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'article_detail.html'

class TagListView(generic.ListView):
    model = Tag
    template_name = 'tag_list.html'



# Create your views here.
