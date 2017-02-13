from django.contrib import admin

from .models import ModelA, Image


class ImageInline(admin.TabularInline):
    model = Image
    insert_after = 'title'


class ModelAAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'description'
    )
    inlines = [
        ImageInline,
    ]
    change_form_template = 'admin/custom/change_form.html'

    class Media:
        css = {
            'all': (
                'css/admin.css',
            )
        }


admin.site.register(ModelA, ModelAAdmin)
