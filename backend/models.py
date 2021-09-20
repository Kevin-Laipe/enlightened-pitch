from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import constraints
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import UserManager

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
    ''' Shadow, Light, Elemental... '''
    name = models.CharField(max_length=20)

class Releasenote(models.Model):
    ''' Rulling released by LSS upon a card's release '''
    text = models.CharField(max_length=500)

class Stat(models.Model):
    '''Cost, defense, attack '''
    name = models.CharField(max_length=10)

class Supertype(models.Model):
    ''' Ice, Earth, Lightning... '''
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

    class Pitch(models.IntegerChoices):
        NONE = 0
        RED = 1
        YELLOW = 2
        BLUE = 3

    name = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    _class = models.IntegerField(choices=Class.choices)
    _type = models.IntegerField(choices=Type.choices)
    pitch = models.IntegerField(choices=Pitch.choices)
    is_banned = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'pitch'], name='unique card')
        ]

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

class CardSupertype(models.Model):
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)
    supertype_id = models.ForeignKey('Supertype', on_delete=models.CASCADE)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Deck(models.Model):
    creator = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField(max_length=5000)

class DeckCard(models.Model):
    deck_id = models.ForeignKey('Deck', on_delete=models.CASCADE)
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    in_sideboard = models.PositiveSmallIntegerField()

class Copy(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    printing_id = models.ForeignKey('Printing', on_delete=models.CASCADE)
    amount_owned = models.PositiveSmallIntegerField()
    amount_wanted = models.PositiveSmallIntegerField()
    amount_trading = models.PositiveSmallIntegerField()