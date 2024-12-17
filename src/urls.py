
from apps.core import views  # Importando as views da pasta core
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('filmes/', views.lista_filmes, name='lista_filmes'),
    path('filmes/<int:filme_id>/', views.detalhe_filme, name='detalhe_filme'),
    path('filmes/adicionar/', views.adicionar_filme, name='adicionar_filme'),
    path('filmes/editar/<int:filme_id>/', views.editar_filme, name='editar_filme'),
    path('filmes/excluir/<int:filme_id>/', views.excluir_filme, name='excluir_filme'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Adicionando a URL para logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)