from django.shortcuts import render, redirect
from .models import Produto
from django.http import HttpResponse
import qrcode

# View para a home page
def home(request):
    return render(request, 'espelho/home.html')

# View para listar produtos
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'espelho/listar_produtos.html', {'produtos': produtos})

# QR code
def generate_qr_code(request):
    data = request.build_absolute_uri('/usuario_app/authorize_login')
    img = qrcode.make(data)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

def dressing_room_limited(request):
    return render(request, 'espelho/dressing_room_limited.html')

def logout_view(request):
    return redirect('/')
