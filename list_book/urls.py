from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.book_add, name='book_append'),
    path('add/<int:id>/', views.book_add, name='book_update'),
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
    path('', views.book_list, name='book_list')
]
