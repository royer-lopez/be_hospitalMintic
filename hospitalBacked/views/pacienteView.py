from rest_framework import status
from rest_framework.response import Response
from hospitalBacked.models.paciente import Paciente
from hospitalBacked.serializers.pasienteSelializer import PasienteSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def createPaciente(request):
    if request.method == 'GET':
        modelo=Paciente.objects.all()
        serializer = PasienteSerializer(modelo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=PasienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT','DELETE'])
def detailPaciente(request,pk):
    if request.method == 'PUT':
        modelo=Paciente.objects.get(pk=pk)
        serializer = PasienteSerializer(modelo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        modelo= Paciente.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
   