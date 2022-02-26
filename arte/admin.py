from django.contrib import admin
from .models import Categoria, Comentario, Tematica, Tags, Arte

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tematica)
admin.site.register(Tags)
admin.site.register(Arte)
admin.site.register(Comentario)