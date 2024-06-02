from django.db import models
from usuario_app.models import Usuario
from lojista_app.models import Produto

class KinectData(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    joint_positions = models.JSONField()
    height = models.FloatField()
    shoulder_width = models.FloatField()
    arm_length = models.FloatField()
    chest_circumference = models.FloatField()
    waist_circumference = models.FloatField()
    hip_circumference = models.FloatField()

    def __str__(self):
        return f"Kinect Data for {self.usuario} at {self.timestamp}"

class ExperimentationSession(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    kinect_data = models.ForeignKey(KinectData, on_delete=models.CASCADE)

    def __str__(self):
        return f"Session for {self.usuario} with {self.produto} at {self.timestamp}"

class UserProfile(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return f"Profile of {self.usuario}"
