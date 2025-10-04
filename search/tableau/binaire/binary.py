

def recherche_binaire(tab, cible):
    debut, fin = 0, len(tab) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] == cible:
            return milieu
        elif tab[milieu] < cible:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1
