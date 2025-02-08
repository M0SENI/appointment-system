from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Appointments
from django.views.generic import ListView , CreateView , UpdateView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.contrib.messages import *


class HomeTemplateView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject=f"{name} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")


class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("fname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointments.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks {fname} for making an appointment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)


class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointments
    queryset = Appointments.objects.filter(status='pending')
    context_object_name = "appointments"
    paginate_by = 8
    # is staff needed

class AppointmentAddView(LoginRequiredMixin,CreateView):
    model = Appointments
    form_class = AppointmentForm
    template_name = 'appointment.html'
    success_url = '/make-an-appointment/'

    def form_valid(self ,  form):
        form.instance.user = self.request.user
        form.instance.save()
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