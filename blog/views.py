from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import CommentForm 
# Create your views here.

class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "latest_posts"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.all().order_by("-date")[:3]
        
        
class AllPostView(ListView):
    template_name = "all_posts.html"
    model = Post  
    ordering = ['-date']
    context_object_name = "all_posts"  
    
    
class DetailPost(View):
    model = Post
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved = post_id in stored_posts
        else: 
            is_saved = False 
        return is_saved
   
    def get(self, request, slug):
        post = Post.objects.get(slug = slug)
        
        context = {
            "post": post, 
            "post_tags": post.tags.all(), 
            "comment_form" : CommentForm(),
            "comments" : post.comments.all().order_by('-id'),
            "saved_for_later" : self.is_stored_post(request, post.id)}
        return render(request, "post_detail.html", context )
        
        
    def post(self,request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug = slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            if not comment.user_name:
                comment.user_name = "Anonymous"
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("detail_page", args = [slug]))
        
        context = {
            "post": post, 
            "post_tags": post.tags, 
            "comment_form" : CommentForm(),
            "comments" : post.comments.all().order_by('-id'),
            "saved_for_later" : self.is_stored_post(request, post.id)}
        return render(request, "post_detail.html", context )


class ReadLaterView(View):
    
   
    
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        
        context = {}
        
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in = stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "read_later.html", context)

     
        
    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        
        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST['post_id'])
        
        if post_id not in stored_posts: 
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
            
        request.session["stored_posts"] = stored_posts

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)