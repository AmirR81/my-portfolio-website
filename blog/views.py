from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Project, Comment
from .forms import CommentCreateForm, CommentReplyForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class HomeView(View):
    def get(self, request):
        return render(request, 'blog/home.html')


class ProjectListView(ListView):
    model = Project
    template_name = 'blog/project_list.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search :
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))
        return queryset
    

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
        context['form_reply'] = CommentReplyForm(  )
        comments = self.object.projectcomment.filter(is_reply=False)
        context['comments'] = comments
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.project = self.get_object()
            comment.save()
        return redirect('home:project_detail', pk=self.kwargs['pk'])




class CommentReplyView(View):

    def post(self, request, *args, **kwargs):
        form = CommentReplyForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.project = get_object_or_404(Project, pk=self.kwargs['pk'])
            comment.reply = get_object_or_404(Comment, pk=self.kwargs['comment_pk'])
            comment.is_reply = True
            comment.save()
        return redirect('home:project_detail', pk=self.kwargs['pk'])


