from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import BlocSerializer, CardSerializer, CardStatSerializer, ClassSerializer, FinishSerializer, ImageSerializer, KeywordSerializer, PrintingSerializer, RaritySerializer, ReleasenoteSerializer, SetSerializer, StatSerializer, SubtypeSerializer, SupertypeSerializer, TalentSerializer, TypeSerializer, ArtistSerializer, FormatSerializer
from .models import Bloc, Card, CardStat, Class, Finish, Image, Keyword, Printing, Rarity, Releasenote, Set, Stat, Subtype, Supertype, Talent, Type, Artist, Format

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

class SupertypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Supertype.
    """
    queryset = Supertype.objects.all()
    serializer_class = SupertypeSerializer

class StatViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Stats.
    """
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

class CardStatViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view CardStats.
    """
    queryset = CardStat.objects.all()
    serializer_class = CardStatSerializer

class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Images.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, pk=None):
        image = get_object_or_404(self.queryset)
        serializer = ImageSerializer.get_image_url(image, context={'request': request})
        print(serializer.data)
        return Response(serializer.data)

class PrintingViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Sets.
    """
    queryset = Printing.objects.all()
    serializer_class = PrintingSerializer

class SetViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Sets.
    """
    queryset = Set.objects.all()
    serializer_class = SetSerializer

class FinishViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Finishes.
    """
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer

class RarityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Rarities.
    """
    queryset = Rarity.objects.all()
    serializer_class = RaritySerializer

class FormatViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Formats.
    """
    queryset = Format.objects.all()
    serializer_class = FormatSerializer

class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to view Artists.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer