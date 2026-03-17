from django.urls import path
from scanner.views import home, generate_qr, scan_qr

urlpatterns = [
    path('', home, name='home'),
    path('generate/', generate_qr, name='generate_qr'),
    path('scan/', scan_qr, name='scan_qr'),
]