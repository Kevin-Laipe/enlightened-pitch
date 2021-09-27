from rest_framework import viewsets

from .serializers import BlocSerializer, CardSerializer
from .models import Bloc, Card

class CardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Cards.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class BlocViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Blocs.
    """
    queryset = Bloc.objects.all()
    serializer_class = BlocSerializer