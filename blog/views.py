from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Project
from .forms import CommentCreateForm


class HomeView(View):
    def get(self, request):
        return render(request, 'blog/home.html')


class ProjectListView(ListView):
    model = Project
    template_name = 'blog/project_list.html'
    context_object_name = 'projects'
    

class ProjectDetailView(DetailView):
    model = Project
    form_class = CommentCreateForm
    template_name = 'blog/project_detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentCreateForm()
        comments = self.object.projectcomment.filter(is_reply=False)
        context['comments'] = comments
        return context


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.project = self.get_object()
            comment.save()
        return redirect('home:project_detail', pk=self.kwargs['pk'])

