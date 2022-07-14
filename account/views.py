from django.shortcuts import redirect, render
# from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from .forms import *
from .models import User
# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'main/profile.html'

    def get_object(self):
        user = User.objects.get(id=self.request.user.id)
        return user

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            auth.login(request,user)
            return redirect('/profile/')
    else:
        form = UserRegisterForm()
    return render(request, "main/register.html", {"form":form})

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('name', 'surname', 'avatar', 'username', 'age', 'phone', 'address')
    template_name = 'main/update_profile.html'
    success_url = '/profile/'

    def get_object(self):
        user = User.objects.get(id=self.request.user.id)
        return user

