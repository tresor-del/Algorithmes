"""
Algorithme de recherche binaire utilisant la methode DIVISER POUR MIEUX REGNER
"""

def recherche_binaire_iterative(tab, cible):
    """
    Recherche binaire itérative
    
    """
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



def recherche_binaire_recursive(tab, debut, fin, cible):

    if debut > fin:
        return -1

    milieu = (debut + fin) // 2
    
    if tab[milieu] == cible:
        return milieu
    
    elif tab[milieu] < cible:
        
        # rechercher dans la moitié droite
        return recherche_binaire_recursive(tab, milieu + 1, fin, cible)
    
    
    else:
        # rechercher dans la moitié  gauche
        return recherche_binaire_recursive(tab, debut, milieu - 1, cible)
    
    

# Exemples

if __name__ == "__main__":
    
    tableau = [1, 2, 3, 4, 5, 6]
    
    print("Recherche binaire iterative: ", recherche_binaire_iterative(tableau, 4))
    print("Recherce binaire recursive: ", recherche_binaire_recursive(tableau, 0, len(tableau) - 1, 4))