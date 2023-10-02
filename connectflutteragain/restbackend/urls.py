from django.conf import settings
from . import views
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'playareas', PlayAreaViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'users', UserViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'bookings', AdminViewSet)



urlpatterns = [
    # ... other URL patterns for your app ...
    path('api/', include(router.urls)),  # Include the router's URLs under '/api/'
    path('vendor_registration/', views.vendor_registration, name='vendor_registration'),
    path('vendor_login/', views.vendor_login, name='vendor_login'),
    path('vendor_area/', views.vendor_area, name='vendor_area'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
