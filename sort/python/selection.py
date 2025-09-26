

def tri_selection(tab):

    for i in range(len(tab)):      

        indexe_minimum = i

        for j in range(i+1, len(tab)):                   
            
            if tab[j] < tab[indexe_minimum]:
                indexe_minimum = j          

        tab[i], tab[indexe_minimum] = tab[indexe_minimum], tab[i] 
    return tab