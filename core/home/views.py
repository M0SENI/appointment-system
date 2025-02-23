from django.contrib.auth import get_user_model
from django.shortcuts import render , redirect
from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.generic import ListView, CreateView, UpdateView, FormView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.messages import *
import random
import string
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()


def generate_code():
    return str(random.randint(100000, 999999))


class HomeTemplateView(View):
    template_name = 'index.html'
    context_object_name = 'user_appointments'
    model = Appointments

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
    def get_queryset(self):
        return Appointments.objects.filter(user=self.request.user).exclude(status='pending')

class AppointmentListView(UserPassesTestMixin, ListView):
    model = Appointments
    form_class = UpdateAppointmentForm
    template_name = "appointment-list.html"
    context_object_name = "appointment"
    paginate_by = 7
    ordering = "-sent_date"
    def get_queryset(self):
        return Appointments.objects.filter(status='pending')
    def test_func(self):
        return self.request.user.is_staff

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



class AppointmentUpdateView(UserPassesTestMixin , UpdateView):
    model = Appointments
    form_class = UpdateAppointmentForm
    template_name = 'appointment-update.html'
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('appointments-list')
    def test_func(self):
        return self.request.user.is_staff



class ContactUsView(CreateView):
    template_name = 'contact-us.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self ,  form):
        if not form.is_valid():
            error(self.request ,"فرم شما ثبت نشد , لطفا مجددا امتحان کنید.")
            return self.form_invalid(form)
        form.instance.user = self.request.user
        form.instance.save()
        success(self.request , "فرم شما ثبت و ارسال شد!")
        return super().form_valid(form)


class ManageAppointments(LoginRequiredMixin,ListView):
    template_name = 'manage-appointments.html'
    model = Appointments
    paginate_by = 4
    context_object_name = "user_appointments"
    def get_queryset(self):
        return Appointments.objects.filter(user=self.request.user , status='pending')


class DeleteAppointmentView(DeleteView):
    model = Appointments
    success_url = reverse_lazy('manage-appointments')
    template_name = 'delete-appointment.html'

class EditAppointmentsView(UpdateView):
    model = Appointments
    form_class = AppointmentForm
    template_name = 'user-edit-appointments.html'
    success_url = reverse_lazy('manage-appointments')
    template_name_suffix = "_update_form"

class ReminderView(LoginRequiredMixin,ListView):
    model = Appointments
    template_name = 'reminder.html'
    context_object_name = "checked_appointments"
    def get_queryset(self):
        return Appointments.objects.filter(user=self.request.user).exclude(status='pending')























class AboutView(TemplateView):
    template_name = 'about-us.html'

class FaqView(TemplateView):
    template_name = 'faqs.html'




