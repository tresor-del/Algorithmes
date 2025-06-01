

int recherche_binaire(int tab[], int taille, int cible) {
    int debut = 0, fin = taille - 1;
    while (debut <= fin) {
        int milieu = (debut + fin) / 2;
        if (tab[milieu] == cible)
            return milieu;
        else if (tab[milieu] < cible)
            debut = milieu + 1;
        else
            fin = milieu - 1;
    }
    return -1;
}
