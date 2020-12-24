from django.contrib import admin
from django.urls import path
from posts.views import IndexView
from . import views
from .views import IndexView, PostDetail

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('detail/<slug:slug>', views.PostDetail.as_view(), name="single"),
    path('category/<slug:slug>', views.CategoryDetail.as_view(), name="category-detail"),
    path('search/', views.SearchView.as_view(), name="search"),
    path('detail/<slug:slug>/update', views.UpdatePostView.as_view(), name="update"),
    path('detail/<slug:slug>/delete', views.PostdeleteView.as_view(), name="delete"),
]