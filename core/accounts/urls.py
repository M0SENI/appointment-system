from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('verify-code/', VerifyCodeView.as_view(), name='verify-code'),
    path('verify/password/', SetPasswordView.as_view(), name='passwords'),
    path('logout/', logout_view, name='logout'),



]