from django.contrib import admin
from .models import PerfilUsuario, Filme, Critica, Comentario, Avaliacao, FilmeFavorito, Categoria, FilmeCategoria, Tag, FilmeTag, Visita, RelatorioFilme

admin.site.register(PerfilUsuario)
admin.site.register(Filme)
admin.site.register(Critica)
admin.site.register(Comentario)
admin.site.register(Avaliacao)
admin.site.register(FilmeFavorito)
admin.site.register(Categoria)
admin.site.register(FilmeCategoria)
admin.site.register(Tag)
admin.site.register(FilmeTag)
admin.site.register(Visita)
admin.site.register(RelatorioFilme)