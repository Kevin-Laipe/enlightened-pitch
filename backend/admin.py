from django.contrib import admin

from .models import Card, Printing, Set, Keyword, Subtype, Talent, Releasenote, Stat, CardKeyword, CardSubtype, CardTalent, CardReleasenote, CardStat, User, Copy, Deck, DeckCard

admin.site.register(Card)
admin.site.register(Printing)
admin.site.register(Set)
admin.site.register(Keyword)
admin.site.register(Subtype)
admin.site.register(Talent)
admin.site.register(Releasenote)
admin.site.register(Stat)
admin.site.register(CardKeyword)
admin.site.register(CardSubtype)
admin.site.register(CardTalent)
admin.site.register(CardReleasenote)
admin.site.register(CardStat)
admin.site.register(User)
admin.site.register(Copy)
admin.site.register(Deck)
admin.site.register(DeckCard)