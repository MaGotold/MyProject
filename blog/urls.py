from django.urls import path
from . import views
from blog.views import IndexView, AllPostView, DetailPost, ReadLaterView


urlpatterns = [
    path("", IndexView.as_view(), name='main_page'),
    path("posts", AllPostView.as_view(), name='posts_page'),
    path("posts/<slug:slug>", DetailPost.as_view(), name='detail_page'),
    path("read-later", ReadLaterView.as_view(), name = "read-later")
] 
