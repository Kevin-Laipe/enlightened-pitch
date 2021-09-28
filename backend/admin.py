from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Bloc, Card, CardStat, Class, Finish, Printing, Rarity, Set, Keyword, Subtype, Supertype, Talent, Releasenote, Stat, Type, User, Copy, Deck, DeckCard

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class KeywordAdmin(admin.ModelAdmin):
    model = Keyword
    list_display = ('name', 'description', 'id', )
    search_fields = ('name', )
    ordering = ('name', )

class SubtypeAdmin(admin.ModelAdmin):
    model = Subtype
    list_display = ('name', 'id',)
    search_fields = ('name', )
    ordering = ('name', )

class ClassAdmin(admin.ModelAdmin):
    model = Class
    list_display = ('name', 'id',)
    search_fields = ('name', )
    ordering = ('name', )

class SupertypeAdmin(admin.ModelAdmin):
    model = Supertype
    list_display = ('name', 'id',)
    search_fields = ('name', )
    ordering = ('name', )

class TalentAdmin(admin.ModelAdmin):
    model = Talent
    list_display = ('name', 'id',)
    search_fields = ('name', )
    ordering = ('name', )

class BlocAdmin(admin.ModelAdmin):
    model = Bloc
    list_display = ('name', 'description', 'id',)
    search_fields = ('name', )
    ordering = ('name', )

class StatAdmin(admin.ModelAdmin):
    model = Bloc
    list_display = ('name', 'id',)
    search_fields = ('name', )
    ordering = ('name', )

class TypeAdmin(admin.ModelAdmin):
    model = Bloc
    list_display = ('name', 'id',)
    search_fields = ('name', )
    ordering = ('name', )

class CardAdmin(admin.ModelAdmin):
    model = Card
    list_display = ('name', '_type', 'id',)
    list_filter = ('bloc', '_class', '_type', 'talent')
    search_fields = ('name', )
    ordering = ('id', )
    fieldsets = (
        (None, {
            'fields': ('name', 'text', ('_class', 'talent', '_type'), ('is_banned_cc', 'is_banned_blitz'), )
        }),
        ('Stats', {
            'fields': ('stats', 'keywords', 'subtypes', 'supertypes', )
        }),
        (None, {
            'fields': ('release_notes', )
        }),
        ('Bloc', {
            'fields': ('bloc', )
        })
    )

class PrintingAdmin(admin.ModelAdmin):
    model = Printing
    list_display = ('uid', 'card', 'rarity', 'finish', 'set', )
    list_filter = ('set', 'finish', 'rarity', )
    search_fields = ('card__name', 'uid', )
    ordering = ('uid', )

# class ReleasenoteAdmin(admin.ModelAdmin):
#     model = Releasenote
#     list_display = ('card', 'id', )
#     search_fields = ('card', )
#     ordering = ('id', )

# class CardReleasenoteAdmin(admin.ModelAdmin):
#     model = CardReleasenote
#     list_display = ('card', 'id',)
#     search_fields = ('card', )
#     ordering = ('card', )

class RarityAdmin(admin.ModelAdmin):
    model = Rarity
    list_display = ('name', 'tag', 'id', )
    search_fields = ('name', )
    ordering = ('id', )

class FinishAdmin(admin.ModelAdmin):
    model = Finish
    list_display = ('name', 'id', )
    search_fields = ('name', )
    ordering = ('name', )

class CardStatAdmin(admin.ModelAdmin):
    model = CardStat
    list_display = ('cards', 'stat', 'value', )
    search_fields = ('cards', )
    ordering = ('cards', )

admin.site.register(Card, CardAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Printing, PrintingAdmin)
admin.site.register(Set)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Subtype, SubtypeAdmin)
admin.site.register(Supertype, SupertypeAdmin)
admin.site.register(Talent, TalentAdmin)
admin.site.register(Bloc, BlocAdmin)
admin.site.register(Releasenote)
admin.site.register(Stat, StatAdmin)
# admin.site.register(CardReleasenote, CardReleasenoteAdmin)
admin.site.register(CardStat, CardStatAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Copy)
admin.site.register(Deck)
admin.site.register(DeckCard)
admin.site.register(Finish, FinishAdmin)
admin.site.register(Rarity, RarityAdmin)
admin.site.register(Type, TypeAdmin)