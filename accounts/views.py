from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserSignupForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class UserSignupView(View):
    form_class = UserSignupForm   #اینجا دیگه نیازی نیست بعد از فرم پرانتز بزاری!
    template_name = 'accounts/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:blog')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()   # یا form = UserSignupForm()   hard coding!
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            messages.success(request, 'You have successfully signed up.', 'success')
            return redirect('home:blog')
        return render(request, self.template_name, {'form':form})
    


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:blog')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully!', 'success')
                return redirect('home:blog')
            else:
                messages.error(request, 'username or password is warng!', 'warning')

        return render(request, self.template_name, {'form':form})
    



class UserLogoutView(LoginRequiredMixin, View):
    #login_url = '/account/login/'   تو تنظیمات گذاشتیش(با حروف بزرگ باید باشه اونجا!)
    def get(self, request):
        logout(request)
        messages.success(request, 'you loggedout successfuly!', 'success')
        return redirect('home:blog')


