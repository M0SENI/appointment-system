from django.db import models
from django.contrib.auth import get_user_model
from django.http import request

User = get_user_model()

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='appointment_user')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        ordering = ["-sent_date"]
        
class Accepted(models.Model):
    pass