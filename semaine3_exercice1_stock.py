# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 1 : Classification Stocks Medicaments
# Utilise les notions de S2 (variables, types, operateurs, f-strings)
# + S3 (if/elif/else, conditions composees)
# ============================================================


# ==============================================================================
# VARIABLES MEDICAMENTS
# ==============================================================================

# Donnés réimportées depuis le fichier sante_variables.py
m1_nom            = 'Artemether-Lumefantrine'
m1_stock          = 3200
m1_seuil_rupture  = 2000
m1_cout_unitaire  = 3500.0   

m2_nom            = 'Amoxicilline 500mg'
m2_stock          = 950
m2_seuil_rupture  = 800
m2_cout_unitaire  = 850.0

m3_nom            = 'Paracetamol 500mg'
m3_stock          = 12400
m3_seuil_rupture  = 3000
m3_cout_unitaire  = 120.0

m4_nom            = 'SRO (sachets)'
m4_stock          = 4200
m4_seuil_rupture  = 5000
m4_cout_unitaire  = 125.0

m5_nom            = 'Vaccin DTP-HepB-Hib'
m5_stock          = 820
m5_seuil_rupture  = 1000
m5_cout_unitaire  = 8500.0


# ==============================================================================
# CLASSIFICATION DES MEDICAMENTS 
# ==============================================================================

# classification médicament 1 : Artemether-Lumefantrine 
if m1_stock <= m1_seuil_rupture:
    m1_statut  = 'RUPTURE CRITIQUE'
    m1_couleur = '[ROUGE]'
    m1_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m1_stock <= m1_seuil_rupture * 1.5:
    m1_statut  = 'ALERTE STOCK'
    m1_couleur = '[ORANGE]'
    m1_action  = 'Commande urgente a declencher sous 72h'
elif m1_stock <= m1_seuil_rupture * 2.0:
    m1_statut  = 'STOCK LIMITE'
    m1_couleur = '[JAUNE]'
    m1_action  = 'Surveillance renforcee-planifier commande'
else:
    m1_statut  = 'STOCK NORMAL'
    m1_couleur = '[VERT]'
    m1_action  = 'Situation normale — suivi standard'

# classification médicament2 : Amoxicilline 500mg 
if m2_stock <= m2_seuil_rupture:
    m2_statut  = 'RUPTURE CRITIQUE'
    m2_couleur = '[ROUGE]'
    m2_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m2_stock <= m2_seuil_rupture * 1.5:
    m2_statut  = 'ALERTE STOCK'
    m2_couleur = '[ORANGE]'
    m2_action  = 'Commande urgente a declencher sous 72h'
elif m2_stock <= m2_seuil_rupture * 2.0:
    m2_statut  = 'STOCK LIMITE'
    m2_couleur = '[JAUNE]'
    m2_action  = 'Surveillance renforcee-planifier commande'
else:
    m2_statut  = 'STOCK NORMAL'
    m2_couleur = '[VERT]'
    m2_action  = 'Situation normale — suivi standard'

# classification médicament 3 : Paracetamol 500mg 
if m3_stock <= m3_seuil_rupture:
    m3_statut  = 'RUPTURE CRITIQUE'
    m3_couleur = '[ROUGE]'
    m3_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m3_stock <= m3_seuil_rupture * 1.5:
    m3_statut  = 'ALERTE STOCK'
    m3_couleur = '[ORANGE]'
    m3_action  = 'Commande urgente a declencher sous 72h'
elif m3_stock <= m3_seuil_rupture * 2.0:
    m3_statut  = 'STOCK LIMITE'
    m3_couleur = '[JAUNE]'
    m3_action  = 'Surveillance renforcee-planifier commande'
else:
    m3_statut  = 'STOCK NORMAL'
    m3_couleur = '[VERT]'
    m3_action  = 'Situation normale — suivi standard'

# classification médicament 4 : SRO (sachets) 
if m4_stock <= m4_seuil_rupture:
    m4_statut  = 'RUPTURE CRITIQUE'
    m4_couleur = '[ROUGE]'
    m4_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m4_stock <= m4_seuil_rupture * 1.5:
    m4_statut  = 'ALERTE STOCK'
    m4_couleur = '[ORANGE]'
    m4_action  = 'Commande urgente a declencher sous 72h'
elif m4_stock <= m4_seuil_rupture * 2.0:
    m4_statut  = 'STOCK LIMITE'
    m4_couleur = '[JAUNE]'
    m4_action  = 'Surveillance renforcee-planifier commande'
else:
    m4_statut  = 'STOCK NORMAL'
    m4_couleur = '[VERT]'
    m4_action  = 'Situation normale — suivi standard'

# classification médicament 5 : Vaccin DTP-HepB-Hib 
if m5_stock <= m5_seuil_rupture:
    m5_statut  = 'RUPTURE CRITIQUE'
    m5_couleur = '[ROUGE]'
    m5_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m5_stock <= m5_seuil_rupture * 1.5:
    m5_statut  = 'ALERTE STOCK'
    m5_couleur = '[ORANGE]'
    m5_action  = 'Commande urgente a declencher sous 72h'
elif m5_stock <= m5_seuil_rupture * 2.0:
    m5_statut  = 'STOCK LIMITE'
    m5_couleur = '[JAUNE]'
    m5_action  = 'Surveillance renforcee-planifier commande'
else:
    m5_statut  = 'STOCK NORMAL'
    m5_couleur = '[VERT]'
    m5_action  = 'Situation normale — suivi standard'


# ==============================================================================
# COMPTAGE DES ALERTES 
# ==============================================================================

#initialisation des variables de comptage
nb_ruptures_critiques = 0
nb_alertes_stock      = 0
nb_stock_normaux = 0

# TODO : Utiliser des if pour incrementer les compteurs
# Exemple : 
# if m1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1
# print("s1",nb_ruptures_critiques)

name_med_critique = ""
name_med_alerte_stock = ""
name_med_stock_normaux = ""

# Comptage medicament 1
if m1_statut == 'RUPTURE CRITIQUE': 
    nb_ruptures_critiques += 1
    name_med_critique += m1_nom
if m1_statut == 'ALERTE STOCK':
    nb_alertes_stock += 1
    name_med_alerte_stock += m2_nom
if m1_statut == 'STOCK NORMAL':
    nb_stock_normaux = nb_stock_normaux + 1
    name_med_stock_normaux += m1_nom

# Comptage medicament 2
if m2_statut == 'RUPTURE CRITIQUE': 
    nb_ruptures_critiques += 1
    name_med_critique += m2_nom
# print("s2 critique",nb_ruptures_critiques)
if m2_statut == 'ALERTE STOCK': 
    nb_alertes_stock += 1
    name_med_alerte_stock += m2_nom
if m2_statut == 'STOCK NORMAL':
    nb_stock_normaux = nb_stock_normaux + 1
    name_med_stock_normaux += m2_nom

# Comptage medicament 3
if m3_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_critiques += 1
    name_med_critique += m3_nom
# print("s3 critique",nb_ruptures_critiques)
if m3_statut == 'ALERTE STOCK': 
    nb_alertes_stock += 1
    name_med_alerte_stock = m3_nom
if m3_statut == 'STOCK NORMAL':
    nb_stock_normaux = nb_stock_normaux + 1
    name_med_stock_normaux += m3_nom

# Comptage medicament 4
if m4_statut == 'RUPTURE CRITIQUE': 
    nb_ruptures_critiques += 1
    name_med_critique += m4_nom
# print("s4 critique",nb_ruptures_critiques)
if m4_statut == 'ALERTE STOCK': 
    nb_alertes_stock += 1
    name_med_alerte_stock = m4_nom
if m4_statut == 'STOCK NORMAL':
    nb_stock_normaux = nb_stock_normaux + 1
    name_med_stock_normaux += m4_nom

# Comptage medicament 5
if m5_statut == 'RUPTURE CRITIQUE': 
    nb_ruptures_critiques += 1
    name_med_critique += m5_nom
if m5_statut == 'ALERTE STOCK': 
    nb_alertes_stock += 1
    name_med_alerte_stock = m5_nom
if m5_statut == 'STOCK NORMAL':
    nb_stock_normaux = nb_stock_normaux + 1
    name_med_stock_normaux += m5_nom

# ==============================================================================
# AFFICHAGE DU RAPPORT 
# ==============================================================================

# S2 (reutilise) : f-strings structurees
# S3 (nouveau) : statuts et couleurs determines par les conditions

separateurs = "=" * 80

print(f'''{separateurs}
RAPPORT DE STOCK — PHARMACIE NATIONALE APPROVISIONNEMENT
Date : 15 janvier 2026')
{separateurs}''')

# Medicament 1
print(f'''{m1_couleur} {m1_nom}
Stock \t : {m1_stock} unites \t | Seuil rupture : {m1_seuil_rupture}
Statut \t : {m1_statut}
Action \t : {m1_action}
{separateurs}''')

# Medicament 2
print(f'''{m2_couleur} {m2_nom}
Stock \t : {m2_stock} unites \t | Seuil rupture : {m2_seuil_rupture}
Statut \t : {m2_statut}
Action \t : {m2_action}
{separateurs}''')

# Medicament 3
print(f'''{m3_couleur} {m3_nom}
Stock \t : {m3_stock} unites  | Seuil rupture : {m3_seuil_rupture}
Statut \t : {m3_statut}
Action \t : {m3_action}
{separateurs}''')

# Medicament 4
print(f'''{m4_couleur} {m4_nom}
Stock \t : {m4_stock} unites \t | Seuil rupture : {m4_seuil_rupture}
Statut \t : {m4_statut}
Action \t : {m4_action}
{separateurs}''')

# Medicament 5
print(f''''{m5_couleur} {m5_nom}
Stock \t : {m5_stock} unites \t | Seuil rupture : {m5_seuil_rupture}
Statut \t : {m5_statut}
Action \t : {m5_action}''')

# --- BILAN FINAL ---
print(f'''{separateurs})
BILAN STOCK — PNA CONGO
Ruptures critiques : {nb_ruptures_critiques} ({name_med_critique})
Alertes stock : {nb_alertes_stock} ({name_med_alerte_stock})
Stocks Normaux : {nb_stock_normaux} ({name_med_stock_normaux})''')

print(separateurs)

# Alerte prioritaire conditionnelle (uniquement s'il y a des ruptures critiques)
if nb_ruptures_critiques > 0:
    print(f'''ALERTE PRIORITAIRE : {nb_ruptures_critiques} medicaments en RUPTURE CRITIQUE
Transmettre immediatement au Dr. MOUKALA (PNA)
{separateurs}''')