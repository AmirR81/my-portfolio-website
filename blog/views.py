from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Project


class HomeView(View):
    def get(self, request):
        return render(request, 'blog/home.html')


class ProjectListView(ListView):
    model = Project
    template_name = 'blog/project_list.html'
    context_object_name = 'projects'
    

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'blog/project_detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs['pk'])