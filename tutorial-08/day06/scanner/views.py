from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'scanner/home.html')

def generate_qr(request):
    return render(request, 'scanner/generate_qr.html')

def scan_qr(request):
    return render(request, 'scanner/scan_qr.html')