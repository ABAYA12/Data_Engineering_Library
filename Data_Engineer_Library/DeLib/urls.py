from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pipelines/', views.pipeline_list, name='pipeline_list'),
    path('pipelines/add/', views.pipeline_add, name='pipeline_add'),
    path('pipelines/<int:pk>/', views.pipeline_detail, name='pipeline_detail'),
    path('pipelines/<int:pk>/edit/', views.pipeline_edit, name='pipeline_edit'),
    path('pipelines/<int:pk>/delete/', views.pipeline_delete, name='pipeline_delete'),
]
