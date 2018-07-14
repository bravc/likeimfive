from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('all', views.all, name='all'),
    path('search', views.search, name="post"),
    path('search/<int:id', views.search, name="post"),
    path('<int:post_id>', views.post, name="post"),
    path('comment', views.newComment, name="comment")

]
