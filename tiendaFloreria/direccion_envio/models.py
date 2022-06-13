import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DireccionEnvio(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    envio1 = models.CharField(max_length=200)
    envio2 = models.CharField(max_length=200, blank=True)
    ciudad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    default = models.BooleanField(default=False)
    creacion = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.envio1
    