from django.urls import path
from . import views

app_name = 'comidas'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_comida, name='create'),
    path('<int:pk>/', views.detail_comida, name='detail'),
    path('<int:pk>/update/', views.update_comida, name='update'),
    path('<int:pk>/delete/', views.delete_comida, name='delete'),
]