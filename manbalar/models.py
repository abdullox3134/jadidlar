from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

User = get_user_model()


def validate_audio_extension(value):
    allowed_extensions = ['.mp3', '.wav', '.ogg',]  # Qo'shimcha audio formatlarni qo'shing
    if not any(value.name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError(_('Faqat MP3, WAV yoki OGG formatlari qo\'llaniladi.'))


class Audiolar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    audio = models.FileField(upload_to='audios/', validators=[validate_audio_extension])
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='liked_audiolar', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audiolar'


class AudioFile(models.Model):
    audiolarmodel = models.ForeignKey(Audiolar, on_delete=models.CASCADE, related_name='audio_files')
    audio = models.FileField(upload_to='audios/', validators=[validate_audio_extension])

    def __str__(self):
        return self.audio.url


def validate_video_extension(value):
    allowed_extensions = ['.mp4', '.avi', '.mkv']  # Qo'shimcha video formatlarni qo'shing
    if not any(value.name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError(_('Faqat MP4, AVI yoki MKV formatlari qo\'llaniladi.'))


class Videolar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi', blank=True, null=True)
    video = models.FileField(upload_to='videos/', validators=[validate_video_extension], blank=True, null=True)
    link = models.URLField(max_length=200, verbose_name='link', blank=True, null=True)
    file = models.FileField(upload_to='files/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videolar'


class VideoFile(models.Model):
    videolarmodel = models.ForeignKey(Videolar, on_delete=models.CASCADE, related_name='video_files')
    video = models.FileField(upload_to='video/', validators=[validate_video_extension])

    def clean(self):
        super().clean()
        content_type = self.video.file.content_type
        allowed_content_types = ['video/mp4', 'video/x-msvideo',
                                 'video/x-matroska',]  # Qo'shimcha video formatlarni qo'shing
        if content_type not in allowed_content_types:
            raise ValidationError(_('Faqat MP4, AVI yoki MKV formatlari qo\'llaniladi.'))


def validate_image_extension(value):
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Qo'shimcha rasm formatlarni qo'shing
    if not any(value.name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError(_('Faqat JPEG, JPG, PNG yoki GIF formatlari qo\'llaniladi.'))


class Rasmlar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi', blank=True, null=True)
    image = models.ImageField(upload_to='images/', validators=[validate_image_extension])
    # file = models.FileField(upload_to='files/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='liked_rasmlar', blank=True)
    blog_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'


class RasmlarImage(models.Model):
    rasimlarmodel = models.ForeignKey(Rasmlar, on_delete=models.CASCADE,
                                      related_name='rasimlar')
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.image.url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True

    def clean(self):
        super().clean()
        if self.image:
            content_type = self.image.file.content_type
            allowed_content_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif']
            if content_type not in allowed_content_types:
                raise ValidationError(_('Faqat JPEG, JPG, PNG yoki GIF formatlari qo\'llaniladi.'))

    def save(self, *args, **kwargs):
        # 5 ta rasm qo'shishni tekshirish
        if not self.pk and Rasmlar.objects.count() >= 100:
            raise ValidationError(_('Faqat 100 ta rasm qo\'shishingiz mumkin.'))
        super().save(*args, **kwargs)
