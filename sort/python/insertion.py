

def tri_insertion(tableau):

    for i in range(1, len(tableau)):      

        cle = tableau[i]                  
        j = i - 1                           

        while(i <= 0, cle < tableau[j]):  
            tableau[j +1] = tableau[j]     
            j -= 1                        
        
        tableau[j + 1] = cle              
    
    return tableau
