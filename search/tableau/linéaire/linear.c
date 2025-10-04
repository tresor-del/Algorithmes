int recherche_lineaire(int tab[], int taille, int cible) {
    for (int i = 0; i < taille; i++) {
        if (tab[i] == cible) {
            return i;
        }
    }
    return -1;
}
