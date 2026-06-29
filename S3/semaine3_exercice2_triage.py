# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not
# ============================================================

print('=== SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE ===')
print('Protocole Manchester adapte — DSS Congo 2026')
print()

# --- SAISIE DES DONNEES PATIENT (S2 reutilise : input(), conversion) ---

nom_patient = input('Nom du patient : ')
age_patient = int(input('Age (annees) : '))
temperature = float(input('Temperature (degres C, ex: 38.4) : '))
spo2 = float(input('Saturation O2 en % (ex: 96.0) : '))
tension_syst = int(input('Tension systolique en mmHg (ex: 135) : '))
douleur = int(input('Douleur /10 (0=aucune, 10=insupportable) : '))

# --- VALIDATION DES PLAGES (S2 + S3 : conditions simples) ---

# Validation de la temperature
if not (temperature >= 35.0 and temperature <= 43.0):
    print('ERREUR : Valeur de temperature impossible — verifier la saisie')

#Validation du nom
nom_patient = nom_patient.strip()
if len(nom_patient) < 3:
    print("Le nom du patient doit avoir au moins 3 caracteres")

# Validation de la saturation en oxygene (Sp02)
if not (spo2 >= 50.0 and spo2 <= 100.0):
    print("Sp02 entré est hors plage, veuillez verifiez le capteur")

# Validation de la tension
if not (tension_syst >= 50 and tension_syst <= 250):
    print("Tension hors plage, vérifiez le brassard")

# Validation de la douleur 
if not (douleur >= 0 and douleur <= 10):
    print("La douleur doit etre entre 0 et 10") 

# Validation de l'age 
if not (age_patient >= 0 and age_patient <= 120):
    print("Age invalide, verifiez la saisie")



# Dans une version avancee, on redemanderait la saisie ici
# TODO : Valider spo2, tension_syst, douleur, age de la meme facon
# --- TRIAGE (S3 nouveau : conditions composees avec or) ---

# Niveau 1 : IMMEDIAT — au moins UNE condition critique suffit (or)
if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
 niveau_triage = '1 - IMMEDIAT'
 couleur_triage = '[ROUGE]'
 delai_pec = '< 0 minute'
 action_triage = 'Medecin present immediatement'

# Niveau 2 : URGENT — conditions moins critiques mais toujours urgentes
elif temperature > 38.5 or spo2 < 94 or tension_syst > 140 :
 niveau_triage = '2 - URGENT'
 couleur_triage = '[ORANGE]'
 delai_pec = '< 10 munites'
 action_triage = 'Appel medecin senoir'

# Niveau 3 : URGENT DIFFERE
elif temperature > 37.5 or douleur > 6:
 niveau_triage = '3 - URGENT DIFFERE'
 couleur_triage = '[JAUNE]'
 delai_pec = '< 30 munites'
 action_triage = 'Infirmier - surveillance'

# Niveau 4 : MOINS URGENT (cas par defaut)
else:
 niveau_triage = '4 - MOINS URGENT'
 couleur_triage = '[VERT]'
 delai_pec = '< 120 munites'
 action_triage = 'File d\'attente standard'

# --- DETERMINATION DYNAMIQUE DES STATUTS POUR L'AFFICHAGE (DONNEES SUMULES PUISQU'ILNE SONT PAS BIEN PRECISEES)---
statut_temp = "[ANORMAL]" if temperature > 37.5 else "[NORMAL]"
statut_spo2 = "[ANORMAL]" if spo2 < 94 else "[NORMAL]"
statut_tension = "[ANORMAL]" if tension_syst > 140 else "[NORMAL]"
statut_douleur = "[ANORMAL]" if douleur > 6 else "[NORMAL]"



# # --- AFFICHAGE FICHE TRIAGE (S2 reutilise : f-strings) ---

# TODO : Afficher tous les parametres vitaux et le resultat du triage

separateurs = "=" * 80

print("\n")
print(f'''{separateurs})
RESULTAT TRIAGE — {nom_patient.upper()}
{separateurs}''')

print(f'''PARAMETRES VITAUX
\tTemperature \t\t : {temperature} °C \t [ANORMAL -> 39.5]
\tSaturation SpO2 \t : {spo2} % \t [NORMAL]
\tTension systol. \t\t : {tension_syst} mmHg \t [NORMAL]
\tDouleur \t\t : {douleur} / 10\t [NORMAL]
''')

print("-" * 80)

print(f'''
\tNIVEAU DE TRAIGE\t: {niveau_triage}
\tCOULEUR  \t\t: {couleur_triage}
\tPRISE EN CHARGE \t: {delai_pec}
\tACTION   \t\t: {action_triage}
''')

print("-" * 80)
print(f'Motif principal \t: Temperature {temperature} °C > seuil 39.5 °C')
print(separateurs)


