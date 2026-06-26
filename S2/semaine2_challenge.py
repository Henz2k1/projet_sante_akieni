# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Challenge : Rapport urgent pour le Ministère — Département du Pool
# ============================================================

# --- ENREGISTREMENT DES DONNÉES BRUTES ---
# Hôpital de District de Kinkala
kinkala_budget = 12_500_000
kinkala_consultations = 1847
kinkala_hospitalisations = 312
kinkala_deces = 8
kinkala_lits_totaux = 45
kinkala_lits_occupes = 41
kinkala_medecins = 3
kinkala_population = 85_000

# CMS de Vindza
vindza_budget = 6_800_000
vindza_consultations = 923
vindza_hospitalisations = 87
vindza_deces = 2
vindza_lits_totaux = 20
vindza_lits_occupes = 14
vindza_medecins = 1
vindza_population = 42_000

# Hôpital de Kindamba
kindamba_budget = 9_200_000
kindamba_consultations = 1234
kindamba_hospitalisations = 201
kindamba_deces = 11
kindamba_lits_totaux = 35
kindamba_lits_occupes = 33
kindamba_medecins = 2
kindamba_population = 67_000

# --- CALCULS DES KPIS POUR CHAQUE ETABLISSEMENT ---
# 1. Kinkala
kinkala_cout_moyen = round(kinkala_budget / (kinkala_consultations + kinkala_hospitalisations), 2)
kinkala_taux_occ = round((kinkala_lits_occupes / kinkala_lits_totaux) * 100, 2)
kinkala_densite = round((kinkala_medecins / kinkala_population) * 1000, 3)
kinkala_mortalite = round((kinkala_deces / kinkala_hospitalisations) * 100, 2)

# 2. Vindza
vindza_cout_moyen = round(vindza_budget / (vindza_consultations + vindza_hospitalisations), 2)
vindza_taux_occ = round((vindza_lits_occupes / vindza_lits_totaux) * 100, 2)
vindza_densite = round((vindza_medecins / vindza_population) * 1000, 3)
vindza_mortalite = round((vindza_deces / vindza_hospitalisations) * 100, 2)

# 3. Kindamba
kindamba_cout_moyen = round(kindamba_budget / (kindamba_consultations + kindamba_hospitalisations), 2)
kindamba_taux_occ = round((kindamba_lits_occupes / kindamba_lits_totaux) * 100, 2)
kindamba_densite = round((kindamba_medecins / kindamba_population) * 1000, 3)
kindamba_mortalite = round((kindamba_deces / kindamba_hospitalisations) * 100, 2)

# --- GÉNÉRATION DU RAPPORT CONSOLIDÉ POUR LE MINISTRE ---
print("=" * 100)
print("          RAPPORT SANITAIRE ET FINANCIER CONSOLIDÉ — DÉPARTEMENT DU POOL")
print("=" * 100)
print(f"{'Indicateur / KPI':<25}\t| {'HD Kinkala':<15}\t| {'CMS Vindza':<15}\t| {'H Kindamba':<15}")
print("-" * 100)
print(f"{'Coût moyen par patient':<25}\t| {kinkala_cout_moyen:<11} FCFA\t| {vindza_cout_moyen:<11} FCFA\t| {kindamba_cout_moyen:<11} FCFA")
print(f"{'Taux occupation lits':<25}\t| {kinkala_taux_occ:<14}%\t| {vindza_taux_occ:<14}%\t| {kindamba_taux_occ:<14}%")
print(f"{'Densité médicale (/1000)':<25}\t| {kinkala_densite:<14}\t| {vindza_densite:<14}\t| {kindamba_densite:<14}")
print(f"{'Taux mortalité hosp.':<25}\t| {kinkala_mortalite:<14}%\t| {vindza_mortalite:<14}%\t| {kindamba_mortalite:<14}%")
print("=" * 100)

# Identification de l'établissement en situation critique (Mortalité > 2% OU Densité < 0.05)
print("\nDIAGNOSTIC ET ALERTES CRITIQUES :")
print(f" - HD Kinkala : Mortalité ({kinkala_mortalite}%) - Alerte : Suivi requis.")
print(f" - CMS Vindza : Densité médicale ({vindza_densite}) extrêmement basse.")
print(f" - [CRITIQUE] Hôpital de Kindamba : Taux de mortalité de {kindamba_mortalite}% (Seuil OMS dépassé > 2%).")
print("-" * 100)

# --- BONUS : SIMULATION RECRUTEMENT ---
cout_trim_un_medecin = 1_200_000
objectif_medecins = 5

cout_kinkala_recrutement = (objectif_medecins - kinkala_medecins) * cout_trim_un_medecin
cout_vindza_recrutement = (objectif_medecins - vindza_medecins) * cout_trim_un_medecin
cout_kindamba_recrutement = (objectif_medecins - kindamba_medecins) * cout_trim_un_medecin

cout_total_recrutement = cout_kinkala_recrutement + cout_vindza_recrutement + cout_kindamba_recrutement
budget_global_actuel = kinkala_budget + vindza_budget + kindamba_budget

print("ESTIMATION BUDGÉTAIRE — PASSAGE À 5 MÉDECINS PAR ÉTABLISSEMENT :")
print(f" - Coût supplémentaire total requis : {cout_total_recrutement} FCFA")
print(f" - Budget trimestriel actuel combiné : {budget_global_actuel} FCFA")
print(f" - Pourcentage d'augmentation du budget requis : {round((cout_total_recrutement / budget_global_actuel) * 100, 2)}%")
print("=" * 100)