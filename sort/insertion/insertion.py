"""
Implémentation d'e l'Algorithme de tri par insertion en python 
"""

def tri_insertion(tableau):

    for i in range(1, len(tableau)):      

        cle = tableau[i]                  
        j = i - 1                           

        while(j >= 0 and cle < tableau[j]):  
            tableau[j +1] = tableau[j]     
            j -= 1                        

        tableau[j + 1] = cle              
    
    return tableau

# exemple 

if __name__ == "__main__":
    
    tableau = [5, 2, 4, 6, 1, 3]
    
    print(tri_insertion(tableau))
