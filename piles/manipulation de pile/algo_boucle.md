ALGORITHME Deplacer_Piles
VARIABLES
    P1, P2, P3 : piles d’entiers
    x : entier
DEBUT
    P2 ← vide
    P3 ← vide

    // Étape 1 : dépiler P1 et distribuer
    TANT QUE P1 n’est pas vide FAIRE
        x ← Depiler(P1)
        SI (x MOD 2 = 0) ALORS
            Empiler(P3, x)
        SINON
            Empiler(P2, x)
        FINSI
    FIN TANT QUE

    // Étape 2 : transférer pairs de P3 dans P2
    TANT QUE P3 n’est pas vide FAIRE
        x ← Depiler(P3)
        Empiler(P2, x)
    FIN TANT QUE
FIN
