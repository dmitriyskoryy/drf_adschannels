from django.contrib import admin

from django.forms import ModelForm, CharField
from .models import *



admin.site.register(Category)
admin.site.register(Author)
# admin.site.register(Adt)
admin.site.register(Respond)
admin.site.register(OneTimeCode)



class AdtAdminForm(ModelForm):
    text = CharField()
    class Meta:
        model = Adt  # Тут нужно указать название модели в которой будем использовать CKEditor
        fields = ('author', 'adtCategory', 'title', 'slug', 'text',)


@admin.register(Adt)
class AdtAdmin(admin.ModelAdmin):
    form = AdtAdminForm
