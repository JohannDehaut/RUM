from django.shortcuts import render


def webpage1(request):
    return render(request, 'home.html')


def webpage2(request):
    return render(request, 'historique.html')


def webpage3(request):
    return render(request, 'asbl.html')


def webpage4(request):
    return render(request, 'membresOrchestre.html')


def webpage5(request):
    return render(request, 'adressesUtiles.html')


def webpage6(request):
    return render(request, 'liensSocietes.html')


def webpage7(request):
    return render(request, 'repertoire.html')


def webpage8(request):
    return render(request, 'agenda.html')


def webpage9(request):
    return render(request, 'pratique.html')


def webpage10(request):
    return render(request, 'bibliotheque.html')


def webpage11(request):
    return render(request, 'media.html')


def webpage12(request):
    return render(request, 'gestionBiblio.html')


def webpage13(request):
    return render(request, 'login.html')
