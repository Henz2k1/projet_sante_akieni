
import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog

# Importations des composants Rich pour l'interface graphique du terminal
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

# Initialisation de la console Rich pour les affichages stylisés
console_virtuelle = Console()

NOM_APP = "WAGNER - FILES SORT"

# Configuration des filtres : associe un nom de dossier à ses extensions cibles
CONFIG_EXTENSIONS_DOSSIERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv', '.md'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Musique': ['.mp3', '.wav', '.flac', '.aac'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z']
}

# Variable globale servant de mémoire à court terme pour la fonction "Annuler"
HISTORIQUE_DES_DEPLACEMENTS = []


# ==============================================================================
# ANALYSER LA CATÉGORIE D'UN FICHIER
# ==============================================================================
def analyser_categorie_fichier(nom_fichier):
    """
    Examine l'extension d'un fichier et détermine le dossier de destination approprié.
    """
    _, extension_fichier = os.path.splitext(nom_fichier)
    extension_fichier = extension_fichier.lower()
    
    for categorie_dossier, liste_extensions in CONFIG_EXTENSIONS_DOSSIERS.items():
        if extension_fichier in liste_extensions:
            return categorie_dossier
            
    return 'Autres'


# ==============================================================================
# GÉNÉRER UN CHEMIN SANS DOUBLON (SÉCURITÉ)
# ==============================================================================
def generer_chemin_sans_doublon(chemin_cible_theorique):
    """
    Vérifie la présence d'un fichier au chemin ciblé.
    Si un conflit existe, génère un nom unique en ajoutant un index numérique (ex: doc_1.pdf).
    """
    if not os.path.exists(chemin_cible_theorique):
        return chemin_cible_theorique, False
    
    dossier_parent, nom_complet_fichier = os.path.split(chemin_cible_theorique)
    nom_sans_extension, extension_fichier = os.path.splitext(nom_complet_fichier)
    
    compteur_doublons = 1
    while True:
        nouveau_nom_fichier = f"{nom_sans_extension}_{compteur_doublons}{extension_fichier}"
        nouveau_chemin_potentiel = os.path.join(dossier_parent, nouveau_nom_fichier)
        
        if not os.path.exists(nouveau_chemin_potentiel):
            return nouveau_chemin_potentiel, True
            
        compteur_doublons += 1


# ==============================================================================
# EXÉCUTER LE TRI DES FICHIERS
# ==============================================================================
def executer_le_tri(chemin_dossier_a_trier):
    """
    Scanne le dossier, pilote la barre de progression visuelle,
    déplace physiquement les fichiers et affiche le tableau de synthèse.
    """
    global HISTORIQUE_DES_DEPLACEMENTS
    console_virtuelle.clear()
    console_virtuelle.print(Panel("[bold blue]Lancement du protocole de tri...[/bold blue]", border_style="blue"))
    
    try:
        liste_fichiers_a_trier = [
            element for element in os.listdir(chemin_dossier_a_trier) 
            if os.path.isfile(os.path.join(chemin_dossier_a_trier, element))
        ]
    except Exception as erreur_systeme:
        console_virtuelle.print(f"[bold red]Erreur : Impossible d'accéder au dossier : {erreur_systeme}[/bold red]")
        time.sleep(2)
        return

    if not liste_fichiers_a_trier:
        console_virtuelle.print("\n[yellow]Le dossier est déjà parfaitement propre et ordonné ![/yellow]")
        time.sleep(2)
        return

    HISTORIQUE_DES_DEPLACEMENTS = []
    donnees_tableau_bilan = []

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40, style="black", complete_style="green"),
        TaskProgressColumn(),
        console=console_virtuelle
    ) as barre_progression:
        
        tache_deplacement = barre_progression.add_task("[cyan]Tri des fichiers en cours...", total=len(liste_fichiers_a_trier))

        for nom_fichier in liste_fichiers_a_trier:
            chemin_origine_complet = os.path.join(chemin_dossier_a_trier, nom_fichier)
            
            categorie_assignee = analyser_categorie_fichier(nom_fichier)
            dossier_destination_final = os.path.join(chemin_dossier_a_trier, categorie_assignee)
            
            os.makedirs(dossier_destination_final, exist_ok=True)
            
            chemin_cible_theorique = os.path.join(dossier_destination_final, nom_fichier)
            chemin_final_securise, a_ete_renomme = generer_chemin_sans_doublon(chemin_cible_theorique)
            
            shutil.move(chemin_origine_complet, chemin_final_securise)
            
            HISTORIQUE_DES_DEPLACEMENTS.append((chemin_origine_complet, chemin_final_securise))
            
            resultat_statut = "Renomme (Doublon)" if a_ete_renomme else "Succes"
            donnees_tableau_bilan.append((nom_fichier, categorie_assignee, resultat_statut))
            
            time.sleep(0.05)
            barre_progression.advance(tache_deplacement)

    console_virtuelle.clear()
    tableau_synthese = Table(title="Bilan complet de l'operation de nettoyage", title_style="bold cyan", style="blue")
    tableau_synthese.add_column("Fichier d'origine", style="white")
    tableau_synthese.add_column("Dossier assigné", style="magenta")
    tableau_synthese.add_column("Statut final", style="green")
    
    for fichier, categorie, statut in donnees_tableau_bilan:
        style_statut = "bold yellow" if "Renomme" in statut else "bold green"
        tableau_synthese.add_row(fichier, categorie, f"[{style_statut}]{statut}[/{style_statut}]")
        
    console_virtuelle.print(tableau_synthese)
    console_virtuelle.print("\n[bold green]Tri termine ! Si vous avez fait une erreur, utilisez l'option 'Annuler' du menu.[/bold green]")
    console_virtuelle.print("[italic white]Appuyez sur Entrée pour revenir au menu principal...[/italic white]")
    input()


# ==============================================================================
#  ANNULER LE DERNIER TRI (UNDO)
# ==============================================================================
def annuler_dernier_tri():
    """
    Restaure les fichiers déplacés lors du dernier tri à leur emplacement d'origine.
    """
    global HISTORIQUE_DES_DEPLACEMENTS
    console_virtuelle.clear()
    
    if not HISTORIQUE_DES_DEPLACEMENTS:
        console_virtuelle.print(Panel("[bold red]Aucune action de tri enregistrée en mémoire ou action déjà annulée.[/bold red]", border_style="red"))
        time.sleep(2.5)
        return

    console_virtuelle.print(Panel(f"[bold yellow]Restauration en cours de {len(HISTORIQUE_DES_DEPLACEMENTS)} fichier(s)...[/bold yellow]", border_style="yellow"))
    
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40, style="black", complete_style="yellow"),
        TaskProgressColumn(),
        console=console_virtuelle
    ) as barre_progression:
        
        tache_restauration = barre_progression.add_task("[yellow]Restauration des fichiers...", total=len(HISTORIQUE_DES_DEPLACEMENTS))
        
        for chemin_origine_initial, chemin_final_actuel in HISTORIQUE_DES_DEPLACEMENTS:
            if os.path.exists(chemin_final_actuel):
                shutil.move(chemin_final_actuel, chemin_origine_initial)
            
            time.sleep(0.05)
            barre_progression.advance(tache_restauration)

    ensemble_dossiers_crees = set([os.path.dirname(paire[1]) for paire in HISTORIQUE_DES_DEPLACEMENTS])
    for dossier_a_verifier in ensemble_dossiers_crees:
        try:
            if os.path.exists(dossier_a_verifier) and not os.listdir(dossier_a_verifier):
                os.rmdir(dossier_a_verifier)
        except Exception:
            pass

    HISTORIQUE_DES_DEPLACEMENTS = []
    
    console_virtuelle.print("\n[bold green]Annulation reussie ! Tous les fichiers ont repris leur place d'origine.[/bold green]")
    time.sleep(2.5)


# ==============================================================================
# CONFIGURER ET SÉLECTIONNER LE DOSSIER CIBLE
# ==============================================================================
def configurer_dossier_cible():
    """
    Gère l'appel à l'explorateur graphique de fichiers ou la saisie au clavier.
    """
    while True:
        console_virtuelle.clear()
        options_text = (
            "[bold cyan][G][/bold cyan] Ouvrir le gestionnaire graphique (Recommande)\n"
            "[bold cyan][M][/bold cyan] Saisir le chemin textuellement au clavier\n"
            "[bold cyan][Q][/bold cyan] Revenir en arriere"
        )
        console_virtuelle.print(Panel(options_text, title="[yellow]Comment souhaitez-vous sélectionner le dossier ?[/yellow]", border_style="yellow", width=70))
        
        methode_selection = Prompt.ask("[bold white]Votre choix[/bold white]")
        
        if methode_selection == 'q' :
            return None
            
        elif methode_selection == 'g'or "G":
            console_virtuelle.print("\n[bold blue]Fenetre du gestionnaire ouverte...[/bold blue]")
            
            instanciation_tkinter = tk.Tk()
            instanciation_tkinter.withdraw()
            instanciation_tkinter.attributes('-topmost', True)
            
            chemin_selectionne_graphique = filedialog.askdirectory(title="Sélectionnez le dossier cible à trier")
            instanciation_tkinter.destroy()
            
            if chemin_selectionne_graphique:
                console_virtuelle.print(f"\n[bold green]Dossier valide :[/bold green] {chemin_selectionne_graphique}")
                time.sleep(1.5)
                return chemin_selectionne_graphique
            else:
                console_virtuelle.print("\n[bold red]Aucune sélection effectuée.[/bold red]")
                time.sleep(1.5)
                
        elif methode_selection == 'm':
            console_virtuelle.print("\n[bold yellow]Saisissez le chemin complet du dossier :[/bold yellow]")
            chemin_saisi_clavier = Prompt.ask("[cyan]Chemin[/cyan]")
            
            chemin_absolu_calcule = os.path.abspath(os.path.expanduser(chemin_saisi_clavier))
            
            if os.path.exists(chemin_absolu_calcule) and os.path.isdir(chemin_absolu_calcule):
                console_virtuelle.print(f"\n[bold green]Dossier valide :[/bold green] {chemin_absolu_calcule}")
                time.sleep(1.5)
                return chemin_absolu_calcule
            else:
                console_virtuelle.print("\n[bold red]Erreur : Le chemin spécifié est introuvable ou invalide.[/bold red]")
                time.sleep(2)


# ==============================================================================
# AFFICHER LES RÈGLES DE TRI ACTUELLES
# ==============================================================================
def afficher_regles_actuelles():
    """
    Génère un tableau ordonné résumant les critères de tri configurés dans le script.
    """
    console_virtuelle.clear()
    tableau_regles = Table(title="Regles de tri actuelles du système", title_style="bold magenta", style="magenta")
    tableau_regles.add_column("Dossier cible", style="bold cyan")
    tableau_regles.add_column("Extensions analysées et capturées", style="white")
    
    for categorie_dossier, liste_extensions in CONFIG_EXTENSIONS_DOSSIERS.items():
        if liste_extensions:
            tableau_regles.add_row(categorie_dossier, ", ".join(liste_extensions))
        else:
            tableau_regles.add_row(categorie_dossier, "[italic grey]Tous les formats non listés ci-dessus[/italic grey]")
            
    console_virtuelle.print(tableau_regles)
    console_virtuelle.print("\n[bold magenta]Appuyez sur Entrée pour retourner au menu principal...[/bold magenta]")
    input()


# ==============================================================================
# MENU PRINCIPAL (TABLEAU DE BORD)
# ==============================================================================
def menu_principal():
    """
    Boucle  pour guider l'utilisateur à travers le tableau de bord de l'application.
    """
    dossier_actif_selectionne = None
    
    while True:
        console_virtuelle.clear()
        
        statut_dossier_affichage = f"[bold green]{dossier_actif_selectionne}[/bold green]" if dossier_actif_selectionne else "[bold red]Aucun dossier sélectionné[/bold red]"
        statut_disponibilite_undo = "[bold green](Disponible)[/bold green]" if HISTORIQUE_DES_DEPLACEMENTS else "[bold red](Indisponible)[/bold red]"
        
        # Structure alignée proprement à gauche à l'intérieur du panel centré
        structure_menu_choix = (
            f"  [bold cyan]1.[/bold cyan] Choisir ou changer de dossier à nettoyer\n"
            f"  [bold cyan]2.[/bold cyan] Exécuter le tri automatique immédiat\n"
            f"  [bold cyan]3.[/bold cyan] Inspecter la liste des règles de filtrage\n"
            f"  [bold cyan]4.[/bold cyan] Annuler le dernier tri effectué {statut_disponibilite_undo}\n"
            f"  [bold cyan]5.[/bold cyan] Fermer l'application"
        )
        
        contenu_panel = (
            f"[bold blue]TABLEAU DE BORD - {NOM_APP}[/bold blue]\n\n"
            f"───────────────────────────────────────────────────────────\n"
            f"[white]Dossier actif :[/white] {statut_dossier_affichage}\n"
            f"───────────────────────────────────────────────────────────\n"
            f"{structure_menu_choix}"
        )
        
        # Utilisation d'une largeur fixe pour forcer le rectangle parfait
        console_virtuelle.print(Panel(
            Align.center(contenu_panel),
            border_style="cyan",
            padding=(1, 2),
            width=70
        ))
        
        identifiant_choix_utilisateur = IntPrompt.ask("[bold white]Entrez votre option[/bold white]", choices=['1', '2', '3', '4', '5'], default=1)
        
        if identifiant_choix_utilisateur == 1:
            dossier_actif_selectionne = configurer_dossier_cible()
        elif identifiant_choix_utilisateur == 2:
            if not dossier_actif_selectionne:
                console_virtuelle.print("\n[bold red]Erreur : Impossible de lancer le tri. Veuillez spécifier un dossier cible (Option 1).[/bold red]\n")
                time.sleep(2.5)
            else:
                executer_le_tri(dossier_actif_selectionne)
        elif identifiant_choix_utilisateur == 3:
            afficher_regles_actuelles()
        elif identifiant_choix_utilisateur == 4:
            annuler_dernier_tri()
        elif identifiant_choix_utilisateur == 5:
            console_virtuelle.clear()
            console_virtuelle.print(f"\n[bold green]Merci d'avoir utilisé {NOM_APP}[/bold green]\n")
            time.sleep(1)
            break


# ==============================================================================
# POINT D'ENTRÉE DU PROGRAMME
# ==============================================================================
if __name__ == "__main__":
    menu_principal()