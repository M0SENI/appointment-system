from django.contrib.auth import login
from django.shortcuts import render , redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .forms import *
from .models import User
from django.contrib.messages import *


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password1 != password2:
            form.add_error('password2', 'Passwords don\'t match')
            return self.form_invalid(form)

        user = form.save(commit=False)
        user.email = email
        user.set_password(password1)
        user.save()
        login(self.request, user)

        success(self.request, "Registration successful.")
        return super(RegistrationView, self).form_valid(form)


