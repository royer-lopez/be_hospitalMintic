from string import printable
from rest_framework import serializers
from hospitalBacked.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','rol','username','password','apellido','e_mail','celular','direccion']