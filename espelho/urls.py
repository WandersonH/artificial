from django.urls import path
from .views import home_view, login_view, dressing_room_limited_view, dressing_room_view, camera_view, profile_view, listar_produtos, generate_qr_code, logout_view

app_name = 'espelho'

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('dressing_room_limited/', dressing_room_limited_view, name='dressing_room_limited'),
    path('dressing_room/', dressing_room_view, name='dressing_room'),
    path('camera/', camera_view, name='camera'),
    path('profile/', profile_view, name='profile'),
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('generate_qr/', generate_qr_code, name='generate_qr_code'),
    path('logout/', logout_view, name='logout'),
]
