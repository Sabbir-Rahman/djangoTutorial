from django.urls import path

from .views import (
    home,
    ArticleListView,
)

urlpatterns = [

    path('', home, name='blog-home'),
    path('view/', ArticleListView.as_view(), name='blog-home'),

]