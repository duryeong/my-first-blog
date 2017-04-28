"""startdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views
from django.views.generic import TemplateView
from blog.views import DuplicationCheck
from blog import views as bv

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^accounts/login/$', views.login, name='login'),
   url(r'^signup/$',bv.signup, name='signup'),
   url(r'^signup_ok/$',TemplateView.as_view(template_name='registration/signup_ok.html'), name='signup_ok'),
   url(r'^duplcheck$', DuplicationCheck.as_view(), name='duplcheck'),
   url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
   url(r'', include('blog.urls')),
]
