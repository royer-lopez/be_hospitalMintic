from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBacked.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBacked.models.usuario import Usuario

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("Get a todos los Usuarios")
        queryset = self.get_queryset()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)
    
    """ 
    def post(self, request, *args, **kwargs):
        print("POST a Usuario")
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        return Response(status=status.HTTP_201_CREATED)
        
         tokenData = {
                       " username": request.data["username"],
                       "password": request.data["password"]
                      }
        tokenSerializer = TokenObtainPairSerializer(data.tokenData)
        """
class UsuarioRetrieveupdatetoDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'id'  # campo con el que se realiza la busqueda del objtt
    lookup_url_kwarg = 'pk' #nobre dado en la url al argumento
    #permission_Classes = ()

    def get(self, request, *args, **kwargs):
        print("GET A Usuario")
        """
        if valid_data['user_id'] != kwargs['pk']:
           stringResponse = {'detail':'Unauthorized Request'}
           return Response(StringResponse, status=status.HTTP_401_UNAUTHORIZED)
        """
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        print("put A Usuario")
        """
        if valid_data{'user_id'} != kwargs['pk']:
           stringResponse = {'detail':'Unauthorized Request'}
           return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        """
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print("Delete an Usuario")
        """
        if valid_data{'user_id'} != kwargs['pk']:
           stringResponse = {'detail':'Unauthorized Request'}
           return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        """
        return super().delete(request, *args, **kwargs) 