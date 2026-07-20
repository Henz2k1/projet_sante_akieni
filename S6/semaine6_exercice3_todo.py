# =============================================================================
# CONFIGURATION DYNAMIQUE DES SEPARATEURS
# =============================================================================
LARGEUR = 50
SEPARATEUR_EGAL = "=" * LARGEUR
SEPARATEUR_TIRET = "-" * LARGEUR


# =============================================================================
# AFFICHER LES TACHES 
# =============================================================================
def afficher_taches(liste_taches):
    """Affiche toutes les tâches de la liste."""
    print(f"\n{SEPARATEUR_EGAL}")
    print("           VOS TACHES EN COURS           ")
    print(SEPARATEUR_EGAL)
    
    if len(liste_taches) == 0:
        print("  Votre liste est vide ! Veuillez ajouter des taches")
    else:
        for index, tache in enumerate(liste_taches, 1):
            print(f"  {index}. {tache}")
            
    print(SEPARATEUR_TIRET)


# =============================================================================
# AJOUTER UNE TACHE
# =============================================================================
def ajouter_tache(liste_taches):
    """Demande une nouvelle tâche à l'utilisateur et l'ajoute à la liste."""
    print(f"\n{SEPARATEUR_TIRET}")
    nouvelle_tache = input(" -> Entrez la tache a ajouter : ")
    print(SEPARATEUR_TIRET)
    
    if nouvelle_tache.strip() != "":
        liste_taches.append(nouvelle_tache)
        print(f" Success : Tache '{nouvelle_tache}' ajoutee avec succes !")
    else:
        print(" Erreur : La tache ne peut pas etre vide.")
    print(SEPARATEUR_TIRET)


# =============================================================================
# SUPPRIMER UNE TACHE
# =============================================================================
def supprimer_tache(liste_taches):
    """Affiche les tâches et demande à l'utilisateur d'en choisir une à supprimer."""
    print(f"\n{SEPARATEUR_EGAL}")
    print("         SUPPRESSION D'UNE TACHE         ")
    print(SEPARATEUR_EGAL)
    
    if len(liste_taches) == 0:
        print("  Aucune tache a supprimer, la liste est deja vide.")
        print(SEPARATEUR_TIRET)
        return

    for index, tache in enumerate(liste_taches, 1):
        print(f"  {index}. {tache}")
    print(SEPARATEUR_TIRET)
        
    try:
        numero = int(input(" -> Entrez le numero de la tache terminee : "))
        index_a_supprimer = numero - 1 
        print(SEPARATEUR_TIRET)
        
        if 0 <= index_a_supprimer < len(liste_taches):
            tache_retiree = liste_taches.pop(index_a_supprimer)
            print(f" Success : Tache '{tache_retiree}' supprimee. Beau travail !")
        else:
            print(" Erreur : Numero invalide, cette tache n'existe pas.")
    except ValueError:
        print(SEPARATEUR_TIRET)
        print(" Erreur : Veuillez entrer un nombre valide.")
    print(SEPARATEUR_TIRET)


# =============================================================================
# QUITTER LE PROGRAMME
# =============================================================================
def quitter_programme(liste_taches):
    """Affiche un message d'au revoir et quitte le programme."""
    print(f"\n{SEPARATEUR_EGAL}")
    print("       Au revoir et bonne journee !      ")
    print(SEPARATEUR_EGAL)
    exit()


# =============================================================================
# PROGRAMME PRINCIPAL
# =============================================================================
taches = []

# Stockage des fonctions 
actions = {
    "1": afficher_taches,
    "2": ajouter_tache,
    "3": supprimer_tache,
    "4": quitter_programme
}

print(SEPARATEUR_EGAL)
print("\tBIENVENUE DANS VOTRE TO-DO LIST")
print(SEPARATEUR_EGAL)

while True:
    print("\nMENU PRINCIPAL :")
    print("  [1] Afficher les taches")
    print("  [2] Ajouter une tache")
    print("  [3] Supprimer une tache terminee")
    print("  [4] Quitter du programme")
    
    choix = input("\n -> Entrez votre choix (1-4) : ")
    
    if choix in actions:
        fonction_selectionnee = actions[choix]
        fonction_selectionnee(taches)
    else:
        print(f"\n{SEPARATEUR_TIRET}")
        print(" Erreur : Choix invalide. Entrez un chiffre entre 1 et 4.")
        print(SEPARATEUR_TIRET)