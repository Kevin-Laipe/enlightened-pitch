from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Card, Printing, Set, Keyword, Subtype, Talent, Releasenote, Stat, CardKeyword, CardSubtype, CardTalent, CardReleasenote, CardStat, User, Copy, Deck, DeckCard

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
    list_display = ('name', 'description', )
    search_fields = ('name', )
    ordering = ('name', )

admin.site.register(Card)
admin.site.register(Printing)
admin.site.register(Set)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Subtype)
admin.site.register(Talent)
admin.site.register(Releasenote)
admin.site.register(Stat)
admin.site.register(CardKeyword)
admin.site.register(CardSubtype)
admin.site.register(CardTalent)
admin.site.register(CardReleasenote)
admin.site.register(CardStat)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Copy)
admin.site.register(Deck)
admin.site.register(DeckCard)