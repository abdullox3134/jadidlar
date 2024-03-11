from django.db import models
from django.utils.safestring import mark_safe


class Ishtirokchilar(models.Model):
    fullname = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, verbose_name='Lavozimi', blank=True, null=True)
    image = models.ImageField(upload_to='image')
    order = models.IntegerField(default=100, blank=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Ishtirokchi'
        verbose_name_plural = 'Ishtirokchilar'


class IshtirokchilarImage(models.Model):
    ishtirokchilar = models.ForeignKey(Ishtirokchilar, on_delete=models.CASCADE,
                                       related_name='ishtirokchi_images')
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.image.url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
