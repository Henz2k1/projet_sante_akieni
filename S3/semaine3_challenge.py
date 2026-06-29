# ==============================================================================
# DECLARATION DES VARIABLES POUR LES 5 HOPITAUX
# ==============================================================================

# Hopital 1 — CHU de Brazzaville 
h1_nom              = 'CHU de Brazzaville' 
h1_ville            = 'Brazzaville' 
h1_departement      = 'Brazzaville' 
h1_type             = 'CHU' 
h1_nb_lits          = 320 
h1_nb_lits_occupes  = 298 
h1_nb_medecins      = 47 
h1_population_zone  = 1_800_000 

# Hopital 2 - Hopital General Pointe-Noire  
h2_nom              = 'Hopital General Pointe-Noire' 
h2_ville            = 'Pointe-Noire' 
h2_departement      = 'Pointe-Noire' 
h2_type             = 'Hopital General' 
h2_nb_lits          = 180 
h2_nb_lits_occupes  = 143 
h2_nb_medecins      = 22 
h2_population_zone  = 1_200_000 

# Hopital 3 - Hopital de Dolisie
h3_nom              = 'Hopital de Dolisie' 
h3_ville            = 'Dolisie' 
h3_departement      = 'Niari' 
h3_type             = 'Hopital de reference' 
h3_nb_lits          = 95 
h3_nb_lits_occupes  = 91 
h3_nb_medecins      = 8 
h3_population_zone  = 180_000 

# Hopital 4 - Hopital de district Owando  
h4_nom              = 'Hopital de district Owando' 
h4_ville            = 'Owando' 
h4_departement      = 'Cuvette' 
h4_type             = 'Hopital de district' 
h4_nb_lits          = 45 
h4_nb_lits_occupes  = 32 
h4_nb_medecins      = 3 
h4_population_zone  = 90_000 

# Hopital 5 - CMS Impfondo 
h5_nom              = 'CMS Impfondo' 
h5_ville            = 'Impfondo' 
h5_departement      = 'Likouala' 
h5_type             = 'CMS' 
h5_nb_lits          = 20 
h5_nb_lits_occupes  = 19 
h5_nb_medecins      = 1 
h5_population_zone  = 45_000


# ==============================================================================
# STOCK MEDICAMENTS HOPITAL 1 — CHU de Brazzaville
# ==============================================================================

# En alerte : Artemether (3200 < 4000), Amoxicilline (950 < 1200)
# En rupture : SRO (0), Vaccin (150 < 1000)

m1_h1_nom            = 'Artemether-Lumefantrine'
m1_h1_stock          = 3000
m1_h1_seuil_rupture  = 2000
m1_h1_cout_unitaire  = 3500.0

m2_h1_nom            = 'Amoxicilline 500mg'
m2_h1_stock          = 950
m2_h1_seuil_rupture  = 800
m2_h1_cout_unitaire  = 850.0

m3_h1_nom            = 'Paracetamol 500mg'
m3_h1_stock          = 12400
m3_h1_seuil_rupture  = 3000
m3_h1_cout_unitaire  = 120.0

m4_h1_nom            = 'SRO (sachets)'
m4_h1_stock          = 4200
m4_h1_seuil_rupture  = 5000
m4_h1_cout_unitaire  = 125.0

m5_h1_nom            = 'Vaccin DTP-HepB-Hib'
m5_h1_stock          = 820
m5_h1_seuil_rupture  = 1000
m5_h1_cout_unitaire  = 8500.0


# ==============================================================================
# STOCK MEDICAMENTS HOPITAL 2 — Hopital General Pointe-Noire
# ==============================================================================

# En alerte : Amoxicilline (600 < 800)
# En rupture : Aucun

m1_h2_nom            = 'Artemether-Lumefantrine'
m1_h2_stock          = 2500
m1_h2_seuil_rupture  = 1500
m1_h2_cout_unitaire  = 3500.0

m2_h2_nom            = 'Amoxicilline 500mg'
m2_h2_stock          = 950
m2_h2_seuil_rupture  = 800
m2_h2_cout_unitaire  = 850.0

m3_h2_nom            = 'Paracetamol 500mg'
m3_h2_stock          = 8000
m3_h2_seuil_rupture  = 2000
m3_h2_cout_unitaire  = 120.0

m4_h2_nom            = 'SRO (sachets)'
m4_h2_stock          = 1800
m4_h2_seuil_rupture  = 1000
m4_h2_cout_unitaire  = 125.0

m5_h2_nom            = 'Vaccin DTP-HepB-Hib'
m5_h2_stock          = 1200
m5_h2_seuil_rupture  = 600
m5_h2_cout_unitaire  = 8500.0


# ==============================================================================
# STOCK MEDICAMENTS HOPITAL 3 — Hopital de Dolisie
# ==============================================================================

# En alerte : Artemether (550 < 800), Vaccin (120 < 300)
# En rupture : SRO (0)

m1_h3_nom            = 'Artemether-Lumefantrine'
m1_h3_stock          = 1200
m1_h3_seuil_rupture  = 800
m1_h3_cout_unitaire  = 3500.0

m2_h3_nom            = 'Amoxicilline 500mg'
m2_h3_stock          = 900
m2_h3_seuil_rupture  = 400
m2_h3_cout_unitaire  = 850.0

m3_h3_nom            = 'Paracetamol 500mg'
m3_h3_stock          = 4500
m3_h3_seuil_rupture  = 1000
m3_h3_cout_unitaire  = 120.0

m4_h3_nom            = 'SRO (sachets)'
m4_h3_stock          = 200
m4_h3_seuil_rupture  = 600
m4_h3_cout_unitaire  = 125.0

m5_h3_nom            = 'Vaccin DTP-HepB-Hib'
m5_h3_stock          = 400
m5_h3_seuil_rupture  = 300
m5_h3_cout_unitaire  = 8500.0


# ==============================================================================
# STOCK MEDICAMENTS HOPITAL 4 — Hopital de district Owando
# ==============================================================================

# En alerte : Aucun
# En rupture : Artemether (0), SRO (0), Vaccin (5)

m1_h4_nom            = 'Artemether-Lumefantrine'
m1_h4_stock          = 100
m1_h4_seuil_rupture  = 400
m1_h4_cout_unitaire  = 3500.0

m2_h4_nom            = 'Amoxicilline 500mg'
m2_h4_stock          = 500
m2_h4_seuil_rupture  = 200
m2_h4_cout_unitaire  = 850.0

m3_h4_nom            = 'Paracetamol 500mg'
m3_h4_stock          = 3100
m3_h4_seuil_rupture  = 600
m3_h4_cout_unitaire  = 120.0

m4_h4_nom            = 'SRO (sachets)'
m4_h4_stock          = 45
m4_h4_seuil_rupture  = 300
m4_h4_cout_unitaire  = 125.0

m5_h4_nom            = 'Vaccin DTP-HepB-Hib'
m5_h4_stock          = 30
m5_h4_seuil_rupture  = 150
m5_h4_cout_unitaire  = 8500.0


# ==============================================================================
# STOCK MEDICAMENTS HOPITAL 5 — CMS Impfondo
# ==============================================================================

# En alerte : Vaccin (35 < 80)
# En rupture : SRO (0), Amoxicilline (0)

m1_h5_nom            = 'Artemether-Lumefantrine'
m1_h5_stock          = 250
m1_h5_seuil_rupture  = 150
m1_h5_cout_unitaire  = 3500.0

m2_h5_nom            = 'Amoxicilline 500mg'
m2_h5_stock          = 20
m2_h5_seuil_rupture  = 100
m2_h5_cout_unitaire  = 850.0

m3_h5_nom            = 'Paracetamol 500mg'
m3_h5_stock          = 1500
m3_h5_seuil_rupture  = 400
m3_h5_cout_unitaire  = 120.0

m4_h5_nom            = 'SRO (sachets)'
m4_h5_stock          = 50
m4_h5_seuil_rupture  = 150
m4_h5_cout_unitaire  = 125.0

m5_h5_nom            = 'Vaccin DTP-HepB-Hib'
m5_h5_stock          = 100
m5_h5_seuil_rupture  = 80
m5_h5_cout_unitaire  = 8500.0



# ==============================================================================
# CLASSIFICATION DES STOCKS — HOPITAL 1 (CHU DE BRAZZAVILLE)
# ==============================================================================

# Médicament 1
if m1_h1_stock <= m1_h1_seuil_rupture:
    m1_h1_statut, m1_h1_couleur, m1_h1_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m1_h1_stock <= m1_h1_seuil_rupture * 1.5:
    m1_h1_statut, m1_h1_couleur, m1_h1_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m1_h1_stock <= m1_h1_seuil_rupture * 2.0:
    m1_h1_statut, m1_h1_couleur, m1_h1_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m1_h1_statut, m1_h1_couleur, m1_h1_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 2
if m2_h1_stock <= m2_h1_seuil_rupture:
    m2_h1_statut, m2_h1_couleur, m2_h1_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m2_h1_stock <= m2_h1_seuil_rupture * 1.5:
    m2_h1_statut, m2_h1_couleur, m2_h1_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m2_h1_stock <= m2_h1_seuil_rupture * 2.0:
    m2_h1_statut, m2_h1_couleur, m2_h1_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m2_h1_statut, m2_h1_couleur, m2_h1_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 3
if m3_h1_stock <= m3_h1_seuil_rupture:
    m3_h1_statut, m3_h1_couleur, m3_h1_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m3_h1_stock <= m3_h1_seuil_rupture * 1.5:
    m3_h1_statut, m3_h1_couleur, m3_h1_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m3_h1_stock <= m3_h1_seuil_rupture * 2.0:
    m3_h1_statut, m3_h1_couleur, m3_h1_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m3_h1_statut, m3_h1_couleur, m3_h1_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 4
if m4_h1_stock <= m4_h1_seuil_rupture:
    m4_h1_statut, m4_h1_couleur, m4_h1_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m4_h1_stock <= m4_h1_seuil_rupture * 1.5:
    m4_h1_statut, m4_h1_couleur, m4_h1_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m4_h1_stock <= m4_h1_seuil_rupture * 2.0:
    m4_h1_statut, m4_h1_couleur, m4_h1_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m4_h1_statut, m4_h1_couleur, m4_h1_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 5
if m5_h1_stock <= m5_h1_seuil_rupture:
    m5_h1_statut, m5_h1_couleur, m5_h1_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m5_h1_stock <= m5_h1_seuil_rupture * 1.5:
    m5_h1_statut, m5_h1_couleur, m5_h1_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m5_h1_stock <= m5_h1_seuil_rupture * 2.0:
    m5_h1_statut, m5_h1_couleur, m5_h1_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m5_h1_statut, m5_h1_couleur, m5_h1_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'


# ==============================================================================
# CLASSIFICATION DES STOCKS — HOPITAL 2 (HOPITAL GENERAL POINTE-NOIRE)
# ==============================================================================

# Médicament 1
if m1_h2_stock <= m1_h2_seuil_rupture:
    m1_h2_statut, m1_h2_couleur, m1_h2_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m1_h2_stock <= m1_h2_seuil_rupture * 1.5:
    m1_h2_statut, m1_h2_couleur, m1_h2_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m1_h2_stock <= m1_h2_seuil_rupture * 2.0:
    m1_h2_statut, m1_h2_couleur, m1_h2_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m1_h2_statut, m1_h2_couleur, m1_h2_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 2
if m2_h2_stock <= m2_h2_seuil_rupture:
    m2_h2_statut, m2_h2_couleur, m2_h2_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m2_h2_stock <= m2_h2_seuil_rupture * 1.5:
    m2_h2_statut, m2_h2_couleur, m2_h2_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m2_h2_stock <= m2_h2_seuil_rupture * 2.0:
    m2_h2_statut, m2_h2_couleur, m2_h2_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m2_h2_statut, m2_h2_couleur, m2_h2_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 3
if m3_h2_stock <= m3_h2_seuil_rupture:
    m3_h2_statut, m3_h2_couleur, m3_h2_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m3_h2_stock <= m3_h2_seuil_rupture * 1.5:
    m3_h2_statut, m3_h2_couleur, m3_h2_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m3_h2_stock <= m3_h2_seuil_rupture * 2.0:
    m3_h2_statut, m3_h2_couleur, m3_h2_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m3_h2_statut, m3_h2_couleur, m3_h2_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 4
if m4_h2_stock <= m4_h2_seuil_rupture:
    m4_h2_statut, m4_h2_couleur, m4_h2_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m4_h2_stock <= m4_h2_seuil_rupture * 1.5:
    m4_h2_statut, m4_h2_couleur, m4_h2_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m4_h2_stock <= m4_h2_seuil_rupture * 2.0:
    m4_h2_statut, m4_h2_couleur, m4_h2_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m4_h2_statut, m4_h2_couleur, m4_h2_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 5
if m5_h2_stock <= m5_h2_seuil_rupture:
    m5_h2_statut, m5_h2_couleur, m5_h2_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m5_h2_stock <= m5_h2_seuil_rupture * 1.5:
    m5_h2_statut, m5_h2_couleur, m5_h2_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m5_h2_stock <= m5_h2_seuil_rupture * 2.0:
    m5_h2_statut, m5_h2_couleur, m5_h2_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m5_h2_statut, m5_h2_couleur, m5_h2_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'


# ==============================================================================
# CLASSIFICATION DES STOCKS — HOPITAL 3 (HOPITAL DE DOLISIE)
# ==============================================================================

# Médicament 1
if m1_h3_stock <= m1_h3_seuil_rupture:
    m1_h3_statut, m1_h3_couleur, m1_h3_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m1_h3_stock <= m1_h3_seuil_rupture * 1.5:
    m1_h3_statut, m1_h3_couleur, m1_h3_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m1_h3_stock <= m1_h3_seuil_rupture * 2.0:
    m1_h3_statut, m1_h3_couleur, m1_h3_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m1_h3_statut, m1_h3_couleur, m1_h3_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 2
if m2_h3_stock <= m2_h3_seuil_rupture:
    m2_h3_statut, m2_h3_couleur, m2_h3_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m2_h3_stock <= m2_h3_seuil_rupture * 1.5:
    m2_h3_statut, m2_h3_couleur, m2_h3_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m2_h3_stock <= m2_h3_seuil_rupture * 2.0:
    m2_h3_statut, m2_h3_couleur, m2_h3_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m2_h3_statut, m2_h3_couleur, m2_h3_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 3
if m3_h3_stock <= m3_h3_seuil_rupture:
    m3_h3_statut, m3_h3_couleur, m3_h3_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m3_h3_stock <= m3_h3_seuil_rupture * 1.5:
    m3_h3_statut, m3_h3_couleur, m3_h3_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m3_h3_stock <= m3_h3_seuil_rupture * 2.0:
    m3_h3_statut, m3_h3_couleur, m3_h3_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m3_h3_statut, m3_h3_couleur, m3_h3_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 4
if m4_h3_stock <= m4_h3_seuil_rupture:
    m4_h3_statut, m4_h3_couleur, m4_h3_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m4_h3_stock <= m4_h3_seuil_rupture * 1.5:
    m4_h3_statut, m4_h3_couleur, m4_h3_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m4_h3_stock <= m4_h3_seuil_rupture * 2.0:
    m4_h3_statut, m4_h3_couleur, m4_h3_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m4_h3_statut, m4_h3_couleur, m4_h3_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 5
if m5_h3_stock <= m5_h3_seuil_rupture:
    m5_h3_statut, m5_h3_couleur, m5_h3_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m5_h3_stock <= m5_h3_seuil_rupture * 1.5:
    m5_h3_statut, m5_h3_couleur, m5_h3_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m5_h3_stock <= m5_h3_seuil_rupture * 2.0:
    m5_h3_statut, m5_h3_couleur, m5_h3_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m5_h3_statut, m5_h3_couleur, m5_h3_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'


# ==============================================================================
# CLASSIFICATION DES STOCKS — HOPITAL 4 (HOPITAL DE DISTRICT OWANDO)
# ==============================================================================

# Médicament 1
if m1_h4_stock <= m1_h4_seuil_rupture:
    m1_h4_statut, m1_h4_couleur, m1_h4_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m1_h4_stock <= m1_h4_seuil_rupture * 1.5:
    m1_h4_statut, m1_h4_couleur, m1_h4_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m1_h4_stock <= m1_h4_seuil_rupture * 2.0:
    m1_h4_statut, m1_h4_couleur, m1_h4_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m1_h4_statut, m1_h4_couleur, m1_h4_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 2
if m2_h4_stock <= m2_h4_seuil_rupture:
    m2_h4_statut, m2_h4_couleur, m2_h4_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m2_h4_stock <= m2_h4_seuil_rupture * 1.5:
    m2_h4_statut, m2_h4_couleur, m2_h4_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m2_h4_stock <= m2_h4_seuil_rupture * 2.0:
    m2_h4_statut, m2_h4_couleur, m2_h4_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m2_h4_statut, m2_h4_couleur, m2_h4_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 3
if m3_h4_stock <= m3_h4_seuil_rupture:
    m3_h4_statut, m3_h4_couleur, m3_h4_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m3_h4_stock <= m3_h4_seuil_rupture * 1.5:
    m3_h4_statut, m3_h4_couleur, m3_h4_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m3_h4_stock <= m3_h4_seuil_rupture * 2.0:
    m3_h4_statut, m3_h4_couleur, m3_h4_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m3_h4_statut, m3_h4_couleur, m3_h4_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 4
if m4_h4_stock <= m4_h4_seuil_rupture:
    m4_h4_statut, m4_h4_couleur, m4_h4_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m4_h4_stock <= m4_h4_seuil_rupture * 1.5:
    m4_h4_statut, m4_h4_couleur, m4_h4_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m4_h4_stock <= m4_h4_seuil_rupture * 2.0:
    m4_h4_statut, m4_h4_couleur, m4_h4_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m4_h4_statut, m4_h4_couleur, m4_h4_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 5
if m5_h4_stock <= m5_h4_seuil_rupture:
    m5_h4_statut, m5_h4_couleur, m5_h4_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m5_h4_stock <= m5_h4_seuil_rupture * 1.5:
    m5_h4_statut, m5_h4_couleur, m5_h4_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m5_h4_stock <= m5_h4_seuil_rupture * 2.0:
    m5_h4_statut, m5_h4_couleur, m5_h4_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m5_h4_statut, m5_h4_couleur, m5_h4_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'


# ==============================================================================
# CLASSIFICATION DES STOCKS — HOPITAL 5 (CMS IMPFONDO)
# ==============================================================================

# Médicament 1
if m1_h5_stock <= m1_h5_seuil_rupture:
    m1_h5_statut, m1_h5_couleur, m1_h5_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m1_h5_stock <= m1_h5_seuil_rupture * 1.5:
    m1_h5_statut, m1_h5_couleur, m1_h5_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m1_h5_stock <= m1_h5_seuil_rupture * 2.0:
    m1_h5_statut, m1_h5_couleur, m1_h5_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m1_h5_statut, m1_h5_couleur, m1_h5_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 2
if m2_h5_stock <= m2_h5_seuil_rupture:
    m2_h5_statut, m2_h5_couleur, m2_h5_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m2_h5_stock <= m2_h5_seuil_rupture * 1.5:
    m2_h5_statut, m2_h5_couleur, m2_h5_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m2_h5_stock <= m2_h5_seuil_rupture * 2.0:
    m2_h5_statut, m2_h5_couleur, m2_h5_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m2_h5_statut, m2_h5_couleur, m2_h5_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 3
if m3_h5_stock <= m3_h5_seuil_rupture:
    m3_h5_statut, m3_h5_couleur, m3_h5_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m3_h5_stock <= m3_h5_seuil_rupture * 1.5:
    m3_h5_statut, m3_h5_couleur, m3_h5_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m3_h5_stock <= m3_h5_seuil_rupture * 2.0:
    m3_h5_statut, m3_h5_couleur, m3_h5_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m3_h5_statut, m3_h5_couleur, m3_h5_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 4
if m4_h5_stock <= m4_h5_seuil_rupture:
    m4_h5_statut, m4_h5_couleur, m4_h5_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m4_h5_stock <= m4_h5_seuil_rupture * 1.5:
    m4_h5_statut, m4_h5_couleur, m4_h5_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m4_h5_stock <= m4_h5_seuil_rupture * 2.0:
    m4_h5_statut, m4_h5_couleur, m4_h5_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m4_h5_statut, m4_h5_couleur, m4_h5_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 5
if m5_h5_stock <= m5_h5_seuil_rupture:
    m5_h5_statut, m5_h5_couleur, m5_h5_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immediate PNA — commande express sous 24h'
elif m5_h5_stock <= m5_h5_seuil_rupture * 1.5:
    m5_h5_statut, m5_h5_couleur, m5_h5_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente a declencher sous 72h'
elif m5_h5_stock <= m5_h5_seuil_rupture * 2.0:
    m5_h5_statut, m5_h5_couleur, m5_h5_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcee-planifier commande'
else:
    m5_h5_statut, m5_h5_couleur, m5_h5_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'



# ==============================================================================
# HOPITAL 1 — CHU DE BRAZZAVILLE
# ==============================================================================

# 1. Initialisation des compteurs et chaînes de caractères
nb_ruptures_critiques_h1 = 0
nb_alertes_stock_h1      = 0
nb_stock_limites_h1      = 0
nb_stock_normaux_h1      = 0

name_med_critique_h1      = ""
name_med_alerte_stock_h1  = ""
name_med_stock_limite_h1  = ""
name_med_stock_normaux_h1 = ""

# Comptage Médicament 1
if m1_h1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h1 += 1; name_med_critique_h1 += m1_h1_nom + ", "
elif m1_h1_statut == 'ALERTE STOCK': nb_alertes_stock_h1 += 1; name_med_alerte_stock_h1 += m1_h1_nom + ", "
elif m1_h1_statut == 'STOCK LIMITE': nb_stock_limites_h1 += 1; name_med_stock_limite_h1 += m1_h1_nom + ", "
elif m1_h1_statut == 'STOCK NORMAL': nb_stock_normaux_h1 += 1; name_med_stock_normaux_h1 += m1_h1_nom + ", "

# Comptage Médicament 2
if m2_h1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h1 += 1; name_med_critique_h1 += m2_h1_nom + ", "
elif m2_h1_statut == 'ALERTE STOCK': nb_alertes_stock_h1 += 1; name_med_alerte_stock_h1 += m2_h1_nom + ", "
elif m2_h1_statut == 'STOCK LIMITE': nb_stock_limites_h1 += 1; name_med_stock_limite_h1 += m2_h1_nom + ", "
elif m2_h1_statut == 'STOCK NORMAL': nb_stock_normaux_h1 += 1; name_med_stock_normaux_h1 += m2_h1_nom + ", "

# Comptage Médicament 3
if m3_h1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h1 += 1; name_med_critique_h1 += m3_h1_nom + ", "
elif m3_h1_statut == 'ALERTE STOCK': nb_alertes_stock_h1 += 1; name_med_alerte_stock_h1 += m3_h1_nom + ", "
elif m3_h1_statut == 'STOCK LIMITE': nb_stock_limites_h1 += 1; name_med_stock_limite_h1 += m3_h1_nom + ", "
elif m3_h1_statut == 'STOCK NORMAL': nb_stock_normaux_h1 += 1; name_med_stock_normaux_h1 += m3_h1_nom + ", "

# Comptage Médicament 4
if m4_h1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h1 += 1; name_med_critique_h1 += m4_h1_nom + ", "
elif m4_h1_statut == 'ALERTE STOCK': nb_alertes_stock_h1 += 1; name_med_alerte_stock_h1 += m4_h1_nom + ", "
elif m4_h1_statut == 'STOCK LIMITE': nb_stock_limites_h1 += 1; name_med_stock_limite_h1 += m4_h1_nom + ", "
elif m4_h1_statut == 'STOCK NORMAL': nb_stock_normaux_h1 += 1; name_med_stock_normaux_h1 += m4_h1_nom + ", "

# Comptage Médicament 5
if m5_h1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h1 += 1; name_med_critique_h1 += m5_h1_nom + ", "
elif m5_h1_statut == 'ALERTE STOCK': nb_alertes_stock_h1 += 1; name_med_alerte_stock_h1 += m5_h1_nom + ", "
elif m5_h1_statut == 'STOCK LIMITE': nb_stock_limites_h1 += 1; name_med_stock_limite_h1 += m5_h1_nom + ", "
elif m5_h1_statut == 'STOCK NORMAL': nb_stock_normaux_h1 += 1; name_med_stock_normaux_h1 += m5_h1_nom + ", "

# # 2. Affichage Rapport Hôpital 1
# print('=' * 65)
# print(f'  RAPPORT DE STOCK — {h1_nom.upper()}')
# print('  Date : 15 janvier 2026')
# print('=' * 65)
# print(f'  [M1] {m1_h1_couleur} {m1_h1_nom}')
# print(f'       Stock : {m1_h1_stock} unites | Seuil rupture : {m1_h1_seuil_rupture}')
# print(f'       Statut : {m1_h1_statut} | Action : {m1_h1_action}')
# print('-' * 65)
# print(f'  [M2] {m2_h1_couleur} {m2_h1_nom}')
# print(f'       Stock : {m2_h1_stock} unites | Seuil rupture : {m2_h1_seuil_rupture}')
# print(f'       Statut : {m2_h1_statut} | Action : {m2_h1_action}')
# print('-' * 65)
# print(f'  [M3] {m3_h1_couleur} {m3_h1_nom}')
# print(f'       Stock : {m3_h1_stock} unites | Seuil rupture : {m3_h1_seuil_rupture}')
# print(f'       Statut : {m3_h1_statut} | Action : {m3_h1_action}')
# print('-' * 65)
# print(f'  [M4] {m4_h1_couleur} {m4_h1_nom}')
# print(f'       Stock : {m4_h1_stock} unites | Seuil rupture : {m4_h1_seuil_rupture}')
# print(f'       Statut : {m4_h1_statut} | Action : {m4_h1_action}')
# print('-' * 65)
# print(f'  [M5] {m5_h1_couleur} {m5_h1_nom}')
# print(f'       Stock : {m5_h1_stock} unites | Seuil rupture : {m5_h1_seuil_rupture}')
# print(f'       Statut : {m5_h1_statut} | Action : {m5_h1_action}')
# print('=' * 65)
# print(f'  SYNTHÈSE : Ruptures: {nb_ruptures_critiques_h1} | Alertes: {nb_alertes_stock_h1} | Limites: {nb_stock_limites_h1}')
# print('=' * 65 + '\n')


# ==============================================================================
# HOPITAL 2 — HOPITAL GENERAL POINTE-NOIRE
# ==============================================================================

nb_ruptures_critiques_h2 = 0
nb_alertes_stock_h2      = 0
nb_stock_limites_h2      = 0
nb_stock_normaux_h2      = 0

name_med_critique_h2, name_med_alerte_stock_h2, name_med_stock_limite_h2, name_med_stock_normaux_h2 = "", "", "", ""

if m1_h2_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h2 += 1; name_med_critique_h2 += m1_h2_nom + ", "
elif m1_h2_statut == 'ALERTE STOCK': nb_alertes_stock_h2 += 1; name_med_alerte_stock_h2 += m1_h2_nom + ", "
elif m1_h2_statut == 'STOCK LIMITE': nb_stock_limites_h2 += 1; name_med_stock_limite_h2 += m1_h2_nom + ", "
elif m1_h2_statut == 'STOCK NORMAL': nb_stock_normaux_h2 += 1; name_med_stock_normaux_h2 += m1_h2_nom + ", "

if m2_h2_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h2 += 1; name_med_critique_h2 += m2_h2_nom + ", "
elif m2_h2_statut == 'ALERTE STOCK': nb_alertes_stock_h2 += 1; name_med_alerte_stock_h2 += m2_h2_nom + ", "
elif m2_h2_statut == 'STOCK LIMITE': nb_stock_limites_h2 += 1; name_med_stock_limite_h2 += m2_h2_nom + ", "
elif m2_h2_statut == 'STOCK NORMAL': nb_stock_normaux_h2 += 1; name_med_stock_normaux_h2 += m2_h2_nom + ", "

if m3_h2_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h2 += 1; name_med_critique_h2 += m3_h2_nom + ", "
elif m3_h2_statut == 'ALERTE STOCK': nb_alertes_stock_h2 += 1; name_med_alerte_stock_h2 += m3_h2_nom + ", "
elif m3_h2_statut == 'STOCK LIMITE': nb_stock_limites_h2 += 1; name_med_stock_limite_h2 += m3_h2_nom + ", "
elif m3_h2_statut == 'STOCK NORMAL': nb_stock_normaux_h2 += 1; name_med_stock_normaux_h2 += m3_h2_nom + ", "

if m4_h2_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h2 += 1; name_med_critique_h2 += m4_h2_nom + ", "
elif m4_h2_statut == 'ALERTE STOCK': nb_alertes_stock_h2 += 1; name_med_alerte_stock_h2 += m4_h2_nom + ", "
elif m4_h2_statut == 'STOCK LIMITE': nb_stock_limites_h2 += 1; name_med_stock_limite_h2 += m4_h2_nom + ", "
elif m4_h2_statut == 'STOCK NORMAL': nb_stock_normaux_h2 += 1; name_med_stock_normaux_h2 += m4_h2_nom + ", "

if m5_h2_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h2 += 1; name_med_critique_h2 += m5_h2_nom + ", "
elif m5_h2_statut == 'ALERTE STOCK': nb_alertes_stock_h2 += 1; name_med_alerte_stock_h2 += m5_h2_nom + ", "
elif m5_h2_statut == 'STOCK LIMITE': nb_stock_limites_h2 += 1; name_med_stock_limite_h2 += m5_h2_nom + ", "
elif m5_h2_statut == 'STOCK NORMAL': nb_stock_normaux_h2 += 1; name_med_stock_normaux_h2 += m5_h2_nom + ", "

# print('=' * 65)
# print(f'  RAPPORT DE STOCK — {h2_nom.upper()}')
# print('  Date : 15 janvier 2026')
# print('=' * 65)
# print(f'  [M1] {m1_h2_couleur} {m1_h2_nom}')
# print(f'       Stock : {m1_h2_stock} unites | Seuil rupture : {m1_h2_seuil_rupture}')
# print(f'       Statut : {m1_h2_statut} | Action : {m1_h2_action}')
# print('-' * 65)
# print(f'  [M2] {m2_h2_couleur} {m2_h2_nom}')
# print(f'       Stock : {m2_h2_stock} unites | Seuil rupture : {m2_h2_seuil_rupture}')
# print(f'       Statut : {m2_h2_statut} | Action : {m2_h2_action}')
# print('-' * 65)
# print(f'  [M3] {m3_h2_couleur} {m3_h2_nom}')
# print(f'       Stock : {m3_h2_stock} unites | Seuil rupture : {m3_h2_seuil_rupture}')
# print(f'       Statut : {m3_h2_statut} | Action : {m3_h2_action}')
# print('-' * 65)
# print(f'  [M4] {m4_h2_couleur} {m4_h2_nom}')
# print(f'       Stock : {m4_h2_stock} unites | Seuil rupture : {m4_h2_seuil_rupture}')
# print(f'       Statut : {m4_h2_statut} | Action : {m4_h2_action}')
# print('-' * 65)
# print(f'  [M5] {m5_h2_couleur} {m5_h2_nom}')
# print(f'       Stock : {m5_h2_stock} unites | Seuil rupture : {m5_h2_seuil_rupture}')
# print(f'       Statut : {m5_h2_statut} | Action : {m5_h2_action}')
# print('=' * 65)
# print(f'  SYNTHÈSE : Ruptures: {nb_ruptures_critiques_h2} | Alertes: {nb_alertes_stock_h2} | Limites: {nb_stock_limites_h2}')
# print('=' * 65 + '\n')


# ==============================================================================
# HOPITAL 3 — HOPITAL DE DOLISIE
# ==============================================================================

nb_ruptures_critiques_h3 = 0
nb_alertes_stock_h3      = 0
nb_stock_limites_h3      = 0
nb_stock_normaux_h3      = 0

name_med_critique_h3, name_med_alerte_stock_h3, name_med_stock_limite_h3, name_med_stock_normaux_h3 = "", "", "", ""

if m1_h3_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h3 += 1; name_med_critique_h3 += m1_h3_nom + ", "
elif m1_h3_statut == 'ALERTE STOCK': nb_alertes_stock_h3 += 1; name_med_alerte_stock_h3 += m1_h3_nom + ", "
elif m1_h3_statut == 'STOCK LIMITE': nb_stock_limites_h3 += 1; name_med_stock_limite_h3 += m1_h3_nom + ", "
elif m1_h3_statut == 'STOCK NORMAL': nb_stock_normaux_h3 += 1; name_med_stock_normaux_h3 += m1_h3_nom + ", "

if m2_h3_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h3 += 1; name_med_critique_h3 += m2_h3_nom + ", "
elif m2_h3_statut == 'ALERTE STOCK': nb_alertes_stock_h3 += 1; name_med_alerte_stock_h3 += m2_h3_nom + ", "
elif m2_h3_statut == 'STOCK LIMITE': nb_stock_limites_h3 += 1; name_med_stock_limite_h3 += m2_h3_nom + ", "
elif m2_h3_statut == 'STOCK NORMAL': nb_stock_normaux_h3 += 1; name_med_stock_normaux_h3 += m2_h3_nom + ", "

if m3_h3_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h3 += 1; name_med_critique_h3 += m3_h3_nom + ", "
elif m3_h3_statut == 'ALERTE STOCK': nb_alertes_stock_h3 += 1; name_med_alerte_stock_h3 += m3_h3_nom + ", "
elif m3_h3_statut == 'STOCK LIMITE': nb_stock_limites_h3 += 1; name_med_stock_limite_h3 += m3_h3_nom + ", "
elif m3_h3_statut == 'STOCK NORMAL': nb_stock_normaux_h3 += 1; name_med_stock_normaux_h3 += m3_h3_nom + ", "

if m4_h3_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h3 += 1; name_med_critique_h3 += m4_h3_nom + ", "
elif m4_h3_statut == 'ALERTE STOCK': nb_alertes_stock_h3 += 1; name_med_alerte_stock_h3 += m4_h3_nom + ", "
elif m4_h3_statut == 'STOCK LIMITE': nb_stock_limites_h3 += 1; name_med_stock_limite_h3 += m4_h3_nom + ", "
elif m4_h3_statut == 'STOCK NORMAL': nb_stock_normaux_h3 += 1; name_med_stock_normaux_h3 += m4_h3_nom + ", "

if m5_h3_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h3 += 1; name_med_critique_h3 += m5_h3_nom + ", "
elif m5_h3_statut == 'ALERTE STOCK': nb_alertes_stock_h3 += 1; name_med_alerte_stock_h3 += m5_h3_nom + ", "
elif m5_h3_statut == 'STOCK LIMITE': nb_stock_limites_h3 += 1; name_med_stock_limite_h3 += m5_h3_nom + ", "
elif m5_h3_statut == 'STOCK NORMAL': nb_stock_normaux_h3 += 1; name_med_stock_normaux_h3 += m5_h3_nom + ", "

# print('=' * 65)
# print(f'  RAPPORT DE STOCK — {h3_nom.upper()}')
# print('  Date : 15 janvier 2026')
# print('=' * 65)
# print(f'  [M1] {m1_h3_couleur} {m1_h3_nom}')
# print(f'       Stock : {m1_h3_stock} unites | Seuil rupture : {m1_h3_seuil_rupture}')
# print(f'       Statut : {m1_h3_statut} | Action : {m1_h3_action}')
# print('-' * 65)
# print(f'  [M2] {m2_h3_couleur} {m2_h3_nom}')
# print(f'       Stock : {m2_h3_stock} unites | Seuil rupture : {m2_h3_seuil_rupture}')
# print(f'       Statut : {m2_h3_statut} | Action : {m2_h3_action}')
# print('-' * 65)
# print(f'  [M3] {m3_h3_couleur} {m3_h3_nom}')
# print(f'       Stock : {m3_h3_stock} unites | Seuil rupture : {m3_h3_seuil_rupture}')
# print(f'       Statut : {m3_h3_statut} | Action : {m3_h3_action}')
# print('-' * 65)
# print(f'  [M4] {m4_h3_couleur} {m4_h3_nom}')
# print(f'       Stock : {m4_h3_stock} unites | Seuil rupture : {m4_h3_seuil_rupture}')
# print(f'       Statut : {m4_h3_statut} | Action : {m4_h3_action}')
# print('-' * 65)
# print(f'  [M5] {m5_h3_couleur} {m5_h3_nom}')
# print(f'       Stock : {m5_h3_stock} unites | Seuil rupture : {m5_h3_seuil_rupture}')
# print(f'       Statut : {m5_h3_statut} | Action : {m5_h3_action}')
# print('=' * 65)
# print(f'  SYNTHÈSE : Ruptures: {nb_ruptures_critiques_h3} | Alertes: {nb_alertes_stock_h3} | Limites: {nb_stock_limites_h3}')
# print('=' * 65 + '\n')


# ==============================================================================
# HOPITAL 4 — HOPITAL DE DISTRICT OWANDO
# ==============================================================================

nb_ruptures_critiques_h4 = 0
nb_alertes_stock_h4      = 0
nb_stock_limites_h4      = 0
nb_stock_normaux_h4      = 0

name_med_critique_h4, name_med_alerte_stock_h4, name_med_stock_limite_h4, name_med_stock_normaux_h4 = "", "", "", ""

if m1_h4_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h4 += 1; name_med_critique_h4 += m1_h4_nom + ", "
elif m1_h4_statut == 'ALERTE STOCK': nb_alertes_stock_h4 += 1; name_med_alerte_stock_h4 += m1_h4_nom + ", "
elif m1_h4_statut == 'STOCK LIMITE': nb_stock_limites_h4 += 1; name_med_stock_limite_h4 += m1_h4_nom + ", "
elif m1_h4_statut == 'STOCK NORMAL': nb_stock_normaux_h4 += 1; name_med_stock_normaux_h4 += m1_h4_nom + ", "

if m2_h4_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h4 += 1; name_med_critique_h4 += m2_h4_nom + ", "
elif m2_h4_statut == 'ALERTE STOCK': nb_alertes_stock_h4 += 1; name_med_alerte_stock_h4 += m2_h4_nom + ", "
elif m2_h4_statut == 'STOCK LIMITE': nb_stock_limites_h4 += 1; name_med_stock_limite_h4 += m2_h4_nom + ", "
elif m2_h4_statut == 'STOCK NORMAL': nb_stock_normaux_h4 += 1; name_med_stock_normaux_h4 += m2_h4_nom + ", "

if m3_h4_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h4 += 1; name_med_critique_h4 += m3_h4_nom + ", "
elif m3_h4_statut == 'ALERTE STOCK': nb_alertes_stock_h4 += 1; name_med_alerte_stock_h4 += m3_h4_nom + ", "
elif m3_h4_statut == 'STOCK LIMITE': nb_stock_limites_h4 += 1; name_med_stock_limite_h4 += m3_h4_nom + ", "
elif m3_h4_statut == 'STOCK NORMAL': nb_stock_normaux_h4 += 1; name_med_stock_normaux_h4 += m3_h4_nom + ", "

if m4_h4_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h4 += 1; name_med_critique_h4 += m4_h4_nom + ", "
elif m4_h4_statut == 'ALERTE STOCK': nb_alertes_stock_h4 += 1; name_med_alerte_stock_h4 += m4_h4_nom + ", "
elif m4_h4_statut == 'STOCK LIMITE': nb_stock_limites_h4 += 1; name_med_stock_limite_h4 += m4_h4_nom + ", "
elif m4_h4_statut == 'STOCK NORMAL': nb_stock_normaux_h4 += 1; name_med_stock_normaux_h4 += m4_h4_nom + ", "

if m5_h4_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h4 += 1; name_med_critique_h4 += m5_h4_nom + ", "
elif m5_h4_statut == 'ALERTE STOCK': nb_alertes_stock_h4 += 1; name_med_alerte_stock_h4 += m5_h4_nom + ", "
elif m5_h4_statut == 'STOCK LIMITE': nb_stock_limites_h4 += 1; name_med_stock_limite_h4 += m5_h4_nom + ", "
elif m5_h4_statut == 'STOCK NORMAL': nb_stock_normaux_h4 += 1; name_med_stock_normaux_h4 += m5_h4_nom + ", "

# print('=' * 65)
# print(f'  RAPPORT DE STOCK — {h4_nom.upper()}')
# print('  Date : 15 janvier 2026')
# print('=' * 65)
# print(f'  [M1] {m1_h4_couleur} {m1_h4_nom}')
# print(f'       Stock : {m1_h4_stock} unites | Seuil rupture : {m1_h4_seuil_rupture}')
# print(f'       Statut : {m1_h4_statut} | Action : {m1_h4_action}')
# print('-' * 65)
# print(f'  [M2] {m2_h4_couleur} {m2_h4_nom}')
# print(f'       Stock : {m2_h4_stock} unites | Seuil rupture : {m2_h4_seuil_rupture}')
# print(f'       Statut : {m2_h4_statut} | Action : {m2_h4_action}')
# print('-' * 65)
# print(f'  [M3] {m3_h4_couleur} {m3_h4_nom}')
# print(f'       Stock : {m3_h4_stock} unites | Seuil rupture : {m3_h4_seuil_rupture}')
# print(f'       Statut : {m3_h4_statut} | Action : {m3_h4_action}')
# print('-' * 65)
# print(f'  [M4] {m4_h4_couleur} {m4_h4_nom}')
# print(f'       Stock : {m4_h4_stock} unites | Seuil rupture : {m4_h4_seuil_rupture}')
# print(f'       Statut : {m4_h4_statut} | Action : {m4_h4_action}')
# print('-' * 65)
# print(f'  [M5] {m5_h4_couleur} {m5_h4_nom}')
# print(f'       Stock : {m5_h4_stock} unites | Seuil rupture : {m5_h4_seuil_rupture}')
# print(f'       Statut : {m5_h4_statut} | Action : {m5_h4_action}')
# print('=' * 65)
# print(f'  SYNTHÈSE : Ruptures: {nb_ruptures_critiques_h4} | Alertes: {nb_alertes_stock_h4} | Limites: {nb_stock_limites_h4}')
# print('=' * 65 + '\n')


# ==============================================================================
# HOPITAL 5 — CMS IMPFONDO
# ==============================================================================

nb_ruptures_critiques_h5 = 0
nb_alertes_stock_h5      = 0
nb_stock_limites_h5      = 0
nb_stock_normaux_h5      = 0

name_med_critique_h5, name_med_alerte_stock_h5, name_med_stock_limite_h5, name_med_stock_normaux_h5 = "", "", "", ""

if m1_h5_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h5 += 1; name_med_critique_h5 += m1_h5_nom + ", "
elif m1_h5_statut == 'ALERTE STOCK': nb_alertes_stock_h5 += 1; name_med_alerte_stock_h5 += m1_h5_nom + ", "
elif m1_h5_statut == 'STOCK LIMITE': nb_stock_limites_h5 += 1; name_med_stock_limite_h5 += m1_h5_nom + ", "
elif m1_h5_statut == 'STOCK NORMAL': nb_stock_normaux_h5 += 1; name_med_stock_normaux_h5 += m1_h5_nom + ", "

if m2_h5_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h5 += 1; name_med_critique_h5 += m2_h5_nom + ", "
elif m2_h5_statut == 'ALERTE STOCK': nb_alertes_stock_h5 += 1; name_med_alerte_stock_h5 += m2_h5_nom + ", "
elif m2_h5_statut == 'STOCK LIMITE': nb_stock_limites_h5 += 1; name_med_stock_limite_h5 += m2_h5_nom + ", "
elif m2_h5_statut == 'STOCK NORMAL': nb_stock_normaux_h5 += 1; name_med_stock_normaux_h5 += m2_h5_nom + ", "

if m3_h5_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h5 += 1; name_med_critique_h5 += m3_h5_nom + ", "
elif m3_h5_statut == 'ALERTE STOCK': nb_alertes_stock_h5 += 1; name_med_alerte_stock_h5 += m3_h5_nom + ", "
elif m3_h5_statut == 'STOCK LIMITE': nb_stock_limites_h5 += 1; name_med_stock_limite_h5 += m3_h5_nom + ", "
elif m3_h5_statut == 'STOCK NORMAL': nb_stock_normaux_h5 += 1; name_med_stock_normaux_h5 += m3_h5_nom + ", "

if m4_h5_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h5 += 1; name_med_critique_h5 += m4_h5_nom + ", "
elif m4_h5_statut == 'ALERTE STOCK': nb_alertes_stock_h5 += 1; name_med_alerte_stock_h5 += m4_h5_nom + ", "
elif m4_h5_statut == 'STOCK LIMITE': nb_stock_limites_h5 += 1; name_med_stock_limite_h5 += m4_h5_nom + ", "
elif m4_h5_statut == 'STOCK NORMAL': nb_stock_normaux_h5 += 1; name_med_stock_normaux_h5 += m4_h5_nom + ", "

if m5_h5_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques_h5 += 1; name_med_critique_h5 += m5_h5_nom + ", "
elif m5_h5_statut == 'ALERTE STOCK': nb_alertes_stock_h5 += 1; name_med_alerte_stock_h5 += m5_h5_nom + ", "
elif m5_h5_statut == 'STOCK LIMITE': nb_stock_limites_h5 += 1; name_med_stock_limite_h5 += m5_h5_nom + ", "
elif m5_h5_statut == 'STOCK NORMAL': nb_stock_normaux_h5 += 1; name_med_stock_normaux_h5 += m5_h5_nom + ", "


# ==============================================================================
# CALCUL DES KPIs POUR CHAQUE HÔPITAL
# ==============================================================================

# Hôpital 1 — CHU de Brazzaville
taux_occupation_h1 = round(((h1_nb_lits_occupes / h1_nb_lits) * 100), 2) 
densite_medicale_h1 = (h1_nb_medecins / h1_population_zone) * 1000

# Hôpital 2 — Hôpital Général Pointe-Noire
taux_occupation_h2 = round(((h2_nb_lits_occupes / h2_nb_lits) * 100), 2) 
densite_medicale_h2 = (h2_nb_medecins / h2_population_zone) * 1000

# Hôpital 3 — Hôpital de Dolisie
taux_occupation_h3 = round(((h3_nb_lits_occupes / h3_nb_lits) * 100),2) 
densite_medicale_h3 = (h3_nb_medecins / h3_population_zone) * 1000

# Hôpital 4 — Hôpital de district Owando
taux_occupation_h4 = round(((h4_nb_lits_occupes / h4_nb_lits) * 100), 2) 
densite_medicale_h4 = (h4_nb_medecins / h4_population_zone) * 1000

# Hôpital 5 — CMS Impfondo
taux_occupation_h5 = round(((h5_nb_lits_occupes / h5_nb_lits) * 100), 2) 
densite_medicale_h5 = (h5_nb_medecins / h5_population_zone) * 1000


# ==============================================================================
# DÉTERMINATION DES NIVEAUX D'ALERTE POUR CHAQUE HÔPITAL
# ==============================================================================

# --- Hôpital 1 — CHU de Brazzaville ---
niveau_alerte_h1 = ""
if nb_ruptures_critiques_h1 >= 2 or taux_occupation_h1 > 95:
    niveau_alerte_h1 = '[CRITIQUE]'
elif (nb_ruptures_critiques_h1 >= 1 or taux_occupation_h1 > 85) or (nb_alertes_stock_h1 >= 2 and h1_nb_medecins < 5):
    niveau_alerte_h1 = '[PREOCCUPANT]'
else:
    niveau_alerte_h1 = '[SATISFAIT]'

# --- Hôpital 2 — Hôpital Général Pointe-Noire ---
niveau_alerte_h2 = ""
if nb_ruptures_critiques_h2 >= 2 or taux_occupation_h2 > 95:
    niveau_alerte_h2 = '[CRITIQUE]'
elif (nb_ruptures_critiques_h2 >= 1 or taux_occupation_h2 > 85) or (nb_alertes_stock_h2 >= 2 and h2_nb_medecins < 5):
    niveau_alerte_h2 = '[PREOCCUPANT]'
else:
    niveau_alerte_h2 = '[SATISFAIT]'

# --- Hôpital 3 — Hôpital de Dolisie ---
niveau_alerte_h3 = ""
if nb_ruptures_critiques_h3 >= 2 or taux_occupation_h3 > 95:
    niveau_alerte_h3 = '[CRITIQUE]'
elif (nb_ruptures_critiques_h3 >= 1 or taux_occupation_h3 > 85) or (nb_alertes_stock_h3 >= 2 and h3_nb_medecins < 5):
    niveau_alerte_h3 = '[PREOCCUPANT]'
else:
    niveau_alerte_h3 = '[SATISFAIT]'

# --- Hôpital 4 — Hôpital de district Owando ---
niveau_alerte_h4 = ""
if nb_ruptures_critiques_h4 >= 2 or taux_occupation_h4 > 95:
    niveau_alerte_h4 = '[CRITIQUE]'
elif (nb_ruptures_critiques_h4 >= 1 or taux_occupation_h4 > 85) or (nb_alertes_stock_h4 >= 2 and h4_nb_medecins < 5):
    niveau_alerte_h4 = '[PREOCCUPANT]'
else:
    niveau_alerte_h4 = '[SATISFAIT]'

# --- Hôpital 5 — CMS Impfondo ---
niveau_alerte_h5 = ""
if nb_ruptures_critiques_h5 >= 2 or taux_occupation_h5 > 95:
    niveau_alerte_h5 = '[CRITIQUE]'
elif (nb_ruptures_critiques_h5 >= 1 or taux_occupation_h5 > 85) or (nb_alertes_stock_h5 >= 2 and h5_nb_medecins < 5):
    niveau_alerte_h5 = '[PREOCCUPANT]'
else:
    niveau_alerte_h5 = '[SATISFAIT]'

# ==============================================================================
# CALCULS PRÉALABLES DES STATUTS D'OCCUPATION POUR L'AFFICHAGE
# ==============================================================================

# Hôpital 1 — CHU Brazzaville
if taux_occupation_h1 > 95: status_occ_h1 = '[CRI]'
elif taux_occupation_h1 > 85: status_occ_h1 = '[ALT]'
else: status_occ_h1 = '[OK ]'

# Hôpital 2 — Hopital Pointe-Noire
if taux_occupation_h2 > 95: status_occ_h2 = '[CRI]'
elif taux_occupation_h2 > 85: status_occ_h2 = '[ALT]'
else: status_occ_h2 = '[OK ]'

# Hôpital 3 — Hopital Dolisie
if taux_occupation_h3 > 95: status_occ_h3 = '[CRI]'
elif taux_occupation_h3 > 85: status_occ_h3 = '[ALT]'
else: status_occ_h3 = '[OK ]'

# Hôpital 4 — Hopital Owando
if taux_occupation_h4 > 95: status_occ_h4 = '[CRI]'
elif taux_occupation_h4 > 85: status_occ_h4 = '[ALT]'
else: status_occ_h4 = '[OK ]'

# Hôpital 5 — CMS Impfondo
if taux_occupation_h5 > 95: status_occ_h5 = '[CRI]'
elif taux_occupation_h5 > 85: status_occ_h5 = '[ALT]'
else: status_occ_h5 = '[OK ]'


# ==============================================================================
# AGREGATION DES COMPTEURS NATIONAUX
# ==============================================================================
total_ruptures_national = (nb_ruptures_critiques_h1 + nb_ruptures_critiques_h2 + nb_ruptures_critiques_h3 + nb_ruptures_critiques_h4 + nb_ruptures_critiques_h5)

nb_hopitaux_critiques = 0
if niveau_alerte_h1 == '[CRITIQUE]': nb_hopitaux_critiques += 1
if niveau_alerte_h2 == '[CRITIQUE]': nb_hopitaux_critiques += 1
if niveau_alerte_h3 == '[CRITIQUE]': nb_hopitaux_critiques += 1
if niveau_alerte_h4 == '[CRITIQUE]': nb_hopitaux_critiques += 1
if niveau_alerte_h5 == '[CRITIQUE]': nb_hopitaux_critiques += 1


# ==============================================================================
# GENERATION DE L'ETAT DE SORTIE FINAL
# ==============================================================================

separateurs = "=" * 80

print(f'''{separateurs}
TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE
Date : 16 janvier 2026  |  Pour le Conseil des Ministres
{separateurs}
''')

print(f'''{separateurs}
{"HOPITAL"} {"OCCUPATION"} {"ALERTES"} {"NIVEAU GLOBAL"}
{separateurs}
''')

# Lignes des hôpitaux
print(f'''{h1_nom}\t\t {taux_occupation_h1}% {status_occ_h1}   {nb_ruptures_critiques_h1}R + {nb_alertes_stock_h1}A    {niveau_alerte_h1}
{h2_nom}\t {taux_occupation_h2}% {status_occ_h2}   {nb_ruptures_critiques_h2}R + {nb_alertes_stock_h2}A    {niveau_alerte_h2}
{h3_nom}\t\t {taux_occupation_h3}% {status_occ_h3}   {nb_ruptures_critiques_h3}R + {nb_alertes_stock_h3}A    {niveau_alerte_h3}
{h4_nom}\t {taux_occupation_h4}% {status_occ_h4}   {nb_ruptures_critiques_h4}R + {nb_alertes_stock_h4}A    {niveau_alerte_h4}
{h5_nom}\t\t\t {taux_occupation_h5}% \t{status_occ_h5}   {nb_ruptures_critiques_h5}R + {nb_alertes_stock_h5}A    {niveau_alerte_h5}''')

print(separateurs)

# Synthèse et recommandations
print(f'''{nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE
{total_ruptures_national} ruptures de stock identifiees a l\'echelle nationale
RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA
{separateurs}''')