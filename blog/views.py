from django.shortcuts import render
from .models import Article
# Create your views here.

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)


def home(request):
    return render(request,"blog/home.html")

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()    # it will generally try to find template in blog/modelname_list.html if we not declare