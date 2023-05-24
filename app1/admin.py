from django.contrib import admin
from .models import contactModels
# Register your models here.


@admin.register(contactModels)
class userAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
