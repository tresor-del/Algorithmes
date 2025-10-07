"""
Algorithme Fusion mais avec des sentinelles
"""

def tri_fusion(tab, debut, fin):
    
    if debut < fin:
        millieu = (debut + fin) // 2
        
        tri_fusion(tab, debut, millieu)
        tri_fusion(tab, millieu + 1, fin)
        fusion(tab, debut, millieu, fin)


def fusion(tab, debut, milieu, fin):
    
    # calculer la taille des sous tableaux
    n1 = milieu - debut + 1
    n2 = fin - milieu
    
    # on crée les sous tableaux: left, right
    l = [0] * (n1 + 1)
    r = [0] * (n2 + 1)
    
    # on copie les élements du tableau dans les deux tableaux
    for i in range(n1):
        l[i] = tab[debut + i]
    for j in range(n2):
        r[j] = tab[milieu + 1 + j]
        
    # ajouter les sentinelles
    l[n1] = float("inf")
    r[n2] = float("inf")

    # fusionner l et r dans un tab
    i = j = 0
    for k in range(debut, fin + 1):
        if l[i] <= r[j]:
            tab[k] = l[i]
            i += 1
        else:
            tab[k] = r[j]
            j += 1
    

# Exemple
tableau = [5, 2, 9, 1, 7]
tri_fusion(tableau, 0, len(tableau) -1)
print(tableau)
    

