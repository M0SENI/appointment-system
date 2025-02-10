from django.contrib.auth import get_user_model
from django.shortcuts import render , redirect
from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.generic import ListView, CreateView, UpdateView, FormView , View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import *
import random
import string
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import get_user_model

User = get_user_model()


def generate_code():
    return str(random.randint(100000, 999999))


class HomeTemplateView(View):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        first_form = AppointmentForm(request.POST)
        second_form = VerifyForm(request.POST)

        if 'submit_first_form' in request.POST:
            if first_form.is_valid():
                first_form.instance.user = self.request.user
                first_form.instance.save()
                success(self.request, "فرم شما ثبت و ارسال شد!")
                return redirect('home')
            else:
                error(self.request, "فرم شما ثبت نشد، لطفا مجددا امتحان کنید.")

        if 'submit_second_form' in request.POST:
            if second_form.is_valid():
                email = second_form.cleaned_data['email']
                user = User.objects.filter(email=email).first()
                code = generate_code()
                self.request.session['email'] = email
                self.request.session['code'] = code
                if user:
                    send_mail('Login Code', f'Your Login code is: {code}', from_email=settings.EMAIL_HOST_USER,
                              recipient_list=[email])
                else:
                    send_mail('SignUp Code', f'Your sign up code is: {code}', from_email=settings.EMAIL_HOST_USER,
                              recipient_list=[email])
                success(self.request, "کد به ایمیل شما ارسال شد!")
                return redirect('verify-code')
            else:
                error(self.request, "ایمیل معتبر نمی‌باشد.")

        return render(request, self.template_name, {'first_form': first_form, 'second_form': second_form})

    def get(self, request, *args, **kwargs):
        first_form = AppointmentForm()
        second_form = VerifyForm()
        return render(request, self.template_name, {'first_form': first_form, 'second_form': second_form})
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


class VerifyView(FormView):
    model = User
    template_name = 'index.html'
    form_class = VerifyForm
    success_url = reverse_lazy('verify-code')





class ContactUsView(CreateView):
    template_name = 'contact-us.html'

class AboutView(TemplateView):
    template_name = 'about-us.html'

class FaqView(TemplateView):
    template_name = 'faqs.html'