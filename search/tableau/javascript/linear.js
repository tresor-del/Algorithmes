function rechercheLineaire(tab, cible) {
    for (let i = 0; i < tab.length; i++) {
        if (tab[i] === cible) {
            return i;
        }
    }
    return -1;
}
