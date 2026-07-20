# ==========================================================
# CALCULATRICE SIMPLE EN PYTHON
# ==========================================================

# CONSTANTES D'AFFICHAGE
SEPARATEUR = "=" * 40
LIGNE = "-" * 40


# ==========================================================
# OPERATIONS DISPONIBLES
# ==========================================================

OPERATIONS = {
    "+": lambda a, b: a + b,   # Addition
    "-": lambda a, b: a - b,   # Soustraction
    "*": lambda a, b: a * b,   # Multiplication
    "/": lambda a, b: a / b,   # Division
    "^": lambda a, b: a ** b   # Puissance
}


# ==========================================================
# 1. FONCTION DE GESTION DES ENTREES
# ==========================================================

def gerer_entrees():
    """
    Demande et valide les informations saisies
    par l'utilisateur.
    """

    # Affichage des opérations
    print()
    print(LIGNE)
    print("\tOPERATIONS DISPONIBLES")
    print(LIGNE)
    print("+  Addition")
    print("-  Soustraction")
    print("*  Multiplication")
    print("/  Division")
    print("^  Puissance")
    print(LIGNE)

    # Choix de l'opérateur
    while True:
        operateur = input("Choisissez une opération : ").strip()

        if operateur in OPERATIONS:
            break

        print("Opérateur invalide.")

    # Saisie du premier nombre
    while True:
        try:
            nombre1 = float(input("Premier nombre : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Saisie du deuxième nombre
    while True:
        try:
            nombre2 = float(input("Deuxième nombre : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    return nombre1, nombre2, operateur



# ==========================================================
# 2. FONCTION DE CALCUL
# ==========================================================

def calculer(nombre1, nombre2, operateur):
    """
    Effectue l'opération choisie.
    """

    if operateur == "/" and nombre2 == 0:
        return "Impossible de diviser par zéro."

    fonction = OPERATIONS[operateur]

    resultat = fonction(nombre1, nombre2)

    return resultat



# ==========================================================
# 3. FONCTION PRINCIPALE DE LA CALCULATRICE
# ==========================================================

def calculatrice():

    print()
    print(SEPARATEUR)
    print("\t\tCALCULATRICE")
    print(SEPARATEUR)


    while True:

        # Récupération des données utilisateur
        nombre1, nombre2, operateur = gerer_entrees()

        # Calcul
        resultat = calculer(nombre1, nombre2, operateur)


        # Affichage du résultat
        print(LIGNE)

        if isinstance(resultat, str):
            print(resultat)
        else:
            print("Résultat :", nombre1, operateur, nombre2, "=", resultat)

        print(LIGNE)


        # Continuer ou arrêter
        while True:
            reponse = input(
                "\nVoulez-vous effectuer un autre calcul ? (O/N) : "
            ).strip().upper()

            if reponse in ("O", "N"):
                break

            print("Réponse invalide.")

        if reponse == "N":
            print("\nMerci d'avoir utilisé notre calculatrice.")
            break



# ==========================================================
# LANCEMENT DU PROGRAMME
# ==========================================================

calculatrice()