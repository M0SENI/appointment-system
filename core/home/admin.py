from django.contrib import admin
from .models import *

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    model = Appointments
    list_display = ("user" , "last_name" , "status" ,"phone")
    list_filter = ('status' , )


class ContactAdmin(admin.ModelAdmin):
    model = Appointments
    list_display = ("user" ,"first_name" , "last_name" ,"phone")
    list_filter = ('first_name' , "last_name" , )


admin.site.register(Appointments , AppointmentAdmin)
admin.site.register(Contact , ContactAdmin)

