from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.safestring import mark_safe
User = get_user_model()


class Kanferensiyalar(models.Model):
    title = models.TextField(verbose_name='nomi', blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='liked_kanferensiyalar', blank=True)
    blog_views = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kanferensiya'
        verbose_name_plural = 'Kanferensiyalar'


class KanferensiyalarImage(models.Model):
    kanferensiya = models.ForeignKey(Kanferensiyalar, on_delete=models.CASCADE,
                                       related_name='kanferensiya_images')
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.image.url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True


class Seminarlar(models.Model):
    title = models.TextField(verbose_name='nomi', blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='liked_seminarlar', blank=True)
    blog_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Seminar'
        verbose_name_plural = 'Seminarlar'


class SeminarlarImage(models.Model):
    seminar = models.ForeignKey(Seminarlar, on_delete=models.CASCADE,
                                       related_name='seminar_images')
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.image.url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True


class Yangiliklar(models.Model):
    title = models.TextField(verbose_name='nomi', blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='image')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='liked_yangiliklar', blank=True)
    blog_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'


class YangiliklarImage(models.Model):
    yangilik = models.ForeignKey(Yangiliklar, on_delete=models.CASCADE,
                                       related_name='yangilik_images')
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.image.url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True

