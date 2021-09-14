from django.db import models
from django.db.models.fields import SmallIntegerField
from django.utils.translation import gettext_lazy as _

def image_directory_path(instance, filename):
    return 'images/{0}'.format(filename)

class Set(models.Model):
    ''' Welcome to Rathe, Arcane Rising... '''
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=5)

class Keyword(models.Model):
    ''' Go again, Dominate, Blade Break... '''
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=150)

class Subtype(models.Model):
    ''' (1H), Chest, Aura... '''
    name = models.CharField(max_length=20)

class Talent(models.Model):
    ''' Shadow, Light, Elemental, Ice, Lightning... '''
    name = models.CharField(max_length=20)

class Releasenote(models.Model):
    ''' Rulling released by LSS upon a card's release '''
    text = models.CharField(max_length=500)

class Stat(models.Model):
    ''' Pitch, cost, defense, attack '''
    name = models.CharField(max_length=10)

class Printing(models.Model):
    '''  '''
    class Finish(models.TextChoices):
        REGULAR = '', _('Regular')
        RAINBOW_FOIL = 'RF', _('Rainbow Foil')
        COLD_FOIL = 'CF', _('Cold Foil')
        EXTENDED_ART = 'EA', _('Extended Art')
        ALTERNATE_ART = 'AA', _('Alternate Art')

    class Rarity(models.TextChoices):
        COMMON = 'C', _('Common')
        RARE = 'R', _('Rare')
        SUPER_RARE = 'S', _('Super Rare')
        MAJESTIC = 'M', _('Majestic')
        LEGENDARY = 'L', _('Legendary')
        FABLED = 'F', _('Fabled')
        PROMO = 'P', _('Promo')

    sku = models.CharField(max_length=15, unique=True)
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE) #TODO
    finish = models.CharField(
        max_length=2,
        choices=Finish.choices,
        default=Finish.REGULAR,
    )
    image = models.ImageField(upload_to=image_directory_path)
    artist = models.CharField(max_length=30)
    set_id = models.ForeignKey('Set', on_delete=models.CASCADE)
    is_first_edition = models.BooleanField(null=True)
    rarity = models.CharField(
        max_length=1,
        choices=Rarity.choices,
    )

class Card(models.Model):
    class Class(models.IntegerChoices):
        GENERIC = 0
        BRUTE = 1
        GUARDIAN = 2
        NINJA = 3
        WARRIOR = 4
        MECHANOLOGIST = 5
        RANGER = 6
        RUNEBLADE = 7
        WIZARD = 8
        MERCHANT = 9
        SHAPESHIFTER = 10
        ILLUSIONIST = 11

    class Type(models.IntegerChoices):
        NON_ATTACK_ACTION = 0
        ATTACK_ACTION = 1
        ATTACK_REACTION = 2
        DEFENSE_REACTION = 3
        INSTANT = 4
        EQUIPMENT = 5
        WEAPON = 6
        HERO = 7

    name = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    _class = models.IntegerField(choices=Class.choices)
    _type = models.IntegerField(choices=Type.choices)

class CardKeyword(models.Model):
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)
    keyword_id = models.ForeignKey('Keyword', on_delete=models.CASCADE)

class CardSubtype(models.Model):
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)
    subtype_id = models.ForeignKey('Subtype', on_delete=models.CASCADE)

class CardTalent(models.Model):
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)
    talent_id = models.ForeignKey('Talent', on_delete=models.CASCADE)

class CardReleasenote(models.Model):
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)
    releasenote_id = models.ForeignKey('Releasenote', on_delete=models.CASCADE)

class CardStat(models.Model):
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)
    stat_id = models.ForeignKey('Stat', on_delete=models.CASCADE)
    value = models.SmallIntegerField()