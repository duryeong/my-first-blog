'''
Created on 2017. 4. 18.

@author: mshan
'''

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)