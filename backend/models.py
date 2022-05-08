from ast import Delete
from operator import mod
from attr import s
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import UserManager

def image_directory_path(instance, filename):
    return 'media/images/{0}'.format(filename)

class Set(models.Model):
    ''' Welcome to Rathe, Arcane Rising... '''
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return str(self.cards.first()).replace(' (Red)', '')

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
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

class Finish(models.Model):
    ''' Card finishes (Rainbow Foil, Cold Foil, Extended Art...) '''
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "finishes"
        
class Rarity(models.Model):
    ''' Common, Rare, Legendary, Fabled... '''
    name = models.CharField(max_length=30)
    tag = models.CharField(max_length=1)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "rarities"

class Artist(models.Model):
    ''' Artist names and their portfolio '''
    name = models.CharField(max_length=40)
    portfolio = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Image(models.Model):
    ''' A printing's image file '''
    printings = models.CharField(max_length=15)
    image = models.ImageField(upload_to=image_directory_path)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.printings

class Printing(models.Model):
    ''' Physical representation of a Card '''
    uid = models.CharField(max_length=15, unique=True, primary_key=True)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    finish = models.ForeignKey('Finish', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    set = models.ForeignKey('Set', on_delete=models.CASCADE)
    is_first_edition = models.BooleanField(blank=True, null=True)
    rarity = models.ForeignKey('Rarity', on_delete=models.CASCADE)
    flavour_text= models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.card.name

class CardStat(models.Model):
    ''' Join table between a Card and a Stat '''
    card = models.ForeignKey('Card', related_name='cardstats', on_delete=models.CASCADE)
    stat = models.ForeignKey('Stat', on_delete=models.CASCADE)
    value = models.CharField(max_length=5)

class Card(models.Model):
    ''' A Card is a non-physical game piece, a rule abstraction '''
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    _class = models.ForeignKey('Class', related_name='cards', on_delete=models.CASCADE, blank=True, null=True)
    _type = models.ForeignKey('Type', related_name='cards', on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword, related_name='cards', blank=True)
    release_notes = models.ManyToManyField(Releasenote, related_name='cards', blank=True)
    subtypes = models.ManyToManyField(Subtype, related_name='cards', blank=True)
    supertypes = models.ManyToManyField(Supertype, related_name='cards', blank=True)
    talent = models.ForeignKey('Talent', related_name='cards', on_delete=models.CASCADE, blank=True, null=True)
    bloc = models.ForeignKey('Bloc', related_name='cards', on_delete=models.CASCADE)
    is_banned_cc = models.BooleanField(default=False)
    is_banned_blitz = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique card')
        ]

    def __str__(self):
        return self.name

class Format(models.Model):
    ''' A game of Flesh and Blood is played in a specific format that determines card legality (Blitz, Classic Constructed...) '''
    name = models.CharField(max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique format')
        ]

class Banlist(models.Model):
    ''' The makers of the game release a banlist periodically. Cards on this list cannot be played in some formats '''
    card = models.ForeignKey('Card', related_name='banned', on_delete=models.CASCADE)
    isBannedInClassicConstructed = models.BooleanField(default=True)
    isBannedInBlitz = models.BooleanField(default=True)
    isBannedInCommoner = models.BooleanField(default=True)
    isBannedInUltimatePitFight = models.BooleanField(default=True)

    def __str__(self):
        return self.card.name

class Deck(models.Model):
    ''' Players make Decks to compete against eachother '''
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField(max_length=5000)
    format = models.ForeignKey('Format', on_delete=models.CASCADE, null=True)

class DeckCard(models.Model):
    ''' Join table for cards in decks '''
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    in_sideboard = models.PositiveSmallIntegerField()

class Copy(models.Model):
    ''' A Copy is a Printing in a user's Collection. It covers the amount owned, wanted and to trade '''
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    printing = models.ForeignKey('Printing', on_delete=models.CASCADE)
    amount_owned = models.PositiveSmallIntegerField()
    amount_wanted = models.PositiveSmallIntegerField()
    amount_trading = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "copies"

class User(AbstractUser):
    ''' A User is probably what you think it is '''
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