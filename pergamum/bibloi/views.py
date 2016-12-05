from django.urls import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ArticleForm
from .models import Article


class ArticleList(ListView):
    model = Article
    paginate_by = 20


class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('bibloi:list')


class ArticleDetail(DetailView):
    model = Article


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('bibloi:list')


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('bibloi:list')
