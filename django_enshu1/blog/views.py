from django.shortcuts import render
from django.views import generic
from .models import Article
from .models import Tag
from django.shortcuts import redirect

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self,request,GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self,request,GET)
        form.is_valid()
        keywoird = form.cleaned_data.get('keyword')
        if keyword:
            queryset = queryset.filter(title=keyword)
        return queryset

class CommentCreateView(generic.CreateView):
    model = Comment
    template_nsme = 'blog/comment_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = CommentCreateForm

    def form_valid(self,form):
        #form.save(commit=False)データベースにはまだ保存しない
        #commit=Falseビューで、モデルのフィールドを埋めるために使う引数
        comment = form.save(commit=False)

        #Commentモデルの、targetフィールドをここで埋める
        #モデル名.object.get(フィールド=値)1津田家、DB空取り出すのに使うのがget
        #url内の<int:pk>は、self.kwargs['pk']で取得できる
        comment.target = Article.object.get(pk=self.kwargs['pk'])

        comment.save()  #saveしないと保存されない
        return redirect('blog:home')










# Create your views here.
