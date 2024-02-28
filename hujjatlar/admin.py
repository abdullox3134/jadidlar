from django.contrib import admin
from hujjatlar.models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Arxiv_hujjatlar, \
    Dissertatsiya, AsarlarFile, MaqolalarFile, TadqiqotlarFile, SherlarFile, HotiralarFile, Arxiv_hujjatlarFile, \
    DissertatsiyaFile


class AsarlarFileInline(admin.TabularInline):
    model = AsarlarFile


@admin.register(Asarlar)
class AsarlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'jadid',)
    inlines = [AsarlarFileInline]
    fields = ('title_uz', 'title_ru', 'title_en', 'jadid', 'image', 'file', 'turkiston_muxtoriyati', 'tadqiqotlar',
              'til_va_imlo',
              'count')
    readonly_fields = ('count',)


class MaqolalarFileInline(admin.TabularInline):
    model = MaqolalarFile


@admin.register(Maqolalar)
class MaqolalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'type',)
    inlines = [MaqolalarFileInline]
    fields = ('title_uz', 'title_ru', 'title_en', 'jadid', 'image', 'file', 'turkiston_muxtoriyati', 'tadqiqotlar',
              'til_va_imlo',
              'type', 'count',)
    readonly_fields = ('count',)


class TadqiqotlarFileInline(admin.TabularInline):
    model = TadqiqotlarFile


@admin.register(Tadqiqotlar)
class TadqiqotlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'jadid', 'type',)
    inlines = [TadqiqotlarFileInline]
    fields = ('title_uz', 'title_ru', 'title_en', 'jadid', 'image', 'file', 'type', 'count',)
    readonly_fields = ('count',)


class SherlarFileInline(admin.TabularInline):
    model = SherlarFile


@admin.register(Sherlar)
class SherlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'jadid', 'type',)
    inlines = [SherlarFileInline]
    fields = ('title_uz', 'title_ru', 'title_en', 'jadid', 'image', 'file', 'type', 'count',)
    readonly_fields = ('count',)


class HotiralarFileInline(admin.TabularInline):
    model = HotiralarFile


@admin.register(Hotiralar)
class HotiralarAdmin(admin.ModelAdmin):
    list_display = ('title', 'jadid', 'type',)
    inlines = [HotiralarFileInline]
    fields = ('title_uz', 'title_ru', 'title_en', 'jadid', 'image', 'file', 'type', 'count',)
    readonly_fields = ('count',)


class Arxiv_hujjatlarFileInline(admin.TabularInline):
    model = Arxiv_hujjatlarFile


@admin.register(Arxiv_hujjatlar)
class Arxiv_hujjatlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'type',)
    inlines = [Arxiv_hujjatlarFileInline]
    fields = ('title_uz', 'title_ru', 'title_en', 'image', 'file', 'type', 'count',)
    readonly_fields = ('count',)


class DissertatsiyaFileInline(admin.TabularInline):
    model = DissertatsiyaFile


@admin.register(Dissertatsiya)
class DissertatsiyaAdmin(admin.ModelAdmin):
    inlines = [DissertatsiyaFileInline]
    fields = ('title_uz', 'title_ru', 'title_en', 'image', 'file', 'count',)
    readonly_fields = ('count',)
