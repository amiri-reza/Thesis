from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    FormView
)
from users.forms import SignUpForm, SignInForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.views import LogoutView
import logging
from users.models import Users


class HomeView(TemplateView):
    template_name = "users/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["user"] = Users.objects.get(id = self.request.user.id)
        return context

class SignIn(FormView):
    template_name = "users/signin.html"
    form_class = SignInForm
    success_url = reverse_lazy("users:home")
    redirect_authenticated_user = True

    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        logger = logging.getLogger(__name__)
        return self.render_to_response(self.get_context_data(form=form))



class SignUp(FormView):
    form_class = SignUpForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("users:signin")
    redirect_authenticated_user = True

    def form_valid(self, form):
        form.save()
        logout(self.request)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        logger = logging.getLogger(__name__)
        return self.render_to_response(self.get_context_data(form=form))
    
class SignOut(LogoutView):
    next_page = reverse_lazy("users:signin")


    
class DeleteUser(DeleteView):
    model = Users
    template_name = "users/delete.html"
    success_url = reverse_lazy("users:signup")


class UpdateUser(UpdateView):
    model = Users
    template_name= "users/update.html"
    context_object_name = "user"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
        user_pk = self.request.user.id
        return reverse_lazy("users:detail", kwargs={"pk": user_pk})


class DetailUser(DetailView):
    model = Users
    template_name = "users/detail.html"
    context_object_name = "user"
    

