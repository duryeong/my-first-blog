'''
Created on 2017. 4. 24.

@author: mshan
'''

from django.core.exceptions import PermissionDenied
from .models import Post

def user_is_entry_author(function):
   def wrap(request, *args, **kwargs):
      post = Post.objects.get(pk=kwargs['pk'])
      if post.author == request.user:
         return function(request, *args, **kwargs)
      else:
         raise PermissionDenied
      
   wrap.__doc__ = function.__doc__
   wrap.__name__ = function.__name__
   
   return wrap