# ============================================================ 
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy 
# Ce fichier centralise toutes les constantes et variables metier 
# Il sera enrichi chaque semaine jusqu'a S24 
# ============================================================ 
# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ======== 
TAUX_EUR_FCFA = 655.957 
TAUX_USD_FCFA = 600.0 
SEUIL_OMS_DENSITE_MEDICALE = 2.3    

# medecins pour 1000 habitants 
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations 
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock 
DEPARTEMENTS_CONGO = [              # 12 departements officiels 
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala', 
    'Niari', 'Plateaux', 'Pool', 'Sangha' 
] 
 
# === SECTION B : VARIABLES DES 5 HOPITAUX =================== 

# ==========================================
# DECLARATION DES 5 HOPITAUX
# ==========================================

# Hopital 1 — CHU de Brazzaville 
h1_nom              = 'CHU de Brazzaville' 
h1_ville            = 'Brazzaville' 
h1_departement      = 'Brazzaville' 
h1_type             = 'CHU' 
h1_nb_lits          = 320 
h1_nb_lits_occupes  = 284 
h1_nb_medecins      = 47 
h1_nb_infirmiers    = 123 
h1_population_zone  = 1_800_000 

# Hopital 2 - Hopital General POINTE NOIRE  
h2_nom              = 'Hopital General Pointe-Noire' 
h2_ville            = 'Pointe-Noire' 
h2_departement      = 'Pointe-Noire' 
h2_type             = 'Hopital General' 
h2_nb_lits          = 220 
h2_nb_lits_occupes  = 175 
h2_nb_medecins      = 32 
h2_nb_infirmiers    = 85 
h2_population_zone  = 1_200_000 

# Hopital 3 -  Hopital de Dolisie
h3_nom              = 'Hopital de Dolisie' 
h3_ville            = 'Dolisie' 
h3_departement      = 'Niari' 
h3_type             = 'Hopital de reference' 
h3_nb_lits          = 110 
h3_nb_lits_occupes  = 65 
h3_nb_medecins      = 12 
h3_nb_infirmiers    = 42 
h3_population_zone  = 180_000 

# Hopital 4 - Hopital de district Owando  
h4_nom              = 'Hopital de district Owando' 
h4_ville            = 'Owando' 
h4_departement      = 'Cuvette' 
h4_type             = 'Hopital de district' 
h4_nb_lits          = 75 
h4_nb_lits_occupes  = 40 
h4_nb_medecins      = 6 
h4_nb_infirmiers    = 28 
h4_population_zone  = 90_000 

# Hopital 5 - Centre de sante de Impfondo 
h5_nom              = 'Centre de sante de Impfondo' 
h5_ville            = 'Impfondo' 
h5_departement      = 'Likouala' 
h5_type             = 'CSI' 
h5_nb_lits          = 30 
h5_nb_lits_occupes  = 18 
h5_nb_medecins      = 2 
h5_nb_infirmiers    = 14 
h5_population_zone  = 45_000


# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================ 
# TODO : Declarer les 5 medicaments essentiels 


# ==========================================
# DECLARATION DES 5 MEDICAMENTS ESSENTIELS
# ==========================================

# Médicament 1 : Artemether-lumefantrine (Antipaludique)
m1_nom            = 'Artemether-Lumefantrine'
m1_stock          = 3200
m1_seuil_rupture  = 2000
m1_cout_unitaire  = 3500.0   # FCFA

# Médicament 2 : Amoxicilline (Antibiotique)
m2_nom            = 'Amoxicilline 500mg'
m2_stock          = 950
m2_seuil_rupture  = 800
m2_cout_unitaire  = 850.0

# Médicament 3 : Paracétamol (Analgésique/Antipyrétique)
m3_nom            = 'Paracetamol 500mg'
m3_stock          = 12400
m3_seuil_rupture  = 3000
m3_cout_unitaire  = 120.0

# Médicament 4 : SRO (Sels de Réhydratation Orale)
m4_nom            = 'SRO (sachets)'
m4_stock          = 4200
m4_seuil_rupture  = 5000
m4_cout_unitaire  = 125.0

# Médicament 5 : Vaccin antipaludique
m5_nom            = 'Vaccin DTP-HepB-Hib'
m5_stock          = 820
m5_seuil_rupture  = 1000
m5_cout_unitaire  = 8500.0


# === SECTION D : CALCULS D'INITIALISATION =================== 

# 1. Agrégations des données Hôpitaux
total_lits = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_lits_occupes = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes
total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone

# 2. Calculs des KPIs Hospitaliers
taux_occupation_global = (total_lits_occupes / total_lits) * 100
densite_medicale_globale = (total_medecins / total_population) * 1000

# 3. Calculs des KPIs Médicaments
valeur_stock_usd = (
    (m1_stock * m1_cout_unitaire) +
    (m2_stock * m2_cout_unitaire) +
    (m3_stock * m3_cout_unitaire) +
    (m4_stock * m4_cout_unitaire) +
    (m5_stock * m5_cout_unitaire)
)
valeur_stock_fcfa = valeur_stock_usd * TAUX_USD_FCFA # Attention à la petite faute de frappe dans votre variable 'TAUX_USD_FCFA'

# Compteur de rupture de stock
alertes_rupture = 0
if m1_stock <= m1_seuil_rupture: alertes_rupture += 1
if m2_stock <= m2_seuil_rupture: alertes_rupture += 1
if m3_stock <= m3_seuil_rupture: alertes_rupture += 1
if m4_stock <= m4_seuil_rupture: alertes_rupture += 1
if m5_stock <= m5_seuil_rupture: alertes_rupture += 1


# === SECTION E : RAPPORT D'INVENTAIRE ======================= 
print("==================================================")
print("      RAPPORT INITIAL DU SYSTEME DE SANTE         ")
print("==================================================")
print(f"Population totale couverte : {total_population:,} habitants")
print(f"Taux d'occupation des lits : {taux_occupation_global:.2f}%")
print(f"Densité médicale globale   : {densite_medicale_globale:.3f} médecins / 1000 hab. (Seuil OMS: {SEUIL_OMS_DENSITE_MEDICALE})")
print("--------------------------------------------------")
print(f"Valeur totale du stock     : {valeur_stock_usd:.2f} USD ({valeur_stock_fcfa:,.0f} FCFA)")
print(f"Médicaments en alerte stock: {alertes_rupture} / 5")
print("==================================================")
