import qrcode
from PIL import Image
from io import BytesIO
from pathlib import Path
from django.conf import settings    
from pyzbar.pyzbar import decode
from django.shortcuts import render
from scanner.models import Profile
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    return render(request, 'scanner/home.html')

def generate_qr(request):
    if request.method == 'POST':
        name = request.POST.get("data")
        roll_num = request.POST.get("num")
        # validate input
        if not name or not roll_num:
            return render(request, 'scanner/generate_qr.html', context = {'error': 'Please provide both name and roll number.'})
        # generate qrcode
        data = f"{name} | {roll_num}"
        qr_code = qrcode.make(data)
        qr_code_io = BytesIO()
        qr_code.save(qr_code_io, format='PNG')
        qr_code_io.seek(0)
        # storage location for qrcode
        qr_storage_path = settings.MEDIA_ROOT / 'qr_codes'
        fs = FileSystemStorage(location=qr_storage_path, base_url='/media/qr_codes/')
        filename = f"{name}_{roll_num}.png"
        fs.save(filename, ContentFile(qr_code_io.read()))
        qr_img_url = fs.url(filename)
        Profile.objects.create(name=name, roll_number=roll_num)
        return render(request, 'scanner/generate_qr.html', context = {'qr_img_url': qr_img_url})
    return render(request, 'scanner/generate_qr.html')

def scan_qr(request):
    return render(request, 'scanner/scan_qr.html')