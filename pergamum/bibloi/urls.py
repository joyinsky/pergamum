from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ArticleList.as_view(), name='list'),
    # url(r'^new/$', views.ArticleCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ArticleDetail.as_view(), name='detail'),
    url(r'^search/$', views.ArticleSearch.as_view(), name='search'),
    # url(r'^(?P<pk>\d+)/update/$', views.ArticleUpdate.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', views.ArticleDelete.as_view(), name='delete'),
]
