#!/usr/bin/env python3
"""Vérifie un message de prospection lu sur l'entrée standard.

Usage : check.py {connexion|suivi|email|relance} < message.txt
Pour un e-mail ou une relance, la première ligne peut être « Objet : ... ».
Code de sortie 1 s'il reste une ERREUR.
"""
import re
import sys

LIMITES = {  # (unité, maximum) pour le corps
    "connexion": ("car", 200),
    "suivi": ("car", 600),
    "email": ("mots", 90),
    "relance": ("mots", 70),
}
OBJET_MAX = 50
SIGNATURE = re.compile(r"\n\s*Hugo Daniel\s*\n.*\Z", re.S)

INTERDITS = [  # (motif, raison) ; motifs insensibles à la casse sauf préfixe (?-i:...)
    (r"—", "tiret cadratin : utiliser « : », « , », « . » ou des parenthèses"),
    (r"(?-i:\bSTAND\b)", "nom produit interne : dire « le démonstrateur 3D de votre stand »"),
    (r"€|\beuros?\b|(?-i:\bHT\b|\bTTC\b)|\btarifs?\b|\bprix\b", "prix : aucun prix ni fourchette"),
    (r"\b\d+\s*(semaines?|jours ouvrés|mois)\b", "délai : aucun délai annoncé"),
    (r"\bexpert|\bleader\b|\binnovant|\brévolution", "ton non humble"),
    (r"je me permets|je vois que vous êtes|j'espère que vous allez bien|n'hésitez pas|suite à mon précédent", "formule de message de masse"),
]
APPEL = r"calendar\.app\.google|\bappel\b|\bcall\b|\bvisio\b|\bcréneau|\bminutes? de votre"
LIEN = r"https?://"


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in LIMITES:
        sys.exit(f"usage : check.py {{{'|'.join(LIMITES)}}} < message")
    genre = sys.argv[1]
    texte = sys.stdin.read().strip()
    erreurs, avertissements = [], []

    objet = None
    m = re.match(r"Objet\s*:\s*(.*)\n", texte)
    if m:
        objet, texte = m.group(1).strip(), texte[m.end():].strip()
    corps = SIGNATURE.sub("", texte).strip()

    unite, maximum = LIMITES[genre]
    taille = len(texte) if unite == "car" else len(re.findall(r"\b\w[\w'’-]*", corps))
    if taille > maximum:
        erreurs.append(f"trop long : {taille}/{maximum} {unite}")

    if genre == "email":
        if objet is None:
            erreurs.append("Objet manquant (première ligne « Objet : ... »)")
        elif len(objet) > OBJET_MAX:
            erreurs.append(f"Objet trop long : {len(objet)}/{OBJET_MAX} car.")

    for motif, raison in INTERDITS:
        trouve = re.search(motif, texte, re.I)
        if trouve:
            erreurs.append(f"« {trouve.group(0)} » : {raison}")

    if genre in ("connexion", "email") and re.search(APPEL, corps, re.I):
        erreurs.append("demande d'appel ou lien calendrier dans un premier message")
    if genre == "connexion" and re.search(LIEN, texte):
        erreurs.append("lien dans une demande de connexion")
    if genre != "connexion" and "?" not in corps:
        erreurs.append("aucune question : finir par une question ouverte (ou la proposition d'appel)")
    if genre == "suivi" and re.search(APPEL, corps, re.I):
        avertissements.append("appel proposé dans le suivi : seulement si la fiche montre un intérêt explicite")
    if corps.count("?") > 2:
        avertissements.append("plus de deux questions : en garder une")

    print(f"Longueur : {taille}/{maximum} {unite}" + (f" · objet {len(objet)}/{OBJET_MAX} car." if objet else ""))
    for e in erreurs:
        print("ERREUR", e)
    for a in avertissements:
        print("AVERTISSEMENT", a)
    print("OK" if not erreurs else "À CORRIGER")
    sys.exit(1 if erreurs else 0)


if __name__ == "__main__":
    main()
