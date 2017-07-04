"""romanloaddotcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView
from django.views.static import serve
from django.conf import settings

from . import views

urlpatterns = [
    # homepage
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^humans.txt$', TemplateView.as_view(template_name='humans.txt', 
        content_type='text/plain')),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', 
        content_type='text/plain')),
    url(r'^shell/$', TemplateView.as_view(template_name="romanload/shell.html"), 
        name='shell'),
    
    # python section landing pages
    url(r'^about/$', TemplateView.as_view(template_name="romanload/about.html"), 
        name='about'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^spring/$', TemplateView.as_view(template_name='taobao.html'), name='spring'),
    url(r'^spring/(\w+)/$', views.spring, name='spring2'),
    
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/media/favicon.ico')),
]

if settings.DEBUG:
    urlpatterns += [
    url(r'^m/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
