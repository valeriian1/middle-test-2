from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.main, name='main'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
]
