from ckeditor.fields import RichTextField
from django.db import models


class Sahifalar(models.Model):
    title = models.CharField(max_length=255, verbose_name='Sahifa nomi', blank=True, null=True)
    text = RichTextField(verbose_name='Matn', blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/', verbose_name='Fayl', blank=True, null=True)
    count = models.BigIntegerField(null=True, blank=True, default=0)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    update = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sahifa'
        verbose_name_plural = 'Sahifalar'


class SahifalarFile(models.Model):
    sahifalar = models.ForeignKey(Sahifalar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/sahifalar')

    def __str__(self):
        return self.file.url

