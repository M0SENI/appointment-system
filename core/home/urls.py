from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentAddView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("manage-appointments/update/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("manage-appointments/update/<int:pk>/" , AppointmentUpdateView.as_view(), name="update-appointment" ),
    # path("manage-appointments/accepted/" , AppointmentUpdateView.as_view(), name="update-appointment" ),
    # path("manage-appointments/rejected/" , AppointmentUpdateView.as_view(), name="update-appointment" ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
