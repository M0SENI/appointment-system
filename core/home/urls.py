from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path("", HomeTemplateView.as_view(), name="home"),
    path ('add-appointment/' , AppointmentAddView.as_view(), name="add-appointment"),
    path('manage-appointments/' , ManageAppointmentTemplateView.as_view(), name="manage-appointments" ),
    path('contact-us/' , ContactUsView.as_view(), name="contact-us" ),
    path('about/' , AboutView.as_view(), name="about-us" ),
    path('faq/' , FaqView.as_view(), name="faq" ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
