# ==========================================================
# CALCULATRICE SIMPLE EN PYTHON
# ==========================================================

# CCONSTANTES D'AFFCIHAGE  
SEPARATEUR = "=" * 40
LIGNE = "-" * 40

# ==========================================================
# OPÉRATIONS DISPONIBLES
# ==========================================================

# Chaque symbole est associé à une fonction lambda
OPERATIONS = {
    "+": lambda a, b: a + b,   # Addition
    "-": lambda a, b: a - b,   # Soustraction
    "*": lambda a, b: a * b,   # Multiplication
    "/": lambda a, b: a / b,   # Division
    "^": lambda a, b: a ** b   # Puissance
}

# ==========================================================
# FONCTIONS DE SAISIE
# ==========================================================

def saisir_nombre(message):
    """
    Demande un nombre à l'utilisateur jusqu'à ce qu'il
    saisisse une valeur valide.
    """
    while True:
        try:
            return float(input(message).strip())
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def saisir_operateur():
    """
    Affiche les opérations disponibles puis demande
    à l'utilisateur d'en choisir une.
    """
    
    print()
    print(LIGNE)
    print("\tOPÉRATIONS DISPONIBLES")
    print(LIGNE)
    print("+  Addition")
    print("-  Soustraction")
    print("*  Multiplication")
    print("/  Division")
    print("^  Puissance")
    print(LIGNE)

    while True:
        operateur = input("Choisissez une opération : ").strip()
        if operateur in OPERATIONS:
            return operateur
        print("Opérateur invalide.")


# ==========================================================
# FONCTION DE CALCUL
# ==========================================================

def effectuer_calcul(nombre1, nombre2, operateur):
    """
    Récupère la fonction correspondant à l'opérateur
    puis effectue le calcul.
    """
    fonction_operation = OPERATIONS[operateur]
    return fonction_operation(nombre1, nombre2)


# ==========================================================
# PROGRAMME PRINCIPAL
# ==========================================================

def calculatrice():
    
    print()
    print(SEPARATEUR)
    print("\t\tCALCULATRICE")
    print(SEPARATEUR)

    while True:

        # Choix de l'opération
        operateur = saisir_operateur()

        # Saisie des nombres
        nombre1 = saisir_nombre("Veuillez saisir le premier nombre  : ")
        nombre2 = saisir_nombre("Veuillez saisir le deuxième nombre : ")

        # Vérification de la division par zéro
        if operateur == "/" and nombre2 == 0:
            print("\nImpossible de diviser un nombre par zéro")
        else:
            try:
                resultat = effectuer_calcul(nombre1, nombre2, operateur)

                print(LIGNE)
                print("Résultat : {} {} {} = {}".format(nombre1, operateur, nombre2, resultat))
                print(LIGNE)

            except OverflowError:
                print("\nLe résultat est trop grand pour être calculé.")

        # Demande si l'utilisateur souhaite continuer
        while True:
            reponse = input("\nVoulez-vous effectuer un autre calcul ? (O/N) : ").strip().upper()

            if reponse in ("O", "N"):
                break
            print("Réponse invalide. Veuillez saisir O ou N.")

        if reponse == "N":
            print("\nMerci d'avoir utilisé notre calculatrice, A tres bientot")
            break


# ==========================================================
# LANCEMENT DU PROGRAMME
# ==========================================================

calculatrice()