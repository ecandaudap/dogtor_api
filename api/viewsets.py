"""REST API viewsets"""

from rest_framework import viewsets, response, decorators, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from . import models, serializers


class OwnerViewSet(viewsets.ModelViewSet):
    """Owner viewset"""
    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    @decorators.action(detail=False, methods=["post"])
    def auth(self, request):
        # Lógica para autenticar al usuario
        email = request.data.get("email")
        password = request.data.get("password")        
        return response.Response({"token": "lkajshdlkfjhaslkdjhflkasjhdfklj"})



class SpeciesViewSet(viewsets.ModelViewSet):
    """Species viewset"""
    queryset = models.Species.objects.all()
    serializer_class = serializers.SpeciesModelSerializer

class PetViewSet(viewsets.ModelViewSet):
    """Pet viewset"""
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetModelSerializer

class RecordViewSet(viewsets.ModelViewSet):
    """Pet viewset"""
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordModelSerializer





