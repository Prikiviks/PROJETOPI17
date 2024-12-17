from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)
    
    def __str__(self):
        return self.usuario.username

# core/models.py
from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    sinopse = models.TextField()
    data_lancamento = models.DateField()
    duracao = models.DurationField()
    genero = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    url_trailer = models.URLField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.titulo

class Critica(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    texto_critica = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Critica de {self.usuario} sobre {self.filme}'

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    critica = models.ForeignKey(Critica, on_delete=models.CASCADE, related_name='comentarios')
    texto_comentario = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comentário de {self.usuario.username} sobre a crítica {self.critica.titulo}"

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    nota = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Avaliação de {self.usuario.username} sobre {self.filme.titulo}"

class FilmeFavorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    data_adicao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario.username} favoritou {self.filme.titulo}"

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome

class FilmeCategoria(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.filme.titulo} - {self.categoria.nome}"

class Tag(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome

class FilmeTag(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.filme.titulo} - {self.tag.nome}"

class Visita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    data_visita = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario.username} visitou {self.filme.titulo}"

class RelatorioFilme(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_relatorio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Relatório de {self.usuario.username} sobre {self.filme.titulo}"