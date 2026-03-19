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
    if request.method == 'POST':
        qr_code_image = request.FILES.get('qr_code_image')
        if not qr_code_image:
            return render(request, 'scanner/scan_qr.html', context={'error': 'Please upload a QR code image.'})
        try:
            img = Image.open(qr_code_image)
            decoded_data = decode(img)
            if not decoded_data:
                return render(request, 'scanner/scan_qr.html', context={'error': 'No QR code found in the image.'})
            data = decoded_data[0].data.decode('utf-8').strip()
            name, roll_num = data.split(' | ')
            profile = Profile.objects.filter(name=name, roll_number=roll_num).first()
            if profile:
                profile.delete()  # Delete the profile after successful scan to prevent reuse
                del_img_path = settings.MEDIA_ROOT / 'qr_codes' / f"{name}_{roll_num}.png"
                if del_img_path.exists():
                    del_img_path.unlink()  # Delete the QR code image after successful scan
                return render(request, 'scanner/scan_qr.html', context={'success': f'Welcome {profile.name}! Your roll number is {profile.roll_number}.'})
            else:
                return render(request, 'scanner/scan_qr.html', context={'error': 'Profile not found. Please check your QR code or Creat Profile'})
        except Exception as e:
            return render(request, 'scanner/scan_qr.html', context={'error': f'Error processing the QR code: {str(e)}'})
    return render(request, 'scanner/scan_qr.html')