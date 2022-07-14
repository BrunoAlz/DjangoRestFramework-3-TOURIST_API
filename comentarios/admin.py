from distutils.errors import CompileError
from django.contrib import admin

from comentarios.models import Comentario


admin.site.register(Comentario)