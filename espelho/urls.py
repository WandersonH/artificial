from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('generate_qr/', views.generate_qr_code, name='generate_qr_code'),
    path('dressing_room_limited/', views.dressing_room_limited, name='dressing_room_limited'),
    path('logout/', views.logout_view, name='logout'),
]
