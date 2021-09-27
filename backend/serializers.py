from rest_framework import serializers

from backend.models import Bloc, Card

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['name', 'text', 'bloc', 'is_banned_cc', 'is_banned_blitz']

class BlocSerializer(serializers.HyperlinkedModelSerializer):
    cards = serializers.HyperlinkedRelatedField(many=True, view_name='card-detail', read_only=True)

    class Meta:
        model = Bloc
        fields = '__all__'