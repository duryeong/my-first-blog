'''
Created on 2017. 4. 17.

@author: mshan
'''

from django.shortcuts import render


def post_list(request):
   return render(request, 'blog/post_list.html', {})