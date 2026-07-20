import random

# =============================================================================
# CONFIGURATION DYNAMIQUE DES SEPARATEURS
# =============================================================================
LARGEUR = 41
SEPARATEUR_EGAL = "=" * LARGEUR
SEPARATEUR_TIRET = "-" * LARGEUR


# =============================================================================
# FONCTION : JOUER UNE MANCHE
# =============================================================================
def jouer_manche():
    """Gère le choix des joueurs et renvoie le résultat de la manche."""
    choix_possibles = ["pierre", "feuille", "ciseaux"]
    
    choix_j = input("Votre choix (pierre, feuille, ciseaux) : ").lower().strip()
    if choix_j not in choix_possibles:
        print("Erreur : Choix invalide. Manche annulee.")
        return "invalide"
        
    choix_ordinateur = random.choice(choix_possibles)
    print(f"L'ordinateur a choisi : {choix_ordinateur}")
    
    if choix_j == choix_ordinateur:
        print("Egalite sur cette manche !")
        return "egalite"
    elif (choix_j == "pierre" and choix_ordinateur == "ciseaux") or \
         (choix_j == "feuille" and choix_ordinateur == "pierre") or \
         (choix_j == "ciseaux" and choix_ordinateur == "feuille"):
        print("Succes : Vous gagnez cette manche !")
        return "joueur"
    else:
        print("Dommage : L'ordinateur gagne cette manche.")
        return "ordi"


# =============================================================================
# FONCTION : DEROULEMENT D'UNE PARTIE
# =============================================================================
def executer_partie():
    """Boucle sur 3 manches et affiche le score final."""
    score_joueur, score_ordinateur, manche = 0, 0, 1
    print(f"\n{SEPARATEUR_EGAL}\n     DEBUT D'UNE PARTIE EN 3 MANCHES\n{SEPARATEUR_EGAL}")
    
    while manche <= 3:
        print(f"\n--- MANCHE {manche} / 3 ---")
        resultat = jouer_manche()
        
        if resultat == "invalide":
            continue
        elif resultat == "joueur":
            score_joueur += 1
        elif resultat == "ordi":
            score_ordinateur += 1
            
        manche += 1

    print(f"\n{SEPARATEUR_EGAL}\n Score final -> Vous : {score_joueur} | Ordi : {score_ordinateur}")
    if score_joueur > score_ordinateur:
        print("Felicitations ! Vous gagnez la partie !")
    elif score_ordinateur > score_joueur:
        print("L'ordinateur gagne la partie.")
    else:
        print("Match nul global !")
    print(SEPARATEUR_EGAL)


# =============================================================================
# PROGRAMME PRINCIPAL
# =============================================================================
print(SEPARATEUR_EGAL)
print("\tBIENVENUE AU PIERRE FEUILLE CISEAUX")
print(SEPARATEUR_EGAL)

while True:
    executer_partie()
    
    print(f"\n{SEPARATEUR_TIRET}")
    if input("Rejouer une partie ? (oui/non) : ").lower().strip() != "oui":
        print(f"\n{SEPARATEUR_EGAL}\n       Merci d'avoir joue ! Au revoir.\n{SEPARATEUR_EGAL}")
        break