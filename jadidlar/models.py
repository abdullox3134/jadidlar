from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

User = get_user_model()


class Jadid(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    die_day = models.DateField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/jadid')
    order = models.IntegerField(default=1000)
    bio = RichTextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked_jadids', blank=True)

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


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     like_count = models.IntegerField(default=0)  # "Like" soni
#
#
# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)


class PostLikes(models.Model):
    likeusers = models.ManyToManyField(User)
    likepost = models.ForeignKey(Jadid,on_delete=models.CASCADE,null=True,related_name='likepost')