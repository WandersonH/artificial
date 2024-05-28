"""
URL configuration for artificial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from espelho import views as espelho_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', espelho_views.home, name='home'),
    path('produtos/', espelho_views.listar_produtos, name='listar_produtos'),
    path('generate_qr/', espelho_views.generate_qr_code, name='generate_qr_code'),
    path('dressing_room_limited/', espelho_views.dressing_room_limited, name='dressing_room_limited'),
    path('logout/', espelho_views.logout_view, name='logout'),
    path('usuario_app/', include('usuario_app.urls')),
    path('lojista/', include('lojista_app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),## editor lojista
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




