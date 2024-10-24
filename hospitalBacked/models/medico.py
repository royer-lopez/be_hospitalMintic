from django.db import models
from .usuario import Usuario

class Medico(models.Model):
    id= models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, related_name='medico', on_delete=models.CASCADE)
    especilidad= models.CharField('Especialidad', max_length=45)
    registro= models.CharField('registro',max_length=20)