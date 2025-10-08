### _devoir d'algo_ 
--Nous avons 3 cabines d'essayage (ressource limitée).

--Chaque client est identifié par un numéro (Client 1, Client 2, etc.).

--Chaque client a une pile de vêtements à essayer.

Le problème est une simulation de la gestion des clients et des vêtements dans un magasin disposant d'un nombre limité de cabines d'essayage.En résumé, l'exercice consiste à écrire un programme qui gère le flux des clients (via une file) vers les cabines disponibles (via un vecteur) tout en simulant des actions spécifiques liées aux articles ou aux opérations (via une pile).

### Pseudo code Algorithme principale 

PROCEDURE GererCabines()

    // Initialisation
    N_CABINES = 3
    CABINES = [ -1, -1, -1 ] // Toutes les cabines sont libres
    ATTENTE = CreerFileVide()
    VETEMENTS = CreerDictionnaireVide()
    ID_CLIENT_GLOBAL = 0

    // Exemple de scénario :
    // 1. Des clients arrivent
    NouveauClient(ATTENTE, VETEMENTS, ID_CLIENT_GLOBAL, ["Jupe", "Robe", "Chemise"])
    ID_CLIENT_GLOBAL = ID_CLIENT_GLOBAL + 1
    NouveauClient(ATTENTE, VETEMENTS, ID_CLIENT_GLOBAL, ["Pantalon", "Veste"])
    ID_CLIENT_GLOBAL = ID_CLIENT_GLOBAL + 1
    NouveauClient(ATTENTE, VETEMENTS, ID_CLIENT_GLOBAL, ["Echarpe", "Bonnet"])
    ID_CLIENT_GLOBAL = ID_CLIENT_GLOBAL + 1
    NouveauClient(ATTENTE, VETEMENTS, ID_CLIENT_GLOBAL, ["Chaussures"]) // 4ème client : devra attendre

    // 2. Attribution des cabines
    AttribuerCabines(CABINES, ATTENTE, VETEMENTS)
    // Client 0, 1, 2 entrent. Client 3 attend.

    // 3. Un client essaie un vêtement (utilise sa Pile)
    // Client 0 essaie un vêtement
    EssayerVetement(CABINES[0], VETEMENTS) 

    // 4. Un client a terminé
    LibererCabine(CABINES, ATTENTE, 0) // Cabine 0 se libère

    // 5. Un nouveau client prend la cabine libérée
    AttribuerCabines(CABINES, ATTENTE, VETEMENTS)
    // Client 3 entre dans la Cabine 0
    
FIN PROCEDURE

### pseudo code NouveauClient (Ajout à la File)

PROCEDURE NouveauClient(ref F_ATTENTE, ref D_VETEMENTS, ID, L_VETEMENTS)
    ENFILER(F_ATTENTE, ID)
    
    PILE_CLIENT = CreerPileVide()
    POUR chaque VETEMENT dans L_VETEMENTS FAIRE
        EMPILER(PILE_CLIENT, VETEMENT)
    FIN POUR
    
    // Stocker la pile de vêtements dans le dictionnaire, avec ID comme clé
    D_VETEMENTS[ID] = PILE_CLIENT
    AFFICHER("-> Client", ID, "arrive. File d'attente : ", TAILLE_FILE(F_ATTENTE))
FIN PROCEDURE

### pseudo code AttribuerCabines (Gestion du Vecteur et de la File)

PROCEDURE AttribuerCabines(ref T_CABINES, ref F_ATTENTE, D_VETEMENTS)
    POUR i DE 0 A TAILLE(T_CABINES) - 1 FAIRE
        SI T_CABINES[i] == -1 ET NON EST_FILE_VIDE(F_ATTENTE) ALORS
            ID_CLIENT = DEFILER(F_ATTENTE)
            T_CABINES[i] = ID_CLIENT // La cabine est occupée par ce client
            AFFICHER("Cabine", i, "attribuée à Client", ID_CLIENT)
            AFFICHER("Client", ID_CLIENT, "entre avec une pile de", TAILLE_PILE(D_VETEMENTS[ID_CLIENT]), "vêtements.")
        FIN SI
    FIN POUR
FIN PROCEDURE

### pseudo code EssayerVetement(utilisation de la pile)

PROCEDURE EssayerVetement(ID_CLIENT, ref D_VETEMENTS)
    SI ID_CLIENT != -1 ALORS
        PILE_CLIENT = D_VETEMENTS[ID_CLIENT]
        SI NON EST_PILE_VIDE(PILE_CLIENT) ALORS
            VETEMENT = DEPILER(PILE_CLIENT)
            AFFICHER("Client", ID_CLIENT, "essaie :", VETEMENT, "(Reste:", TAILLE_PILE(PILE_CLIENT), ")")
        SINON
            AFFICHER("Client", ID_CLIENT, "a fini d'essayer ses vêtements.")
        FIN SI
    FIN SI
FIN PROCEDURE
