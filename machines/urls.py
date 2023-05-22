from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.accueil, name='Accueil'),
    path('', views.historique, name='Historique'),
    path('', views.comite, name='Comité'),
    path('', views.orchestre, name='Orchestre'),
    path('', views.adressesUtiles, name='Adresses Utiles'),
    path('', views.liensSocietes, name='Liens vers diverses sociétés'),
    path('', views.repertoire, name='Le répertoire annuel mis en place'),
    path('', views.agenda, name="Agenda des prestations de l'année"),
    path('', views.pratique, name="Informations pratiques"),
    path('', views.bibliotheque, name="Bibliothèque des oeuvres musicales en notre possession"),
    path('', views.medias, name="Quelques photos de notre fanfare"),
    path('', views.gestionBiblio, name="Gestion de la bibliothèque"),
    path('login', views.login, name="Login")
]
