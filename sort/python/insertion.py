

def tri_insertion(tableau):

    for i in range(1, len(tableau)):        # on le fait pour chaque ligne du tableau

        cle = tableau[i]                    # a chaque position, on prend la valeur correspondante
        j = i - 1                           

        while(i <= 0, cle < tableau[j]):    # pour chaque valeur des positions inférieur a la position
            tableau[j +1] = tableau[j]      # de la valeur actuelle, si elle est inférieur a l'une d'entre
            j -= 1                          # elles, on décale cette valeur de sa posistion a la position supérieur
        
        tableau[j + 1] = cle                # a la fin, on met la valeur a la place obtenue
    
    return tableau
