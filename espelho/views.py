from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from io import BytesIO
import subprocess

def home_view(request):
    start_voice_recognition()
    return render(request, 'espelho/home.html')

def generate_qr_code(request):
    url = "http://127.0.0.1:8000/usuario_app/login/"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = buffer.getvalue()

    return HttpResponse(img_str, content_type="image/png")

def dressing_room_limited_view(request):
    return render(request, 'espelho/dressing_room_limited.html')

def dressing_room_view(request):
    return render(request, 'espelho/dressing_room.html')

def camera_view(request):
    return render(request, 'espelho/camera.html')

def profile_view(request):
    return render(request, 'espelho/profile.html')

def login_view(request):
    return render(request, 'espelho/login.html')

def listar_produtos(request):
    # Adicione o código da lógica desta view aqui
    pass

def logout_view(request):
    # Adicione o código da lógica desta view aqui
    pass

def start_voice_recognition():
    subprocess.Popen(["python", "/Volumes/Untitled/ARtificial/.venv/artificial/kinect_voice_recognition.py"])
