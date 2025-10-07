

def tri_selection(tab):

    for i in range(len(tab)):      

        index_minimum = i

        for j in range(i+1, len(tab)):                   
            
            if tab[j] < tab[index_minimum]:
                index_minimum = j          

        tab[i], tab[index_minimum] = tab[index_minimum], tab[i] 
    return tab