function date(id) {
    date = new Date;
    annee = date.getFullYear();

    moi = date.getMonth();
    mois = new Array('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre');

    j = date.getDate();
    jour = date.getDay();
    jours = new Array('Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi');

    resultat = jours[jour] + ' ' + j + ' ' + mois[moi] + ' ' + annee;
    document.getElementById(id).innerHTML = resultat;
    return true;
}