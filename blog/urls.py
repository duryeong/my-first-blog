'''
Created on 2017. 4. 17.

@author: mshan
'''

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]