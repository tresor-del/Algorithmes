

function rechercheBinaire(tab, cible) {
    let debut = 0, fin = tab.length - 1;

    while (debut <= fin) {
        // diviser le tableau en deux parties
        let milieu = Math.floor((debut + fin) / 2);
        if (tab[milieu] === cible) return milieu;
        else if (tab[milieu] < cible) debut = milieu + 1;
        else fin = milieu - 1;
    }
    return -1;
}
