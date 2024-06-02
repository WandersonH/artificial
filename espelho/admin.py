from django.contrib import admin
from .models import Produto, ExperimentationSession, KinectData, UserProfile

# Registro dos modelos no admin
admin.site.register(Produto)
admin.site.register(ExperimentationSession)
admin.site.register(KinectData)
admin.site.register(UserProfile)
