# Por exemplo: se você quiser criar uma API que disponibilize apenas listagem de uma determinada Entidade você poderia escolher a ListAPIView.
#
# Agora se você precisar construir uma API que disponibilize apenas as operações de criação e listagem, você poderia utilizar a ListCreateAPIView.
#
# Agora se você precisar construir uma API “com tudo dentro” (isto é: criação, deleção, atualização e listagem), escolha a ModelViewSet: perceba que ela estende todos os Mixins disponíveis.

from django.shortcuts import render
from api.serializers import FundoImobiliarioSerializer
from rest_framework import viewsets, permissions
from api.models import FundoImobiliario


# Create your views here.

class FundoImobiliarioViewSet(viewsets.ModelViewSet):
    queryset = FundoImobiliario.objects.all()
    serializer_class = FundoImobiliarioSerializer
    permission_classes = [permissions.IsAuthenticated]
