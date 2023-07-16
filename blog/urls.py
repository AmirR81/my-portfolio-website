from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView

app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='blog'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
] 