from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

from jadidlar.models import Jadid


User = get_user_model()


class Asarlar(models.Model):
    title = models.TextField(verbose_name='nomi', blank=True, null=True)
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE, related_name='asarlar', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    count = models.BigIntegerField(null=True, blank=True, default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    turkiston_muxtoriyati = models.BooleanField(default=False, verbose_name='Turkiston muxtoriyati')
    tadqiqotlar = models.BooleanField(default=False, verbose_name='Tadqiqotlar')
    til_va_imlo = models.BooleanField(default=False, verbose_name='Til va imlo')
    likes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='liked_asarlar', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Asar'
        verbose_name_plural = 'Asarlar'


class AsarlarFile(models.Model):
    asarlar = models.ForeignKey(Asarlar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/asarlar')

    def __str__(self):
        return self.file.url


class Maqolalar(models.Model):
    title = models.TextField(verbose_name='nomi', blank=True, null=True)
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE,  related_name='maqolalar', blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/maqolalar', verbose_name='fayl', blank=True, null=True)
    count = models.BigIntegerField(null=True, blank=True, default=0)
    create = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana', blank=True, null=True)
    update = models.DateTimeField(auto_now=True, verbose_name='o`zgartirilgan sana', blank=True, null=True)
    turkiston_muxtoriyati = models.BooleanField(default=False, verbose_name='Turkiston muxtoriyati')
    tadqiqotlar = models.BooleanField(default=False, verbose_name='Tadqiqotlar')
    til_va_imlo = models.BooleanField(default=False, verbose_name='Til va imlo')

    Tarix = 'Tarix'
    Siyosat = 'Siyosat'
    Iqtisod = 'Iqtisod'
    Madaniyat_va_sanat = 'Madaniyat_va_sanat'
    Ijtimoiy_masalalar_va_din = 'Ijtimoiy_masalalar_va_din'
    Adabiyot = 'Adabiyot'
    Talim_Tarbiya = 'Talim_Tarbiya'
    Boshqa_masalalar = 'Boshqa_masalalar'
    Bibliografik_korsatkich = 'Bibliografik_korsatkich'

    TYPE_CHOICE = (
        (Tarix, 'Tarix'),
        (Siyosat, 'Siyosat'),
        (Iqtisod, 'Iqtisod'),
        (Madaniyat_va_sanat, 'Madaniyat_va_sanat'),
        (Ijtimoiy_masalalar_va_din, 'Ijtimoiy_masalalar_va_din'),
        (Adabiyot, 'Adabiyot'),
        (Talim_Tarbiya, 'Talim_Tarbiya'),
        (Boshqa_masalalar, 'Boshqa_masalalar'),
        (Bibliografik_korsatkich, 'Bibliografik_korsatkich'),
    )
    type = models.CharField(max_length=30, choices=TYPE_CHOICE, verbose_name='matbuotlar', blank=True, null=True)
    likes = models.IntegerField(default=0, blank=True, null=True)
    users = models.ManyToManyField(User, related_name='liked_maqolalar')

    def __str__(self):
        return self.title or ''

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class MaqolalarFile(models.Model):
    maqolalar = models.ForeignKey(Maqolalar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/maqolalar')

    def __str__(self):
        return self.file.url


class Tadqiqotlar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi', blank=True, null=True)
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE, related_name='tadqiqotlar', blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/tadqiqotlar')
    count = models.BigIntegerField(null=True, blank=True, default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    Turkiston_muxtoriyati = 'Turkiston_muxtoriyati'
    Tadqiqotlar = 'Tadqiqotlar'
    Til_va_imlo = 'Til_va_imlo'
    TYPE_CHOICE = (
        (Turkiston_muxtoriyati, 'Turkiston_muxtoriyati'),
        (Tadqiqotlar, 'Tadqiqotlar'),
        (Til_va_imlo, 'Til_va_imlo'),
    )
    type = models.CharField(max_length=25, choices=TYPE_CHOICE, verbose_name='turi', default=Turkiston_muxtoriyati, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tadqiqot'
        verbose_name_plural = 'Tadqiqotlar'


class TadqiqotlarFile(models.Model):
    tadqiqotlar = models.ForeignKey(Tadqiqotlar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/tadqiqotlar')

    def __str__(self):
        return self.file.url


class Sherlar(models.Model):
    title = models.TextField(verbose_name='nomi', blank=True, null=True)
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE, related_name='sherlar', blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/sherlar')
    count = models.BigIntegerField(null=True, blank=True, default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    Turkiston_muxtoriyati = 'Turkiston_muxtoriyati'
    # Tadqiqotlar = 'Tadqiqotlar'
    # Til_va_imlo = 'Til va imlo'
    TYPE_CHOICE = (
        (Turkiston_muxtoriyati, 'Turkiston_muxtoriyati'),
        # (Tadqiqotlar, 'Tadqiqotlar'),
        # (Til_va_imlo, 'Til va imlo'),
    )
    type = models.CharField(max_length=25, choices=TYPE_CHOICE, verbose_name='turi', default=Turkiston_muxtoriyati, blank=True, null=True)
    likes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='liked_sherlar', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sher'
        verbose_name_plural = 'Sherlar'


class SherlarFile(models.Model):
    sherlar = models.ForeignKey(Sherlar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/sherlar')

    def __str__(self):
        return self.file.url


class Hotiralar(models.Model):
    title = models.TextField(verbose_name='nomi', blank=True, null=True)
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE, related_name='hotiralar', blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/hotiralar', verbose_name='fayl')
    count = models.BigIntegerField(null=True, blank=True, default=0)
    create = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')
    update = models.DateTimeField(auto_now=True, verbose_name='o`zgartirilgan sana')
    Turkiston_muxtoriyati = 'Turkiston_muxtoriyati'
    Tadqiqotlar = 'Tadqiqotlar'
    # Til_va_imlo = 'Til va imlo'
    TYPE_CHOICE = (
        (Turkiston_muxtoriyati, 'Turkiston_muxtoriyati'),
        (Tadqiqotlar, 'Tadqiqotlar'),
        # (Til_va_imlo, 'Til_va_imlo'),
    )
    type = models.CharField(max_length=25, choices=TYPE_CHOICE, verbose_name='turi', default=Turkiston_muxtoriyati, blank=True, null=True)
    likes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='liked_hotiralar', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hotira'
        verbose_name_plural = 'Hotiralar'


class HotiralarFile(models.Model):
    hotiralar = models.ForeignKey(Hotiralar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/hotiralar')
    count = models.BigIntegerField(null=True, blank=True, default=0)


    def __str__(self):
        return self.file.url


# class Hikmatlar(models.Model):
#     text = RichTextField(verbose_name='hikmatli soz')
#     create = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')
#     update = models.DateTimeField(auto_now=True, verbose_name='o`zgartirilgan sana')
#
#     class Meta:
#         verbose_name = 'Hikmat'
#         verbose_name_plural = 'Hikmatlar'
#
#     def __str__(self):
#         return self.text


class Arxiv_hujjatlar(models.Model):
    ARXIV = 'ARXIV'
    SKANER = 'SKANER'
    TYPE_CHOICE = (
        (ARXIV, 'ARXIV'),
        (SKANER, 'SKANER'),
    )

    title = models.TextField(verbose_name='nomi', blank=True, null=True)
    type = models.CharField(max_length=6, choices=TYPE_CHOICE, verbose_name='turi', default=ARXIV, blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/arxiv_hujjatlar', verbose_name='fayl')
    count = models.BigIntegerField(null=True, blank=True, default=0)
    likes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='liked_arxiv_hujjatlar', blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Arxiv hujjat'
        verbose_name_plural = 'Arxiv hujjatlar'


class Arxiv_hujjatlarFile(models.Model):
    arxiv_hujjatlar = models.ForeignKey(Arxiv_hujjatlar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/arxiv_hujjatlar')


    def __str__(self):
        return self.file.url


class Dissertatsiya(models.Model):
    title = models.TextField(verbose_name='nomi', blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField(upload_to='files/dissertatsiya', verbose_name='fayl', blank=True, null=True)
    count = models.BigIntegerField(null=True, blank=True, default=0)
    create = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')
    update = models.DateTimeField(auto_now=True, verbose_name='o`zgartirilgan sana')
    likes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name='liked_dissertatsiya', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Dissertatsiya'
        verbose_name_plural = 'Dissertatsiyalar'


class DissertatsiyaFile(models.Model):
    dissertatsiya = models.ForeignKey(Dissertatsiya, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/dissertatsiya')

    def __str__(self):
        return self.file.url


