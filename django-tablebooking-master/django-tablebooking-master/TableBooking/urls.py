from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('booking/',include('Booking.urls',namespace='booking')),
    path('',include('Menu.urls')),
    path('',include('Contact.urls')),
    path('',include('About.urls')),
path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
path('accounts/',include('account.urls')),

]

urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
