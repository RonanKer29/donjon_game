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

evenements = [
    {"type": "monstre", "nom": "gobelin", "degats": 10}, {"type": "potion", "soin": 5},
    {"type": "piege", "degats": 15}, {"type": "tresor", "objet": "épée ancienne"}
]

def afficher_stats(joueur):
    """fonction qui affiche les stats de depart du joueur"""
    print(f"  🧙 Bienvenue {joueur['nom']}")
    print(f"  ❤️  Points de vie : {joueur['pv']}")
    print("  🎒 Inventaire: ")
    for objets in joueur["inventaire"]:
        print(f"    - {objets}")

def generer_salle():
    salle = random.choice(evenements)
    return salle


def jouer():
    """fonction pricipale"""
    stats_joueur = {
        "nom": "",
        "pv": 100,
        "inventaire" : ["baton", "bouclier", "potion"]
}
    pseudo = input("Quel est le nom de votre aventurier ? ")
    stats_joueur["nom"] = pseudo
    afficher_stats(stats_joueur)
    evenement = generer_salle()
    if evenement["type"] == "monstre":
        print(f"Vous rencontrez un {evenement['nom']} qui vous inflige {evenement['degats']} pv")
    if evenement['type'] == "potion":
        print(f"Vous vous soignez de {evenement['soin']} pv")
    if evenement['type'] == "piege":
        print(f"Vous tombez sur un piège qui vous inflige {evenement['degats']} pv")
    if evenement['type'] == "tresor":
        print(f"Vous trouvez un trésor: {evenement['objet']}")
jouer()
