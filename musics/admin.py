# musics/admin.py
from django.contrib import admin
from .models import Music, Category, Track

class TrackInline(admin.TabularInline):
    model = Track
    extra = 1

class MusicAdmin(admin.ModelAdmin):
    inlines = [TrackInline]
    filter_horizontal = ('categories',)
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'slug':
            kwargs['help_text'] = 'Informe a URL para o produto. Ex: titulo-do-produto.'
        return super().formfield_for_dbfield(db_field, request, **kwargs)

admin.site.register(Music, MusicAdmin)
admin.site.register(Category)
