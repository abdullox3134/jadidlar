from django.db import models


class Tanlovlar(models.Model):
    Telegram = models.CharField(max_length=255, verbose_name='Telegram', blank=True, null=True)
    Instagram = models.CharField(max_length=255, verbose_name='Instagram', blank=True, null=True)
    Facebook = models.CharField(max_length=255, verbose_name='Facebook', blank=True, null=True)
    Email = models.CharField(max_length=255, verbose_name='Email', blank=True, null=True)
    Telefon = models.CharField(max_length=255, verbose_name='Telefon', blank=True, null=True)

    class Meta:
        verbose_name = "Tanlov"
        verbose_name_plural = "Tanlovlar"
