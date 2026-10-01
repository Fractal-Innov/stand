#!/usr/bin/env python3
"""Journal des prospects : un tableau Markdown à coller dans Notion.

Usage :
  journal.py add  [--journal CHEMIN] < contact.json   ajoute, ou met à jour le contact (même nom + entreprise)
  journal.py show [--journal CHEMIN]                  affiche le tableau

Chemin par défaut : <racine du dépôt>/.prospection/journal.md (ignoré par git : dépôt public).
Les champs absents du JSON gardent leur valeur précédente ; la date est celle du jour.
"""
import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path

COLONNES = [
    ("date", "Date"),
    ("contact", "Contact"),
    ("poste", "Poste"),
    ("entreprise", "Entreprise"),
    ("secteur", "Secteur"),
    ("canal", "Canal"),
    ("source", "Source"),
    ("accroche", "Accroche"),
    ("angle", "Angle"),
    ("statut", "Statut"),
    ("message_1", "Connexion / e-mail"),
    ("message_2", "Suivi / relance"),
    ("prochaine_action", "Prochaine action"),
]
CLES = [c for c, _ in COLONNES]
TITRE = "# Journal des prospects\n\nÀ coller dans Notion. Fichier local, jamais commité.\n\n"


def chemin_par_defaut():
    racine = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    return Path(racine or ".") / ".prospection" / "journal.md"


def cellule(valeur):
    # Une cellule Markdown tient sur une ligne et ne contient pas de « | ».
    return " ".join(str(valeur or "").split()).replace("|", "/")


def lire(chemin):
    lignes = []
    if chemin.exists():
        for ligne in chemin.read_text().splitlines():
            if ligne.startswith("|") and not ligne.startswith("|---"):
                valeurs = [v.strip() for v in ligne.strip().strip("|").split("|")]
                if valeurs != [titre for _, titre in COLONNES]:
                    lignes.append(dict(zip(CLES, valeurs)))
    return lignes


def ecrire(chemin, lignes):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    tableau = ["| " + " | ".join(t for _, t in COLONNES) + " |", "|" + "---|" * len(COLONNES)]
    tableau += ["| " + " | ".join(cellule(l.get(c)) for c in CLES) + " |" for l in lignes]
    chemin.write_text(TITRE + "\n".join(tableau) + "\n")


def meme_contact(a, b):
    cle = lambda l: (cellule(l.get("contact")).lower(), cellule(l.get("entreprise")).lower())
    return cle(a) == cle(b)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=["add", "show"])
    p.add_argument("--journal", type=Path, default=None)
    args = p.parse_args()
    chemin = args.journal or chemin_par_defaut()
    lignes = lire(chemin)

    if args.action == "add":
        nouveau = json.loads(sys.stdin.read(), strict=False)  # tolère les retours à la ligne bruts
        inconnus = set(nouveau) - set(CLES)
        if inconnus:
            sys.exit(f"champs inconnus : {', '.join(sorted(inconnus))} (attendus : {', '.join(CLES)})")
        if not nouveau.get("contact") or not nouveau.get("entreprise"):
            sys.exit("« contact » et « entreprise » sont obligatoires")
        nouveau["date"] = nouveau.get("date") or datetime.date.today().isoformat()
        existant = next((l for l in lignes if meme_contact(l, nouveau)), None)
        if existant:
            existant.update({k: v for k, v in nouveau.items() if v})
            print(f"Mis à jour : {nouveau['contact']} ({nouveau['entreprise']})")
        else:
            lignes.append(nouveau)
            print(f"Ajouté : {nouveau['contact']} ({nouveau['entreprise']})")
        ecrire(chemin, lignes)
        print(f"Journal : {chemin}")
    else:
        print(chemin.read_text() if chemin.exists() else f"Journal vide ({chemin})")


if __name__ == "__main__":
    main()
