## PROCEDURE pile_vide(P)

### DEBUT
    Si sommet(P) < 1 ALORS
        RETOURNER vrai
    SINON 
        RETOURNER faux
    FIN SI
### FIN PROCEDURE

---

## PROCEDURE pile_pleine(P, MAX)

### DEBUT
    Si sommet(P) = MAX ALORS
        RETOURNER vrai
    SINON 
        RETOURNER faux
    FIN SI
### FIN PROCEDURE

---

## PROCEDURE Empiler(VAR P: pile, X: type_c)

### DEBUT
    Si pile_pleine(P, max) ALORS
        ECRIRE("Impossible la pile est pleine")
    SINON
        sommet(P) <- sommet(P) + 1
        P[sommet(P)] <- X
    FIN SI
### FIN PROCEDURE

--- 

### PROCEDURE Dépiler(VAR P: pile, X: type_c)

### DEBUT
    Si pile_vide(P) ALORS
        ECRIRE("Impossible, Pile vide")
    SINON
        X <- P(sommet(P)) 
        sommet(P) <- sommet(P) − 1
        retourner X
    FIN SI
### FIN PROCEDURE

---

# ALGORITHME Deplacer_Piles

## VARIABLES
    P1, P2, P3 : piles d’entiers
    x : entier
### DEBUT
    P2 ← vide
    P3 ← vide

#### Étape 1 : dépiler P1 et distribuer

    TANT QUE Non pile_vide(P1) FAIRE
        x ← Depiler(P1)
        SI (x MOD 2 = 0) `ALORS`
            Empiler(P3, x)
        SINON
            Empiler(P2, x)
        FINSI
    FIN TANT QUE

#### Étape 2 : transférer pairs de P3 dans P2

    TANT QUE Non pile_vide(P3) FAIRE
        x ← Depiler(P3)
        Empiler(P2, x)
    FIN TANT QUE
### FIN
