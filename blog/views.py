#-*-coding: utf-8 -*-

'''
Created on 2017. 4. 17.

@author: mshan
'''

#회원가입
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.base import View

from .decorators import user_is_entry_author
from .forms import PostForm, CommentForm
from .forms import RegisterForm
from .models import Post, Comment


# ajax
def post_list(request):
   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
   post = get_object_or_404(Post, pk=pk)
   return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
   if request.method == "POST":
      form = PostForm(request.POST)
      if form.is_valid():
         post = form.save(commit=False)
         post.author = request.user
         #        post.published_date = timezone.now()
         post.save()
      return redirect('post_detail', pk=post.pk)
   else:
      form = PostForm()
   return render(request, 'blog/post_edit.html', {'form': form})

@login_required
@user_is_entry_author
def post_edit(request, pk):
   post = get_object_or_404(Post, pk=pk)
   if request.method == "POST":
      form = PostForm(request.POST, instance=post)
      if form.is_valid():
         post = form.save(commit=False)
         post.author = request.user
#          post.published_date = timezone.now()
         post.save()
         return redirect('post_detail', pk=post.pk)
   else:
      form = PostForm(instance=post)
   return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
   posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
   return render(request, 'blog/post_draft_list.html', {'posts': posts})
 
@login_required
def post_publish(request, pk):
   post = get_object_or_404(Post, pk=pk)
   post.publish()
   return redirect('post_detail', pk=pk)

@login_required
@user_is_entry_author
def post_remove(request, pk):
   post = get_object_or_404(Post, pk=pk)
   post.delete()
   return redirect('post_list')
 
@login_required
def add_comment_to_post(request, pk):
   post = get_object_or_404(Post, pk=pk)
   if request.method == "POST":
      form = CommentForm(request.POST)
      if form.is_valid():
         comment = form.save(commit=False)
         comment.post = post
         comment.save()
         return redirect('post_detail', pk=post.pk)
   else:
      form = CommentForm()

   return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   comment.approve()
   return redirect('post_detail', pk=comment.post.pk)

@login_required
@user_is_entry_author
def comment_remove(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   post_pk = comment.post.pk
   comment.delete()
   return redirect('post_detail', pk=post_pk)

def signup(request):
    """signsup
    to register users
    """
    if request.method == "POST":
        userform = RegisterForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(
                reverse("signup_ok")
            )
    elif request.method =="GET":
        userform = RegisterForm()
    return render(request, "registration/signup.html", {"userform": userform,})

class DuplicationCheck(View):
    def post(self, request):
        # user = get_object_or_404(User, username=username)
        username = request.POST.get('username', None)
        data = {
            'is_taken': User.objects.filter(username__iexact=username).exists()
            }
        return JsonResponse(data)
