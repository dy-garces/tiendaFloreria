import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DireccionEnvio(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    envio1 = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.envio1
    
    @property
    def direcciones(self):
        return '{}-{}'.format(self.ciudad, self.region)