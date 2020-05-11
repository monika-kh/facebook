from django.contrib import admin
from .models import Facebook
from django.contrib.admin import ModelAdmin, register

# Register your models here.


# admin.site.register(Facebook)


@register(Facebook)
class FacebookAdmin(ModelAdmin):
    list_display = ('name', 'first_name', 'last_name', 'hometown', 'location', 'birthdate',
                    'language', 'email')
