from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from .models import Appointments
from django.views.generic import ListView, CreateView, UpdateView, FormView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.contrib.messages import *


class HomeTemplateView(CreateView , LoginRequiredMixin):
    model = Appointments
    form_class = AppointmentForm
    template_name = 'index.html'
    success_url = '/make-an-appointment/'

    def form_valid(self ,  form):
        if not form.is_valid():
            error(self.request ,"فرم شما ثبت نشد , لطفا مجددا امتحان کنید.")
            return self.form_invalid(form)
        form.instance.user = self.request.user
        form.instance.save()
        success(self.request , "فرم شما ثبت و ارسال شد!")
        return super().form_valid(form)



class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointments
    queryset = Appointments.objects.filter(status='pending')
    context_object_name = "appointments"
    paginate_by = 8
    # is staff permission needed

class AppointmentAddView(LoginRequiredMixin,FormView):
    model = Appointments
    form_class = AppointmentForm
    template_name = 'appointment.html'
    success_url = '/make-an-appointment/'

    def form_valid(self ,  form):
        if not form.is_valid():
            error(self.request ,"فرم شما ثبت نشد , لطفا مجددا امتحان کنید.")
            return self.form_invalid(form)
        form.instance.user = self.request.user
        form.instance.save()
        success(self.request , "فرم شما ثبت و ارسال شد!")
        return super().form_valid(form)



class AppointmentUpdateView(UpdateView):
    model = Appointments
    form_class = UpdateAppointmentForm
    template_name = 'update-appointment.html'
    template_name_suffix = "_update_form"
    success_url = "/manage-appointments/"
    def form_valid(self , form):
        response = super().form_valid(form)
        success(self.request , "Appointment updated successfully!")
        return response



class ContactUsView(CreateView):
    template_name = 'contact-us.html'

class AboutView(TemplateView):
    template_name = 'about-us.html'

class FaqView(TemplateView):
    template_name = 'faqs.html'