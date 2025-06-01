

def tri_selection(tab):

    for i in range(len(tab)):       # on le fait pour chaque valeur a partir de la position 0

        indexe_minimum = i

        for j in range(i+1, len(tab)):      # pour chaque position supérieur,                
            
            if tab[j] < tab[indexe_minimum]: # on vérifie s'il y a une val inf a la val actuelle 
                indexe_minimum = j           # et on prend sa position comme la position minimum

        tab[i], tab[indexe_minimum] = tab[indexe_minimum], tab[i] # ensuite on change les valeurs
    return tab