from django.contrib import admin
from django.utils.html import format_html
from tadbirlar.models import Kanferensiyalar, KanferensiyalarImage, SeminarlarImage, Seminarlar, YangiliklarImage, \
    Yangiliklar


class KanferensiyalarImageInline(admin.TabularInline):
    model = KanferensiyalarImage
    fields = ('image',)
    max_num = 10
    min_num = 1
    can_delete = False
    show_change_link = True
    show_add_button = True
    verbose_name = 'Rasm'
    verbose_name_plural = 'Rasmlar'
    list_display = ('image',)
    ordering = ('image',)
    extra = 0


@admin.register(Kanferensiyalar)
class KanferensiyalarAdmin(admin.ModelAdmin):
    inlines = [KanferensiyalarImageInline]
    list_display = ('title', 'display_admin_photo', 'created_at', 'updated_at',)
    fields = ('title_uz', 'title_ru', 'title_en', 'text_uz', 'text_ru', 'text_en', 'image',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 25
    list_max_show_all = 100
    save_as = False
    save_as_continue = True
    save_on_top = False
    readonly_fields = ('display_admin_photo', 'display_images', 'created_at', 'updated_at',)

    def display_admin_photo(self, obj):
        return format_html('<img src="{0}" width="100" height="100"  />'.format(obj.image.url))

    display_admin_photo.short_description = 'Rasm'
    display_admin_photo.allow_tags = True

    def display_images(self, obj):
        images = obj.kanferensiya_images.all()  # Related name ni moslashtiring
        return format_html(''.join(
            '<img src="{0}" width="100" height="100" style="margin-right: 10px;"  />'.format(img.image.url) for img in
            images))

    display_images.short_description = 'Images'
    display_images.allow_tags = True

    def logo_image(self, obj):
        return format_html('<img src="{0}" width="100" height="100" />'.format(obj.logo_image.url))

    logo_image.short_description = 'Rasm'
    logo_image.allow_tags = True


class SeminarlarImageInline(admin.TabularInline):
    model = SeminarlarImage
    fields = ('image',)
    max_num = 10
    min_num = 1
    can_delete = False
    show_change_link = True
    show_add_button = True
    verbose_name = 'Rasm'
    verbose_name_plural = 'Rasmlar'
    list_display = ('image',)
    ordering = ('image',)
    extra = 0


@admin.register(Seminarlar)
class SeminarlarAdmin(admin.ModelAdmin):
    inlines = [SeminarlarImageInline]
    list_display = ('title', 'display_admin_photo', 'created_at', 'updated_at',)
    fields = ('title_uz', 'title_ru', 'title_en', 'text_uz', 'text_ru', 'text_en', 'image',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 25
    list_max_show_all = 100
    save_as = False
    save_as_continue = True
    save_on_top = False
    readonly_fields = ('display_admin_photo', 'display_images', 'created_at', 'updated_at',)

    def display_admin_photo(self, obj):
        return format_html('<img src="{0}" width="100" height="100"  />'.format(obj.image.url))

    display_admin_photo.short_description = 'Rasm'
    display_admin_photo.allow_tags = True

    def display_images(self, obj):
        images = obj.seminar_images.all()  # Adjust the related name accordingly
        return format_html(''.join(
            '<img src="{0}" width="100" height="100" style="margin-right: 10px;"  />'.format(img.image.url) for img in
            images))

    display_images.short_description = 'Images'
    display_images.allow_tags = True

    def logo_image(self, obj):
        return format_html('<img src="{0}" width="100" height="100" />'.format(obj.logo_image.url))

    logo_image.short_description = 'Rasm'
    logo_image.allow_tags = True


class YangiliklarImageInline(admin.TabularInline):
    model = YangiliklarImage
    fields = ('image',)
    max_num = 10
    min_num = 1
    can_delete = False
    show_change_link = True
    show_add_button = True
    verbose_name = 'Rasm'
    verbose_name_plural = 'Rasmlar'
    list_display = ('image',)
    ordering = ('image',)
    extra = 0


@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    inlines = [YangiliklarImageInline]
    list_display = ('title', 'display_admin_photo', 'created_at', 'updated_at',)
    fields = ('title_uz', 'title_ru', 'title_en', 'text_uz', 'text_ru', 'text_en', 'link', 'image',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 25
    list_max_show_all = 100
    save_as = False
    save_as_continue = True
    save_on_top = False
    readonly_fields = ('display_admin_photo', 'display_images', 'created_at', 'updated_at',)

    def display_admin_photo(self, obj):
        return format_html('<img src="{0}" width="100" height="100"  />'.format(obj.image.url))

    display_admin_photo.short_description = 'Rasm'
    display_admin_photo.allow_tags = True

    def display_images(self, obj):
        images = obj.yangilik_images.all()  # Adjust the related name accordingly
        return format_html(''.join(
            '<img src="{0}" width="100" height="100" style="margin-right: 10px;"  />'.format(img.image.url) for img in
            images))

    display_images.short_description = 'Images'
    display_images.allow_tags = True

    def logo_image(self, obj):
        return format_html('<img src="{0}" width="100" height="100" />'.format(obj.logo_image.url))

    logo_image.short_description = 'Rasm'
    logo_image.allow_tags = True
