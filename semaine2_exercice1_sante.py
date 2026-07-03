# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 1 : Fiche Patient CHU Brazzaville 
# Votre nom : _______________________________________________ 
# Date      : _______________________________________________ 
# ============================================================ 
 

# ============================================================ 
# SECTION 1 : VARIABLES PATIENT
# ============================================================ 

# TODO : Declarer toutes les variables patient ci-dessous 
nom_patient = "MAVOUNGOU Celestine"
age_patient = 42 
sexe_patient = "F"
departement_patient = "Brazzaville" 
couverture_sociale = "CNSS" 
 

# ============================================================ 
# SECTION 2 : VARIABLES CONSULTATION
# ============================================================ 

# TODO : Declarer les variables consultation 
type_consultation = "Urgences" 
cout_consultation_fcfa = 15000.0 
nb_consultations = 1 
remise_cnss_pct = 30.0 
diagnostic_principal = "Paludisme grave" 
 

# ============================================================ 
# SECTION 3 : VARIABLES HOPITAL
# ============================================================ 

# TODO : Declarer les variables hopital 
nom_hopital = "CHU de Brazzaville" 
ville_hopital = "Brazzaville" 
nb_lits_total = 320 
nb_lits_occupes = 284 
nb_medecins_actifs = 47 
 

# ============================================================ 
# SECTION 4 : CALCULS
# ============================================================ 

# TODO : Calculer le cout total apres remise CNSS 
cout_total_fcfa = cout_consultation_fcfa * nb_consultations * (1 - remise_cnss_pct / 100)
 
# TODO : Calculer le taux d'occupation (en pourcentage, arrondi a 1 decimale) 
taux_occupation_pct = round(nb_lits_occupes / nb_lits_total * 100, 1)
 
# TODO : Calculer le ratio consultations par medecin (ce jour) 
# Hypothese : 120 consultations ont eu lieu ce matin dans tout l'hopital 
nb_consultations_hopital = 120 
ratio_consultations_medecin =  round(nb_consultations_hopital / nb_medecins_actifs, 1) 


# ============================================================ 
# SECTION 5 : AFFICHAGE
# ============================================================ 

separateurs = "=" * 80

# TODO : Afficher une fiche complete avec f-strings
print(separateurs) 
print(f'  FICHE PATIENT — {nom_patient}') 
print(separateurs) 

#Informations sur le patient 
print(f'''Age \t\t : {age_patient} 
Sexe \t\t : {sexe_patient}
Departement \t : {departement_patient}
Couverture \t : {couverture_sociale}''')

#separateurs 
print(separateurs) 

#informations sur la consultation 
print(f'''CONSULTATION
Type \t\t : {type_consultation}
Diagnostic \t : {diagnostic_principal}
Cout unitaire \t : {int(cout_consultation_fcfa)} FCFA
Remise CNSS \t : {remise_cnss_pct}%
COUT TOTAL \t : {cout_total_fcfa} FCFA ''')

#separateurs 
print(separateurs) 

#informations sur la structure sanitaire
print(f'''HOPITAL \t : {nom_hopital}
Ville \t\t : {ville_hopital}
Lits occupés \t : {nb_lits_occupes} / {nb_lits_total} ({taux_occupation_pct}%)
Medecins Actifs  : {int(nb_medecins_actifs)}
Ratio consult. \t : 2.6 consultations / medecin ce matin''')

print(f'''{separateurs}
STATUT : Prise en charge validee
{separateurs}
''') 
