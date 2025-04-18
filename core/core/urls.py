from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include("accounts.urls") , name="account"),
    path("", include("home.urls") , name="home"),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL ,document_root=settings.STATICFILES_DIRS[0])
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'home.views.custom_404'
