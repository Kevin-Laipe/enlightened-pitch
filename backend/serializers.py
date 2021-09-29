from re import T
from rest_framework import serializers

from backend.models import Bloc, Card, CardStat, Class, Finish, Keyword, Printing, Rarity, Releasenote, Set, Stat, Subtype, Supertype, Talent, Type

class CardSerializer(serializers.HyperlinkedModelSerializer):
    keywords = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='keyword-detail',
        read_only=True
    )
    cardstats = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='cardstat-detail',
        read_only=True
    )

    class Meta:
        model = Card
        fields = '__all__'

class BlocSerializer(serializers.HyperlinkedModelSerializer):
    cards = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='card-detail',
        read_only=True
    )

    class Meta:
        model = Bloc
        fields = '__all__'

class ClassSerializer(serializers.HyperlinkedModelSerializer):
    cards = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='card-detail',
        read_only=True
    )

    class Meta:
        model = Class
        fields = '__all__'

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    cards = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='card-detail',
        read_only=True
    )

    class Meta:
        model = Type
        fields = '__all__'

class TalentSerializer(serializers.HyperlinkedModelSerializer):
    cards = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='card-detail',
        read_only=True
    )

    class Meta:
        model = Talent
        fields = '__all__'

class KeywordSerializer(serializers.HyperlinkedModelSerializer):
    cards = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='card-detail',
        read_only=True
    )

    class Meta:
        model = Keyword
        fields = '__all__'

class StatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'

class CardStatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardStat
        fields = '__all__'

class ReleasenoteSerializer(serializers.HyperlinkedModelSerializer):
    cards = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='card-detail',
        read_only=True
    )

    class Meta:
        model = Releasenote
        fields = '__all__'

class SubtypeSerializer(serializers.HyperlinkedModelSerializer):
    cards = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='card-detail',
        read_only=True
    )

    class Meta:
        model = Subtype
        fields = '__all__'

class SupertypeSerializer(serializers.HyperlinkedModelSerializer):
    cards = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='card-detail',
        read_only=True
    )

    class Meta:
        model = Supertype
        fields = '__all__'

class PrintingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Printing
        fields = '__all__'

class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'

class FinishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finish
        fields = '__all__'

class RaritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rarity
        fields = '__all__'