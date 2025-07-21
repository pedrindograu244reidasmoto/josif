from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre_pesquisa, name='sobre'),
    path('metodologia/', views.metodologia, name='metodologia'),
    path('resultados/', views.resultados, name='resultados'),
    path('estrategias/', views.estrategias, name='estrategias'),
    path('contato/', views.contato, name='contato'),
]

