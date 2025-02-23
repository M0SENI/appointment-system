from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path("", HomeTemplateView.as_view(), name="home"),
    path ('add-appointment/' , AppointmentAddView.as_view(), name="add-appointment"),
    path('appointment-list/' , AppointmentListView.as_view(), name="appointments-list" ),
    path('appointment-list/edit/<int:pk>' , AppointmentUpdateView.as_view(), name="edit-appointments" ),
    path('manage-appointments/' , ManageAppointments.as_view(), name="manage-appointments" ),
    path('manage-appointments/<int:pk>' , EditAppointmentsView.as_view(), name="user-edit-appointments" ),
    path('delete-appointments/<int:pk>' , DeleteAppointmentView.as_view(), name="user-delete-appointments" ),
    path('reminder/' , ReminderView.as_view(), name="reminder" ),
    path('contact-us/' , ContactUsView.as_view(), name="contact-us" ),
    path('about/' , AboutView.as_view(), name="about-us" ),
    path('faq/' , FaqView.as_view(), name="faq" ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
