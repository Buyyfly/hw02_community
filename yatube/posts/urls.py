from . import views
from django.urls import path

app_name = 'index'

urlpatterns = [
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('', views.index, name='post_list'),
]
