from django.contrib import admin

from tanlovlar.models import Tanlovlar


class TanlovlarAdmin(admin.ModelAdmin):
    list_display = ('Telegram', 'Instagram', 'Facebook', 'Email', 'Telefon',)
    list_display_links = ('Telegram', 'Instagram', 'Facebook', 'Email', 'Telefon',)
    list_per_page = 25


admin.site.register(Tanlovlar,  TanlovlarAdmin)