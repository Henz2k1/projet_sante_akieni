# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 2 : KPIs Sanitaires OMS 
# ============================================================ 


# ============================================================ 
# DONNEES BRUTES
# ============================================================ 

budget_fcfa = 87_450_000 # underscore pour lisibilité des grands nombres 
nb_consultations_ext = 4823 
nb_hospitalisations = 1247 
nb_deces = 18 
nb_lits_total = 180 
nb_lits_occupes = 143 
nb_medecins = 22 
nb_infirmiers = 58 
population_dept = 128_000 
taux_eur_fcfa = 655.957 
taux_usd_fcfa = 600.0 


# # ============================================================ 
# CALCULS COMPLÉTÉS
# ============================================================  

# 1. Conversions devises (arrondies à 2 décimales)
budget_eur = round(budget_fcfa / taux_eur_fcfa, 2) 
budget_usd = round(budget_fcfa / taux_usd_fcfa, 2) 

# 2. Indicateurs OMS (Densité pour 1000 hab, Mortalité et Occupation en %)
densite_medicale = round((nb_medecins / population_dept) * 1000, 1) 
taux_mortalite = round((nb_deces / nb_hospitalisations) * 100, 1) 
taux_occupation = round((nb_lits_occupes / nb_lits_total) * 100, 1) 

# 3. Division entière et modulo pour la pharmacie
budget_medicaments = round(float(budget_fcfa * 0.35))
cout_journalier_meds = 450_000 
jours_stock = budget_medicaments // cout_journalier_meds 
jours_restants = budget_medicaments % cout_journalier_meds 

# 4. Puissance pour la projection budgétaire à N+2 (Croissance de 8% par an sur 2 ans)
budget_n_plus_2 = budget_fcfa * (1.08 ** 2) 


# ============================================================ 
# AFFICHAGE RAPPORT
# ============================================================ 

separateurs = "=" * 80

print(f'''{separateurs}
RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire
{separateurs}''') 

#INFORMATIONS SUR LE BUDGET
print(f'''BUDGET
\tDepenses Q4\t\t: {budget_fcfa}\tFCFA
\tEn euros \t\t: {budget_eur}\tEUR
\tEn dollars \t\t: {budget_usd}\tUSD''')

#INDICATEURS OMS
print(f'''
INDICATEURS OMS
\tDensité médicale\t: {densite_medicale} médecins / 1000 hab [Norme OMS : >= 2.3]
\tTaux mortalité\t\t: {taux_mortalite}%\t\t\t [Seuil alerte : > 2%]
\tTaux occupation\t\t: {taux_occupation}%\t\t\t [Optimal : 70-85%]''')

#INFORMATIONS SUR LA PHARMACIE
print(f'''
ANALYSE PHARMACIE
\tBudget médicaments\t: {budget_medicaments} FCFA
\tJours de stock\t\t: {jours_stock} jours
\tJours dépassement\t: {jours_restants // cout_journalier_meds} jours''')

#PROJECTION
print(F'''
PROJECTION
\tBudget N+2 (8%/an): {budget_n_plus_2} FCFA''')

#MESSAGE D'ALERTE
print(f"ALERTE : Densité médicale CRITIQUE ({densite_medicale} pour 1000 hab — norme OMS : 2.3)")
