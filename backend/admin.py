from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Bloc, Card, CardSupertype, Class, Printing, Set, Keyword, Subtype, Supertype, Talent, Releasenote, Stat, CardKeyword, CardSubtype, CardReleasenote, CardStat, Type, User, Copy, Deck, DeckCard

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

class CardSupertypeInline(admin.TabularInline):
    model = CardSupertype
    extra = 0

class CardSubtypeInline(admin.TabularInline):
    model = CardSubtype
    extra = 0

class CardStatInline(admin.TabularInline):
    model = CardStat
    extra = 0

class CardKeywordInline(admin.TabularInline):
    model = CardKeyword
    extra = 0

class CardAdmin(admin.ModelAdmin):
    model = Bloc
    list_display = ('name', '_type', 'id',)
    search_fields = ('name', )
    ordering = ('id', )
    fieldsets = (
        (None, {
            'fields': ('name', 'text', ('_class', 'talent', '_type'), )
        }),
        ('Restrictions', {
            'fields': ('is_banned_cc', 'is_banned_blitz', )
        }),
        ('Bloc', {
            'fields': ('bloc', )
        })
    )
    inlines = [
        CardStatInline,
        CardKeywordInline,
        CardSupertypeInline,
        CardSubtypeInline,
    ]

admin.site.register(Card, CardAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Printing)
admin.site.register(Set)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Subtype, SubtypeAdmin)
admin.site.register(Supertype, SupertypeAdmin)
admin.site.register(Talent, TalentAdmin)
admin.site.register(Bloc, BlocAdmin)
admin.site.register(Releasenote)
admin.site.register(Stat, StatAdmin)
admin.site.register(CardKeyword)
admin.site.register(CardSubtype)
admin.site.register(CardReleasenote)
admin.site.register(CardStat)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Copy)
admin.site.register(Deck)
admin.site.register(DeckCard)
admin.site.register(Type, TypeAdmin)