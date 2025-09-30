'''FONCTION EstPair(x : entier) : booléen
DEBUT
    RETOURNER (x MOD 2 = 0)
FIN

PROCÉDURE Deplacer_Piles(VAR P1, P2 : pile)
VARIABLES
    P3 : pile   // pour stocker les pairs
    x : entier
DEBUT
    P2 ← vide
    P3 ← vide

    // Étape 1 : vider P1 en séparant pairs et impairs
    TANT QUE NON PileVide(P1) FAIRE
        x ← Depiler(P1)
        SI EstPair(x) ALORS
            Empiler(P3, x)      // pairs vont dans P3
        SINON
            Empiler(P2, x)      // impairs vont dans P2
        FINSI
    FIN TANT QUE

    // Étape 2 : transférer pairs de P3 vers P2
    TANT QUE NON PileVide(P3) FAIRE
        x ← Depiler(P3)
        Empiler(P2, x)
    FIN TANT QUE
FIN
'''