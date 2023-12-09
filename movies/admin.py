# movies/admin.py
from django import forms
from django.contrib import admin
from .models import Movie, Category

class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    
    RATING = [
        (0, 'Livre'),
        (10, 'Maiores de 10 anos'),
        (12, 'Maiores de 12 anos'),
        (14, 'Maiores de 14 anos'),
        (16, 'Maiores de 16 anos'),
        (18, 'Maiores de 18 anos')
    ]
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'slug':
            kwargs['help_text'] = 'Informe a URL para o produto. Ex: titulo-do-produto.'
        elif db_field.name == 'directors':
            kwargs['help_text'] = 'Separe os diretores por vírgulas.'
        elif db_field.name == 'running_time':
            kwargs['help_text'] = 'Informe a duração em minutos.'
        elif db_field.name == 'rating':
            kwargs['widget'] = forms.Select(choices=self.RATING)
            return db_field.formfield(**kwargs)
        return super().formfield_for_dbfield(db_field, request, **kwargs)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
