from django.contrib import admin

from .models import *

admin.site.register(Manga)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Genre)
