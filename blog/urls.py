from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView, CommentReplyView

app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='blog'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/comment/<int:comment_pk>/reply/', CommentReplyView.as_view(), name='comment_reply'),
] 