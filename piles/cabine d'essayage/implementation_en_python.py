from collections import deque # Mieux pour simuler une file (performance)

# --- 1. Structures de Données ---
NB_CABINES = 3
CABINES = [-1] * NB_CABINES  # Vecteur/Tableau: -1 = Libre
ATTENTE = deque()             # File: collection.deque
VETEMENTS = {}                # Dictionnaire: Clé ID_Client -> Valeur Pile (list)
ID_CLIENT_GLOBAL = 0

# --- 2. Fonctions de Gestion (traduction du pseudocode) ---

def nouveau_client(vetements_liste):
    """Ajoute un client à la file et initialise sa pile de vêtements."""
    global ID_CLIENT_GLOBAL
    client_id = ID_CLIENT_GLOBAL
    
    # 1. Empiler les vêtements (LIFO)
    pile_vetements = []
    for vetement in vetements_liste:
        pile_vetements.append(vetement) # Empiler (push)
        
    VETEMENTS[client_id] = pile_vetements
    ATTENTE.append(client_id) # Enfiler (enqueue)
    
    print(f"-> Client {client_id} arrive. File d'attente : {len(ATTENTE)}.")
    ID_CLIENT_GLOBAL += 1

def attribuer_cabines():
    """Attribue les cabines libres aux clients en attente (FIFO)."""
    for i in range(NB_CABINES):
        if CABINES[i] == -1 and ATTENTE:
            client_id = ATTENTE.popleft()  # Défiler (dequeue)
            CABINES[i] = client_id
            
            nb_vetements = len(VETEMENTS[client_id])
            print(f"✅ Cabine {i} attribuée à Client {client_id}.")
            print(f"   Client {client_id} entre avec une pile de {nb_vetements} vêtements.")

def essayer_vetement(cabine_index):
    """Fait essayer un vêtement au client dans la cabine (utilise la Pile)."""
    client_id = CABINES[cabine_index]
    if client_id != -1:
        pile_client = VETEMENTS[client_id]
        if pile_client:
            vetement = pile_client.pop() # Dépiler (pop)
            print(f"👚 Client {client_id} (Cabine {cabine_index}) essaie : {vetement}. (Reste: {len(pile_client)})")
        else:
            print(f"🎉 Client {client_id} a fini d'essayer ses vêtements.")
    else:
        print(f"Cabine {cabine_index} est libre.")

def liberer_cabine(cabine_index):
    """Libère la cabine et réinitialise son état."""
    client_id = CABINES[cabine_index]
    CABINES[cabine_index] = -1
    print(f"🚪 Client {client_id} sort de la Cabine {cabine_index}. La cabine est libre.")
    
# --- 3. SCÉNARIO DE SIMULATION ---

print("--- DÉBUT DE LA JOURNÉE ---")

# 1. ARRIVÉES
nouveau_client(["Jupe", "Robe", "Chemise"]) # C0
nouveau_client(["Pantalon", "Veste"])      # C1
nouveau_client(["Écharpe", "Bonnet"])      # C2
nouveau_client(["Chaussures"])             # C3 doit attendre

print("\n--- ATTRIBUTION INITIALE ---")
attribuer_cabines()
# C0, C1, C2 entrent dans les cabines 0, 1, 2. C3 est en attente.

print("\n--- PHASE D'ESSAYAGE ---")
# C0 essaie le dernier vêtement empilé (Chemise)
essayer_vetement(0) 
# C1 essaie le dernier vêtement empilé (Veste)
essayer_vetement(1)

print("\n--- LIBÉRATION ET ROTATION ---")
# C0 termine et libère la Cabine 0
liberer_cabine(0) 

# Le système réattribue
attribuer_cabines()
# C3, en tête de la file, prend la Cabine 0

print("\n--- SUITE DE L'ESSAYAGE ---")
essayer_vetement(0) # C3 essaie Chaussures
essayer_vetement(0) # C3 a fini de sa pile

print("\n--- ÉTAT FINAL ---")
print(f"Cabines : {CABINES}")
print(f"File d'attente : {list(ATTENTE)}")
print("--- FIN ---")