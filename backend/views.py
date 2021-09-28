from rest_framework import viewsets

from .serializers import BlocSerializer, CardSerializer, ClassSerializer, KeywordSerializer, ReleasenoteSerializer, SubtypeSerializer, TalentSerializer, TypeSerializer
from .models import Bloc, Card, Class, Keyword, Releasenote, Subtype, Talent, Type

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

class ClassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Classes.
    """
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Types.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TalentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Talents.
    """
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer

class KeywordViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Keywords.
    """
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class ReleasenoteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Releasenotes.
    """
    queryset = Releasenote.objects.all()
    serializer_class = ReleasenoteSerializer

class SubtypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Subtypes.
    """
    queryset = Subtype.objects.all()
    serializer_class = SubtypeSerializer