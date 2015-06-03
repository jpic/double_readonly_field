from django.contrib import admin
from django import forms

from .models import YourModel


class YourForm(forms.ModelForm):
    relation = forms.ModelChoiceField(YourModel.objects.all())

    class Meta:
        exclude = tuple()
        model = YourModel


class YourModelAdmin(admin.ModelAdmin):
    form = YourForm

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['relation']
        return super(YourModelAdmin, self).get_readonly_fields(request, obj)
admin.site.register(YourModel, YourModelAdmin)
