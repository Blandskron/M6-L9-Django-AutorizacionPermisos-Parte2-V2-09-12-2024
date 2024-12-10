from rest_framework import viewsets
from .serializers import EscuelaSerializer
from .models import Escuela

# Create your views here.
class EscuelaViewSet(viewsets.ModelViewSet):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer
