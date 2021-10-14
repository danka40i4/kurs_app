from django.contrib import admin
from django.urls import path
from .views import home, post_list, post_detail, post_new, post_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('post_list', post_list, name='post_list'),
    path('post/<int:pk>/',post_detail, name='post_detail'),
    path('post/new',post_new, name='post_new'),
    path('post/<int:pk>/edit',post_edit, name='post_edit')
]
