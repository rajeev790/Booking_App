from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),  # Authentication URLs
    path('railway/', include('railway.urls')),      # Railway booking URLs
    path('hotel/', include('hotel.urls')),          # Hotel booking URLs
    path('trip/', include('trip.urls')),            # Trip booking URLs
    path('metro/', include('metro.urls')),          # Metro booking URLs
]
