from django.shortcuts import render
from django.http import HttpResponse
import datetime


def accueil(request):
    return render(request, 'home')


def historique(request):
    return render(request, 'historique')


def comite(request):
    return render(request, 'asbl')


def orchestre(request):
    return render(request, 'orchestre')


def adressesUtiles(request):
    return render(request, 'adressesUtiles')


def liensSocietes(request):
    return render(request, 'liensSocietes')


def repertoire(request):
    return render(request, 'repertoire')


def agenda(request):
    return render(request, 'agenda')


def pratique(request):
    return render(request, 'pratique')


def bibliotheque(request):
    return render(request, 'bibliotheque')


def medias(request):
    return render(request, 'media')


def gestionBiblio(request):
    return render(request, 'gestionBiblio')


def date(request):
    current_datetime = datetime.datetime.now()
    html = current_datetime
    return HttpResponse(html)


def login(request):
    return render(request, 'login')



