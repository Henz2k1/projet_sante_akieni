# ==========================================================
# VDECLARATION DES ARIABLES D'ACCUMULATEURS
# ==========================================================
total_suspects = 0
total_confirmes = 0
total_deces = 0
total_actifs = 0

zones_vertes = 0
zones_jaunes = 0
zones_oranges = 0
zones_rouges = 0

nb_districts = 9

# ==========================================================
# BOUCLE SUR LES DISTRICTS
# ==========================================================
for i in range(1, nb_districts + 1):
    print('--- District', i, '---')

    nom_district = input('Nom du district : ')
    suspects = int(input('Cas suspects : '))
    confirmes = int(input('Cas confirmes : '))
    deces = int(input('Deces : '))

# ======================================================
# CALCUL DES CAS ACTIFS
# ======================================================
    cas_actifs = int(confirmes - deces)

# ======================================================
# CALCUL DE LA LETALITE
# ======================================================
    if confirmes > 0:
        letalite = (deces / confirmes) * 100
    else:
        letalite = 0

# ======================================================
# CLASSIFICATION DU NIVEAU D'ALERTE
# ======================================================
    if confirmes >= 10:
        alerte = 'ROUGE'
        zones_rouges = zones_rouges + 1

    elif confirmes >= 5:
        alerte = 'ORANGE'
        zones_oranges = zones_oranges + 1

    elif confirmes >= 2:
        alerte = 'JAUNE'
        zones_jaunes = zones_jaunes + 1

    else:
        alerte = 'VERT'
        zones_vertes = zones_vertes + 1

# ======================================================
# MISE A JOUR DES CUMULATIFS
# ======================================================
    total_suspects = total_suspects + suspects
    total_confirmes = total_confirmes + confirmes
    total_deces = total_deces + deces
    total_actifs = total_actifs + cas_actifs

# ======================================================
# AFFICHAGE PAR DISTRICT
# ======================================================
    print(' Alerte :', alerte)
    print(' Actifs :', cas_actifs)
    print(' Letalite :', round(letalite, 1), '%')
    print()
    
    
# ==========================================================
# RAPPORT NATIONAL
# ==========================================================
separateurs = "=" * 50

print(separateurs)
print(' RAPPORT NATIONAL MPOX 2025 ')
print(separateurs)

print(f'''Districts analyses : {nb_districts}
Total suspects : {total_suspects}
Total confirmes : {total_confirmes}
Total deces : {total_deces}
Total cas actifs : {total_actifs}''')

print(f'''Zones VERTES :', {zones_vertes}
Zones JAUNES : {zones_jaunes}
Zones ORANGES : {zones_oranges}
Zones ROUGES : {zones_rouges}''')

print(separateurs)