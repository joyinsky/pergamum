from django.urls import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ArticleForm, ArticleSearchForm
from .models import Article
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet


class ArticleList(ListView):
    model = Article
    paginate_by = 20


#class ArticleCreate(CreateView):
#    model = Article
#    form_class = ArticleForm
#    success_url = reverse_lazy('bibloi:list')


class ArticleDetail(DetailView):
    model = Article

#class ArticleUpdate(UpdateView):
#    model = Article
#    form_class = ArticleForm
#    success_url = reverse_lazy('bibloi:list')


#class ArticleDelete(DeleteView):
#    model = Article
#    success_url = reverse_lazy('bibloi:list')

class ArticleSearch(SearchView):
    template_name = 'search/search.html'
    form_class = ArticleSearchForm
    queryset = SearchQuerySet().order_by('-date')


