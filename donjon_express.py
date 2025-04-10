#Projet : Jeu de simulation de donjon (mode texte) – "Aventure Express" 🏹🐉
#🧠 L’idée :

#Tu joues un aventurier qui entre dans un donjon. À chaque "salle", il se passe un événement aléatoire (trésor, piège, monstre, potion…). Tu dois survivre jusqu’à sortir du donjon ou mourir en essayant 😈
#🔧 Ce que tu vas pratiquer :

#✅ Fonctions
#✅ Boucles (while, for)
#✅ Listes et dictionnaires (inventaire, événements)
#✅ Conditions
#✅ Nouveauté : système de "jeu à étapes" avec événements aléatoires (random.choice)
#✅ Et un petit kiff narratif avec du texte qui change
#💡 Ce que le joueur peut vivre :

#    Commencer l’aventure (PV de départ, équipement de base)

#    Explorer une salle → événement aléatoire (ex : trouver une potion, tomber sur un monstre, piéger, gagner un objet…)

#    Prendre une décision → fuir, attaquer, utiliser un objet, etc.

#    Gérer un inventaire (liste d’objets simples à utiliser)

#    Gagner ou mourir

import random
import copy

evenements = [
    {"type": "monstre", "nom": "gobelin", "pv": 25, "force": 5},
    {"type": "monstre", "nom": "troll", "pv": 25, "force": 8},
    {"type": "monstre", "nom": "orc", "pv": 30, "force": 7},
    {"type": "potion", "nom": "potion", "soin": 5},
    {"type": "potion", "nom": "super potion", "soin": 15},
    {"type": "piege", "degats": 15},
    {"type": "tresor", "objet": "épée ancienne"},
    {"type": "tresor", "objet": "hache"},
    {"type": "tresor", "objet": "épée mystique"}
]

def afficher_stats(joueur):
    """fonction qui affiche les stats de depart du joueur"""
    print(f"  🧙 Bienvenue {joueur['nom']}")
    print(f"  ❤️  Points de vie : {joueur['pv']}")
    print("  🎒 Voici votre inventaire de départ: ")
    for objets in joueur["inventaire"]:
        print(f"    - {objets}")

def afficher_menu():
    print("\n🧭 Que voulez-vous faire ?")
    print("1. Explorer une salle")
    print("2. Consulter l'inventaire")
    print("3. Quitter le donjon")
    print("4. Afficher les armes")
    print("5. Utiliser une potion")


def generer_salle():
    salle = random.choice(evenements)
    return copy.deepcopy(salle)

def gerer_evenement(evenement, joueur):
    if evenement["type"] == "monstre":
        print(f"\nVous rencontrez un {evenement['nom']}")
        reponse_monstre = input("Voulez vous le combattre (A) ou fuir (B) ? ")
        if reponse_monstre.strip().upper() == "A":
            combat(joueur, evenement)

        if reponse_monstre.strip().upper() == "B":
            degats_fuite = random.randint(2, 8)
            print(f"\n⚠️ Vous fuyez... mais le monstre vous jette un sort avant de partir qui vous inflige {degats_fuite} pv !")
            joueur["pv"] -= degats_fuite
            print(f"\nIl vous reste {joueur['pv']} pv")

    elif evenement['type'] == "potion":
        print(f"\nVous touvez une {evenement['nom']}.")
        print(f"\nVous avez {joueur['pv']} pv.")
        reponse_potion = input(f"voulez vous utiliser cette potion qui vous soignera de {evenement['soin']} pv ? Oui (A) ou Non (B)")
        if reponse_potion.strip().upper() == "A":
            print(f"\nVous vous soignez de {evenement['soin']} pv")
            joueur["pv"] += evenement["soin"]
            print(f"\nVous avez maintenant {joueur['pv']} pv.")

        else:
            print("Cette potion a été rangée dans votre inventaire")
            joueur['inventaire'].append(evenement['nom'])

    elif evenement['type'] == "piege":
        print(f"\nMince, vous tombez sur un piège qui vous inflige {evenement['degats']} pv")
        joueur["pv"] -= evenement["degats"]
        print(f"\nIl vous reste {joueur['pv']} pv")

    elif evenement['type'] == "tresor":
        print(f"\nVous trouvez un trésor: {evenement['objet']}. Ce trésor a été ajouté a votre inventaire.")
        joueur['inventaire'].append(evenement['objet'])

    joueur["salles"] += 1
    print(f"\n📍 Salle {joueur['salles']}/10")

def calculer_degats(joueur):
    degats_armes = {
        "baton": 5,
        "arc": 10,
        "épée ancienne": 15,
        "hache": 30,
        "épée mystique": 20
    }
    return degats_armes[joueur["arme"]]

def utiliser_potion(joueur):

    potions_disponibles = ["potion", "super potion"]
    potions_inventaire = [objet for objet in joueur["inventaire"] if objet in potions_disponibles]
    print("\nVoici les potions disponibles dans votre inventaire :")
    for potion in potions_inventaire:
        print(f" - {potion}")
    choix = input("Quelle potion voulez vous utiliser ? ")
    if choix in potions_inventaire:
        soins = {
        "potion": 5,
        "super potion": 15
    }
        soin = soins[choix]
        joueur["pv"] += soin
        joueur["inventaire"].remove(choix)
        print(f"\n🧪 Vous vous êtes soigné de {soin} PV.")
        print("\n🔁 Retour au menu principal...\n")


def combat(joueur, monstre):
    print(f"\n⚔️  Combat contre un {monstre['nom']} ! Il a {monstre['pv']} PV.")
    while monstre['pv'] > 0 and joueur['pv'] > 0:
        degats = calculer_degats(joueur)
        monstre["pv"] -= degats
        print(f"🗡️  Vous infligez {degats} dégâts au {monstre['nom']} (il lui reste {monstre['pv']} PV)")
        if monstre["pv"] <= 0:
            print(f"\n✅ Vous avez vaincu le {monstre['nom']} !")
            break
        joueur["pv"] -= monstre["force"]
        print(f"\n💥 Le {monstre['nom']} vous inflige {monstre['force']} dégâts ! Il vous reste {joueur['pv']} PV\n")
        input("Appuyez sur Entrée pour continuer...\n")


def changer_arme(joueur):
    armes_disponibles = ["baton", "arc", "épée ancienne", "hache", "épée mystique"]
    armes_inventaire = [objet for objet in joueur["inventaire"] if objet in armes_disponibles]
    print(f"🗡️  Arme actuellement équipée : {joueur['arme']}")
    print("Voici les armes disponibles dans votre inventaire :")
    for arme in armes_inventaire:
        print(f" - {arme}")
    choix = input("Quelle arme voulez-vous équiper ? ")
    if choix in armes_inventaire:
        joueur["arme"] = choix
        print(f"Vous avez équipé {choix}.")
        print("🔁 Retour au menu principal...\n")

    else:
        print("Arme invalide.")

def afficher_intro():
    print("\n" + "="*50)
    print("🏰 BIENVENUE DANS DUNGEON QUEST 🏰")
    print("="*50)
    print("\nVous êtes un aventurier intrépide qui entre dans un donjon mystérieux.")
    print("Votre objectif est d’explorer 10 salles et de survivre aux dangers qui s’y trouvent.")
    print("\n🧩 Chaque salle peut contenir :")
    print("- Un monstre à combattre (ou fuir... à vos risques)")
    print("- Un piège douloureux")
    print("- Une potion de soin")
    print("- Un trésor contenant des armes puissantes\n")
    print("⚔️  Règle du jeu : Vous pouvez changer d’arme, utiliser des potions ou consulter votre inventaire à tout moment.")
    print("🏆 Atteignez la 10e salle pour gagner. Si vos PV tombent à 0, c'est la fin.\n")
    print("Bonne chance, héros...\n")
    input("Appuyez sur Entrée pour commencer votre aventure...")




def jouer():
    """fonction pricipale"""
    stats_joueur = {
        "nom": "",
        "pv": 100,
        "inventaire": ["baton", "bouclier", "potion", "arc"],
        "arme": "baton",
        "salles": 0
}
    afficher_intro()
    pseudo = input("Quel est le nom de votre aventurier ? ")
    stats_joueur["nom"] = pseudo
    afficher_stats(stats_joueur)
    print("Vous allez rentrer dans la première salle, Préparez vous !")
    while stats_joueur['pv'] > 0:
        afficher_menu()
        choix_menu = input(" ")
        if choix_menu == "1":
            evenement = generer_salle()
            gerer_evenement(evenement, stats_joueur)
            if stats_joueur["salles"] >= 10:
                print("🏆 Félicitations ! Vous avez atteint la salle finale et découvert le secret du donjon.")
                break

        if choix_menu == "2":
            afficher_stats(stats_joueur)
        if choix_menu == "3":
            print("Vous quittez le donjon")
            break
        if choix_menu == "4":
            changer_arme(stats_joueur)
        if choix_menu == "5":
            utiliser_potion(stats_joueur)
    if stats_joueur['pv'] <= 0:
        print("💀 Vous êtes mort dans le donjon. Reposez en paix, héros.")


jouer()
