from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.shortcuts import HttpResponseRedirect, render
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import RequestContext


admin.autodiscover()


def login_user(request):
    username = password = ''

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                url = "/"
                if request.GET.get('next'):
                    url = request.GET.get('next')
                return HttpResponseRedirect(url)
            else:
                messages.error(request, "Tu cuenta no está activa. Contacta al administrador")
        else:
            messages.error(request, "Tu usuario o contraseña son incorrectos.")
    return render(request, template_name='login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


urlpatterns = [
    url(r'^attachments/', include('attachments.urls', namespace='attachments')),
    url(r'^bibloi/', include('pergamum.bibloi.urls', namespace='bibloi')),
    url(r'^search/', include('haystack.urls', namespace='search')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(TemplateView.as_view(template_name='home.html'))),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout_view, name='logout')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
