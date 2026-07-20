# ============================================================ 
# SECTION A : CONSTANTES NATIONALES ET NORMES OMS
# ============================================================ 
TAUX_EUR_FCFA = 655.957 
TAUX_USD_FCFA = 600.0 
SEUIL_OMS_DENSITE_MEDICALE = 2.3    

# medecins pour 1000 habitants 
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  
SEUIL_MORTALITE_ALERTE = 2.0        
SEUIL_RUPTURE_STOCK_JOURS = 30      

# ============================================================ 
# SECTION B : DECLARATION DES 5 HOPITAUX
# ============================================================ 

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


# ============================================================ 
# SECTION C : VARIABLES DES 5 MEDICAMENTS
# ============================================================ 

# Médicament 1 : Artemether-lumefantrine (Antipaludique)
m1_nom            = 'Artemether-Lumefantrine'
m1_stock          = 3200
m1_seuil_rupture  = 2000
m1_cout_unitaire  = 3500.0  

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

# ============================================================ 
# SECTION D : CALCULS D'INITIALISATION KPI NUMERIQUES
# ============================================================ 

# Total des lits ppour les 5 hopitaux 
total_lits = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits

#Total des lits occupés pour les 5 hopitaux 
total_lits_occupes = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes

#Total des medecins pour les 5 hopitaux)
total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins

#Total de la population pour les 5 hopitaux 
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone

#Calculs des KPIs Hospitaliers pour les 5 hopitaux
taux_occupation_global = round(((total_lits_occupes / total_lits) * 100), 2)
densite_medicale_globale = round(((total_medecins / total_population) * 1000), 3) 

#Calculs des KPIs Médicaments
valeur_stock_usd = int((
    (m1_stock * m1_cout_unitaire) +
    (m2_stock * m2_cout_unitaire) +
    (m3_stock * m3_cout_unitaire) +
    (m4_stock * m4_cout_unitaire) +
    (m5_stock * m5_cout_unitaire)
)) 

#Conversion du stock USD en FCA 
valeur_stock_fcfa = int(valeur_stock_usd * TAUX_USD_FCFA) 

#Compteur de rupture de stock 
alertes_rupture = 0
if m1_stock <= m1_seuil_rupture: alertes_rupture += 1
if m2_stock <= m2_seuil_rupture: alertes_rupture += 1
if m3_stock <= m3_seuil_rupture: alertes_rupture += 1
if m4_stock <= m4_seuil_rupture: alertes_rupture += 1
if m5_stock <= m5_seuil_rupture: alertes_rupture += 1


#Avec cette variable, on evitera de chaque fois repeter les separateurs manuellement lors de nos affichages 
separateurs = "=" * 80


# ============================================================ 
# SECTION E : RAPPORT D'INVENTAIRE
# ============================================================ 

print(f'''{separateurs}
\tRAPPORT INITIAL DU SYSTEME DE SANTE        
{separateurs}
Population totale couverte\t: {total_population} habitants
Taux d'occupation des lits\t: {taux_occupation_global}%
Densité médicale globale\t: {densite_medicale_globale} médecins / 1000 hab. (Seuil OMS: {SEUIL_OMS_DENSITE_MEDICALE}
{separateurs}
Valeur totale du stock\t\t: {valeur_stock_usd} USD ({valeur_stock_fcfa} FCFA)
Médicaments en alerte stock\t: {alertes_rupture} / 5
{separateurs} 
\n''')


# ============================================================ 
# SECTION F : CLASSIFICATION STATUT STOCKS (MÉDICAMENTS)
# ============================================================ 

print(f'''{separateurs}
\tCLASSIFICATION DES STOCKS DE MÉDICAMENTS
{separateurs}''')

# Médicament 1
if m1_stock <= m1_seuil_rupture:
    m1_statut = "RUPTURE DE STOCK"
else:
    m1_statut = "EN STOCK"
print(f"- {m1_nom}\t: {m1_statut}")

# Médicament 2
if m2_stock <= m2_seuil_rupture:
    m2_statut = "RUPTURE DE STOCK"
else:
    m2_statut = "EN STOCK"
print(f"- {m2_nom}\t\t: {m2_statut}")

# Médicament 3
if m3_stock <= m3_seuil_rupture:
    m3_statut = "RUPTURE DE STOCK"
else:
    m3_statut = "EN STOCK"
print(f"- {m3_nom}\t\t: {m3_statut}")

# Médicament 4
if m4_stock <= m4_seuil_rupture:
    m4_statut = "RUPTURE DE STOCK"
else:
    m4_statut = "EN STOCK"
print(f"- {m4_nom}\t\t\t: {m4_statut}")

# Médicament 5
if m5_stock <= m5_seuil_rupture:
    m5_statut = "RUPTURE DE STOCK"
else:
    m5_statut = "EN STOCK"
print(f"- {m5_nom}\t\t: {m5_statut}")

#fin de la section
print(separateurs)
print("\n")


# ============================================================ 
# SECTION G : CLASSIFICATION OCCUPATION HÔPITAUX
# ============================================================ 

print(f'''{separateurs}
\tNIVEAU D'OCCUPATION PAR HOPITAL
{separateurs}''')

# Calcul des taux d'occupation pour chaque hopital 
taux_h1 = round(((h1_nb_lits_occupes / h1_nb_lits) * 100), 2) 
taux_h2 = round(((h2_nb_lits_occupes / h2_nb_lits) * 100), 2) 
taux_h3 = round(((h3_nb_lits_occupes / h3_nb_lits) * 100), 2) 
taux_h4 = round(((h4_nb_lits_occupes / h4_nb_lits) * 100), 2) 
taux_h5 = round(((h5_nb_lits_occupes / h5_nb_lits) * 100), 2) 

# Hopital 1 (CHU de Brazzaville)
if taux_h1 >= 90.0:
    h1_occupation = "CRITIQUE"
elif taux_h1 >= 75.0:
    h1_occupation = "ELEVE"
elif taux_h1 >= 50.0:
    h1_occupation = "OPTIMAL"
else:
    h1_occupation = "SOUS-UTILISE"
print(f"- {h1_nom}\t\t: {h1_occupation} ({taux_h1}%)")

# Hopital 2 (Hopital General Pointe-Noire)
if taux_h2 >= 90.0:
    h2_occupation = "CRITIQUE"
elif taux_h2 >= 75.0:
    h2_occupation = "ELEVE"
elif taux_h2 >= 50.0:
    h2_occupation = "OPTIMAL"
else:
    h2_occupation = "SOUS-UTILISE"
print(f"- {h2_nom}\t: {h2_occupation} ({taux_h2}%)")

# Hopital 3 (Hopital de Dolisie)
if taux_h3 >= 90.0:
    h3_occupation = "CRITIQUE"
elif taux_h3 >= 75.0:
    h3_occupation = "ELEVE"
elif taux_h3 >= 50.0:
    h3_occupation = "OPTIMAL"
else:
    h3_occupation = "SOUS-UTILISE"
print(f"- {h3_nom}\t\t: {h3_occupation} ({taux_h3}%)")

# Hopital 4 (Hopital de district Owando)
if taux_h4 >= 90.0:
    h4_occupation = "CRITIQUE"
elif taux_h4 >= 75.0:
    h4_occupation = "ELEVE"
elif taux_h4 >= 50.0:
    h4_occupation = "OPTIMAL"
else:
    h4_occupation = "SOUS-UTILISE"
print(f"- {h4_nom}\t: {h4_occupation} ({taux_h4}%)")

# Hopital 5 (Centre de sante de Impfondo)
if taux_h5 >= 90.0:
    h5_occupation = "CRITIQUE"
elif taux_h5 >= 75.0:
    h5_occupation = "ELEVE"
elif taux_h5 >= 50.0:
    h5_occupation = "OPTIMAL"
else:
    h5_occupation = "SOUS-UTILISE"
print(f"- {h5_nom}\t: {h5_occupation} ({taux_h5}%)")

print(separateurs)
print("\n")


# ============================================================ 
#SECTION H : CLASSIFICATION COUVERTURE VACCINALE
# ============================================================ 

print(f'''{separateurs}
\tSTATUT OMS COUVERTURE VACCINALE
{separateurs}''')

# Calcul des taux de vaccination pour les 5 hopitaux 
taux_brazzaville = (418500 / 450000) * 100  
taux_pointe_noire = (229600 / 280000) * 100
taux_pool = (54000 / 120000) * 100           
taux_sangha = (35700 / 85000) * 100        

# Brazzaville
if taux_brazzaville >= SEUIL_OMS_COUVERTURE_VACCIN:
    statut_brazzaville = "ZONE SATISFAISANTE"
else:
    statut_brazzaville = "ZONE INSUFFISANTE (< 95%)"
print(f"- Brazzaville\t: {taux_brazzaville}% \t-> {statut_brazzaville}")

# Pointe-Noire
if taux_pointe_noire >= SEUIL_OMS_COUVERTURE_VACCIN:
    statut_pointe_noire = "ZONE SATISFAISANTE"
elif taux_pointe_noire >= 80.0:
    statut_pointe_noire = "ZONE A RISQUE (< 80% non 82% => A RISQUE)"
else:
    statut_pointe_noire = "ZONE CRITIQUE (<50%)"
print(f"- Pointe-Noire\t: {taux_pointe_noire}% \t-> {statut_pointe_noire}")

# Pool
if taux_pool >= SEUIL_OMS_COUVERTURE_VACCIN:
    statut_pool = "ZONE SATISFAISANTE"
elif taux_pool >= 80.0:
    statut_pool = "ZONE A RISQUE (< 80% non 82% => A RISQUE)"
elif taux_pool >= 50.0:
    statut_pool = "ZONE INSUFFISANTE (< 95%)"
else:
    statut_pool = "ZONE CRITIQUE (<50%)"
print(f"- Pool\t\t: {taux_pool}% \t-> {statut_pool}")

# Sangha
if taux_sangha >= SEUIL_OMS_COUVERTURE_VACCIN:
    statut_sangha = "ZONE SATISFAISANTE"
elif taux_sangha >= 80.0:
    statut_sangha = "ZONE A RISQUE (< 80% non 82% => A RISQUE)"
elif taux_sangha >= 50.0:
    statut_sangha = "ZONE INSUFFISANTE (< 95%)"
else:
    statut_sangha = "ZONE CRITIQUE (<50%)"
print(f"- Sangha\t: {taux_sangha}% \t-> {statut_sangha}")

print(separateurs)
print("\n")


# ============================================================ 
# SECTION I : RAPPORT D'ÉTAT GLOBAL AVEC ALERTES
# ============================================================ 

# Compteurs d'alertes pour les hôpitaux en saturation (critique >= 90%)
alertes_hopitaux_saturation = 0

if taux_h1 >= 90.0:
    alertes_hopitaux_saturation += 1
if taux_h2 >= 90.0:
    alertes_hopitaux_saturation += 1
if taux_h3 >= 90.0:
    alertes_hopitaux_saturation += 1
if taux_h4 >= 90.0:
    alertes_hopitaux_saturation += 1
if taux_h5 >= 90.0:
    alertes_hopitaux_saturation += 1

# Compteurs de zones vaccinales critiques (<50%)
alertes_zones_critiques = 0
if taux_brazzaville < 50.0:
    alertes_zones_critiques += 1
if taux_pointe_noire < 50.0:
    alertes_zones_critiques += 1
if taux_pool < 50.0:
    alertes_zones_critiques += 1
if taux_sangha < 50.0:
    alertes_zones_critiques += 1


print(f'''{separateurs})
RAPPORT D'ÉTAT GLOBAL
{separateurs}
Ruptures de stock de médicaments\t: {alertes_rupture} / 5)
Hôpitaux en saturation (critiques)\t: {alertes_hopitaux_saturation} / 5)
Zones vaccinales critiques (< 50%)\t: {alertes_zones_critiques} / 4)
{separateurs}\n
Résumé Exécutif :
Le système de santé couvre une population totale de {total_population} habitants
La valeur totale des stocks s'élève à {valeur_stock_usd} USD ({valeur_stock_fcfa} FCFA)
Le taux d'occupation global des lits est de {taux_occupation_global}%.
{separateurs}''')
