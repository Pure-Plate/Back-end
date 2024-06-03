from django.urls import path
from . import views

urlpatterns = [
    path('add/<str:restaurant_name>/', views.add_favorites, name='add_favorites'),
    path('user/', views.get_favorites, name='get_favorites'),  # authenticated user
    path('delete/<str:restaurant_name>/', views.delete_favorites, name='delete_favorites'),
]
