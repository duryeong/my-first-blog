#-*-coding: utf-8 -*-

'''
Created on 2017. 4. 18.

@author: mshan
'''

from django import forms

from .models import Post, Comment

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

   class Meta:
      model = Post
      fields = ('title', 'text',)
      
class CommentForm(forms.ModelForm):

   class Meta:
      model = Comment
      fields = ('author', 'text',)
      
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    class Meta:
        model = User
        fields = ("username", "email", )
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # 각 input 태그의 help_text, label 제거함.
        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        # 각 input 요소에 속성 추가함.
        self.fields['username'].widget.attrs['placeholder'] = "ID"
        self.fields['username'].widget.attrs['id'] = "username"
        self.fields['password1'].widget.attrs['placeholder'] = "비밀번호"
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['placeholder'] = "비밀번호 확인"
        self.fields['email'].widget.attrs['placeholder'] = "exampl@abc.com"