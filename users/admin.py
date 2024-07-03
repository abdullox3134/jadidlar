from django.contrib import admin
from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'full_name', 'email')


admin.site.register(CustomUser, CustomUserAdmin)
