# gado/admin.py

from django.contrib import admin
from .models import *

admin.site.register(Animal)
admin.site.register(RegistroSanitario)
admin.site.register(RegistroAlimentacao)
admin.site.register(RegistroReprodutivo)
