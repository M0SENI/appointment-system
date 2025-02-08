from django.contrib import admin
from .models import Appointments

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    model = Appointments
    list_display = ("user" , "last_name" , "status" ,"phone")
    list_filter = ('status' , )


admin.site.register(Appointments , AppointmentAdmin)

