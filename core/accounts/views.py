from django.contrib.auth import login
from django.shortcuts import render , redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy , reverse
from django.views.generic import FormView, CreateView
from .forms import *
from .models import User
from django.contrib.messages import *
from django.conf import settings
import random
import string
from django.contrib.auth import logout




class VerifyCodeView(FormView):
    template_name = 'verify_code.html'
    form_class = VerifyCodeForm
    success_url = reverse_lazy('passwords')

    def form_valid(self, form):
        entered_code = form.cleaned_data['code']
        stored_code = self.request.session.get('code')
        if entered_code == stored_code:
            email = self.request.session.get('email')
            user = User.objects.filter(email=email).first()
            if user:
                self.request.session.set_expiry(1209600)
                login(self.request, user)
                return redirect('home')
            else:
                return super().form_valid(form)
        else:
            form.add_error('code', 'Verification code is incorrect')
            return self.form_invalid(form)


class SetPasswordView(FormView):
    template_name = 'set_password.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        password = form.cleaned_data['password']
        email = self.request.session.get('email')
        user, created = User.objects.get_or_create(email=email)
        user.set_password(password)
        user.save()
        login(self.request, user)
        self.request.session.set_expiry(1209600)
        success(self.request, message="با موفقیت وارد حساب شدید!")
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('home')

