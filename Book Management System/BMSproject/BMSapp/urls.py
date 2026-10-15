from django.urls import path
from . import views

urlpatterns = [
    path('', views.Book_list, name='book_list'),
    path('create/', views.Book_create, name='book_create'),
    path('update/<int:id>/', views.Book_update, name='book_update'),
    path('delete/<int:id>/', views.Book_delete, name='book_delete'),
]   