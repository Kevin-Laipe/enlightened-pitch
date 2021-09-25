from attr import s
from django.db import models
from django.contrib.auth.models import AbstractUser
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
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=500)
    notes = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

class Subtype(models.Model):
    ''' (1H), Chest, Aura... '''
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Talent(models.Model):
    ''' Shadow, Light, Elemental... '''
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Releasenote(models.Model):
    ''' Rullings released by LSS upon a card's release '''
    text = models.TextField(max_length=5000)

class Stat(models.Model):
    '''Cost, defense, attack '''
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Supertype(models.Model):
    ''' Ice, Earth, Lightning... '''
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Class(models.Model):
    ''' Generic, Brute, Runeblade... '''
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "classes"

class Type(models.Model):
    ''' Action, instant, defense reaction... '''
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Bloc(models.Model):
    ''' Play sets (as opposed to master sets)... '''
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

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
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    _class = models.ForeignKey('Class', on_delete=models.CASCADE, blank=True, null=True)
    _type = models.ForeignKey('Type', on_delete=models.CASCADE)
    talent = models.ForeignKey('Talent', on_delete=models.CASCADE, blank=True, null=True)
    bloc = models.ForeignKey('Bloc', on_delete=models.CASCADE)
    is_banned_cc = models.BooleanField(default=False)
    is_banned_blitz = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique card')
        ]

    def __str__(self):
        # TODO: if the card has different pitch versions, add its color to its name
        return "%s" % (self.name)

class CardKeyword(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.card, self.keyword)
        
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['card', 'keyword'], name='A card cannot have the same keyword more than once')
        ]

class CardSubtype(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    subtype = models.ForeignKey('Subtype', on_delete=models.CASCADE)
        
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['card', 'subtype'], name='A card cannot have the same subtype more than once')
        ]

class CardReleasenote(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    releasenote = models.ForeignKey('Releasenote', on_delete=models.CASCADE)
        
    def __str__(self):
        return str(self.card)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['card', 'releasenote'], name='A card cannot have the same release note more than once')
        ]

class CardStat(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    stat = models.ForeignKey('Stat', on_delete=models.CASCADE)
    value = models.CharField(max_length=5)
        
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['card', 'stat'], name='A card cannot have the same stat more than once')
        ]

class CardSupertype(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    supertype = models.ForeignKey('Supertype', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['card', 'supertype'], name='A card cannot have the same super-type more than once')
        ]

class Deck(models.Model):
    creator = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField(max_length=5000)

class DeckCard(models.Model):
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    in_sideboard = models.PositiveSmallIntegerField()

class Copy(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    printing = models.ForeignKey('Printing', on_delete=models.CASCADE)
    amount_owned = models.PositiveSmallIntegerField()
    amount_wanted = models.PositiveSmallIntegerField()
    amount_trading = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "copies"

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