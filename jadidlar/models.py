from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe


class Jadid(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    die_day = models.DateField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/jadid')
    order = models.IntegerField(default=1000)
    bio = RichTextField(blank=True, null=True)
    blog_views = models.IntegerField(default=0)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Jadid'
        verbose_name_plural = 'Jadidlar'


class JadidImage(models.Model):
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE,
                              related_name='jadid_images')
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.image.url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
