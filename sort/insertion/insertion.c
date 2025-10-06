
/*
Tri insertion en language C

Utilisation:
    - compiler (linux): gcc insertion.c -o i.c
    - executer: ./i.c
*/

#include <stdio.h>

// Fonction pour trier
void tri_insertion(int tab[], int n) {
    int valeur, i, j;

    for (i = 1; i < n; i++)
    {
        valeur = tab[i];
        j = i - 1;

        while (j>=0, valeur < tab[j])
        {
            tab[j+1] = tab[j];
            j--;
        }

        tab[j+1] = valeur;
    }
    
}

void afficher_tableau(int tab[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", tab[i]);
    }
    printf("\n");
}

int main() {
    int tab[] = {64, 25, 12, 22, 11};
    int n = sizeof(tab) / sizeof(tab[0]);

    printf("Tableau avant le tri :\n");
    afficher_tableau(tab, n);

    tri_insertion(tab, n);

    printf("Tableau après le tri par insertion :\n");
    afficher_tableau(tab, n);

    return 0;
}
