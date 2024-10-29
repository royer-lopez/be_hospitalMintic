from rest_framework import serializers
from hospitalBacked.models.paciente import Paciente

class PasienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['usuario','medico']