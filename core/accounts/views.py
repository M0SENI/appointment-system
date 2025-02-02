from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


class LoginView(LoginRequiredMixin, View):
    login_url = "/users/"
    redirect_field_name = "redirect_to"
    def email_check(self):
        print('email_check')
        return self.request.user.username.startswith("admin")
    def password_check(self):
        print('password_check')
        return self.request.user.password.startswith("<PASSWORD>")
    def post(self, request, *args, **kwargs):
        if not self.email_check():
            raise PermissionDenied