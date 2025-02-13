from django.db.models import *
from django.contrib.auth import get_user_model
from django.http import request
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class Appointments(Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار پاسخ'),
        ('accepted', 'تایید شده'),
        ('rejected', 'لغو  شده'),
    ]
    user = ForeignKey(User, on_delete=CASCADE , related_name='appointments_user')
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone = CharField(max_length=50)
    request = TextField(blank=True)
    status = CharField(max_length=50,blank=True , choices=STATUS_CHOICES, default='pending')
    note = TextField(blank=True)
    sent_date = DateField(auto_now_add=True)
    checked_date = DateField(auto_now=True)


    class Meta:
        ordering = ["-sent_date"]
        verbose_name_plural = "Appointments"
        verbose_name = "Appointment"


class Contact(Model):
    user = ForeignKey(User, on_delete=CASCADE , related_name='contact_user')
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone = CharField(max_length=50)
    request = TextField(blank=True)
    answer = TextField(blank=True)
    created_date = DateField(auto_now_add=True)

    class Meta:
        ordering = ["-created_date"]
        verbose_name_plural = "Contacts"
        verbose_name = "Contact"
