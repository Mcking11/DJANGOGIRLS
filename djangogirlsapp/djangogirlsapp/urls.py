from django.contrib import admin
from django.urls import path

from blog.views import frontpage, post_detail, PostCreateView

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]
