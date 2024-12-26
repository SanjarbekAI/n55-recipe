from django.urls import path

from blogs.views import blog_list_view

app_name = 'blogs'

urlpatterns = [
    path('', blog_list_view, name='list'),
]
