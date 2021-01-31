from django.contrib import admin
from .models import *

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display= ('title', 'description','cat')



admin.site.register(Category)
admin.site.register(Image,ImageAdmin)
