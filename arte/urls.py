from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListarArte, name='listar_arte'),
    path('publicar/', views.PublicarArte, name='publicar_arte'),
    path('busca/', views.busca, name="busca"),
    path('carrinho/', views.AdicionarCarrinho, name="adicionar_carrinho"),
    path('detalhar/<slug>/', views.DetalharArte, name="detalhar"),
    path('minhasartes/detalhar/<slug>/', views.DetalharArte, name="detalhar"),
    path('busca/detalhar/<slug>/', views.DetalharArte, name="detalhar"),
]
