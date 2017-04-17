'''
Created on 2017. 4. 17.

@author: mshan
'''

from django.contrib import admin

from .models import Post

admin.site.register(Post)