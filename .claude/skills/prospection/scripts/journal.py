#!/usr/bin/env python3
"""Journal de prospection : deux tableaux Markdown (Entreprises, Contacts), exportés en CSV pour Notion.

Usage :
  journal.py add {entreprises|contacts} [--journal CHEMIN] < ligne.json   ajoute, ou met à jour la ligne de même clé
  journal.py show [entreprises|contacts] [--journal CHEMIN]              affiche un tableau, ou les deux
  journal.py export [--journal CHEMIN]                                   régénère entreprises.csv et contacts.csv

Chemin par défaut : <racine du dépôt>/prospection/journal.md (ignoré par git : dépôt public).
Clé : l'entreprise pour Entreprises, le contact + l'entreprise pour Contacts.
Les champs absents du JSON gardent leur valeur ; « salons » et « sources » s'accumulent ;
« mis_a_jour » prend la date du jour (sert à la durée de conservation RGPD).
Chaque écriture régénère aussi entreprises.csv et contacts.csv à côté du journal
(UTF-8 avec BOM, pour les accents) : c'est ce fichier qu'on importe dans Notion.
"""
import argparse
import csv
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

TABLES = {
    "entreprises": {
        "titre": "Entreprises",
        "colonnes": [
            ("mis_a_jour", "Mis à jour"), ("entreprise", "Entreprise"), ("site", "Site"),
            ("secteur", "Secteur"), ("produit", "Produit"), ("salons", "Salons (stand)"),
            ("note", "Note"), ("raison", "Raison"), ("statut", "Statut"), ("sources", "Sources"),
        ],
        "cle": ["entreprise"],
    },
    "contacts": {
        "titre": "Contacts",
        "colonnes": [
            ("mis_a_jour", "Mis à jour"), ("contact", "Contact"), ("poste", "Poste"),
            ("entreprise", "Entreprise"), ("linkedin", "LinkedIn"), ("email", "E-mail"),
            ("canal", "Canal"), ("accroche", "Accroche"), ("angle", "Angle"), ("statut", "Statut"),
            ("message_1", "Connexion / e-mail"), ("message_2", "Suivi / relance"),
            ("prochaine_action", "Prochaine action"), ("sources", "Sources"),
        ],
        "cle": ["contact", "entreprise"],
    },
}
CUMULES = {"salons", "sources"}
ENTETE = "# Journal de prospection\n\nPour Notion, importer entreprises.csv et contacts.csv (même dossier). Fichier local, jamais commité. Supprimer un contact 3 ans après le dernier échange (RGPD).\n"


def chemin_par_defaut():
    racine = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    return Path(racine or ".") / "prospection" / "journal.md"


def cellule(valeur):
    # Une cellule Markdown tient sur une ligne et ne contient pas de « | ».
    return " ".join(str(valeur or "").split()).replace("|", "/")


def lire(chemin):
    """Renvoie {table: [lignes]} en lisant chaque tableau sous son titre « ## ... »."""
    donnees = {nom: [] for nom in TABLES}
    if not chemin.exists():
        return donnees
    par_titre = {t["titre"]: nom for nom, t in TABLES.items()}
    courant = None
    for ligne in chemin.read_text().splitlines():
        m = re.match(r"## (.+)", ligne)
        if m:
            courant = par_titre.get(m.group(1).strip())
        elif courant and ligne.startswith("|") and not ligne.startswith("|---"):
            valeurs = [v.strip() for v in ligne.strip().strip("|").split("|")]
            colonnes = TABLES[courant]["colonnes"]
            if valeurs != [titre for _, titre in colonnes]:
                donnees[courant].append(dict(zip((c for c, _ in colonnes), valeurs)))
    return donnees


def tableau(nom, lignes):
    colonnes = TABLES[nom]["colonnes"]
    sortie = [f"## {TABLES[nom]['titre']}", "", "| " + " | ".join(t for _, t in colonnes) + " |", "|" + "---|" * len(colonnes)]
    sortie += ["| " + " | ".join(cellule(l.get(c)) for c, _ in colonnes) + " |" for l in lignes]
    return "\n".join(sortie)


def exporter(chemin, donnees):
    """Un CSV par table, à côté du journal : Notion l'importe en base de données."""
    for nom, table in TABLES.items():
        with open(chemin.parent / f"{nom}.csv", "w", newline="", encoding="utf-8-sig") as f:
            ecrivain = csv.writer(f)
            ecrivain.writerow(t for _, t in table["colonnes"])
            ecrivain.writerows([l.get(c, "") for c, _ in table["colonnes"]] for l in donnees[nom])


def ecrire(chemin, donnees):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(ENTETE + "".join("\n" + tableau(nom, donnees[nom]) + "\n" for nom in TABLES))
    exporter(chemin, donnees)


def cumuler(ancien, nouveau):
    morceaux = [m.strip() for m in f"{ancien or ''};{nouveau or ''}".split(";") if m.strip()]
    return " ; ".join(dict.fromkeys(morceaux))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=["add", "show", "export"])
    p.add_argument("table", nargs="?", choices=list(TABLES))
    p.add_argument("--journal", type=Path, default=None)
    args = p.parse_args()
    chemin = args.journal or chemin_par_defaut()
    donnees = lire(chemin)

    if args.action == "show":
        noms = [args.table] if args.table else list(TABLES)
        print(ENTETE + "".join("\n" + tableau(n, donnees[n]) + "\n" for n in noms))
        return

    if args.action == "export":
        exporter(chemin, donnees)
        print(f"CSV : {chemin.parent / 'entreprises.csv'}, {chemin.parent / 'contacts.csv'}")
        return

    if not args.table:
        sys.exit("préciser la table : entreprises ou contacts")
    nom, table = args.table, TABLES[args.table]
    cles = [c for c, _ in table["colonnes"]]
    nouveau = json.loads(sys.stdin.read(), strict=False)  # tolère les retours à la ligne bruts
    inconnus = set(nouveau) - set(cles)
    if inconnus:
        sys.exit(f"champs inconnus : {', '.join(sorted(inconnus))} (attendus : {', '.join(cles)})")
    if not all(nouveau.get(k) for k in table["cle"]):
        sys.exit(f"champs obligatoires : {', '.join(table['cle'])}")
    nouveau["mis_a_jour"] = datetime.date.today().isoformat()

    identifiant = lambda l: tuple(cellule(l.get(k)).lower() for k in table["cle"])
    existant = next((l for l in donnees[nom] if identifiant(l) == identifiant(nouveau)), None)
    if existant:
        for k, v in nouveau.items():
            if v and k not in table["cle"]:  # la clé garde son orthographe d'origine
                existant[k] = cumuler(existant.get(k), v) if k in CUMULES else v
        print(f"{table['titre']} : mis à jour {' / '.join(nouveau[k] for k in table['cle'])}")
    else:
        donnees[nom].append(nouveau)
        print(f"{table['titre']} : ajouté {' / '.join(nouveau[k] for k in table['cle'])}")
    ecrire(chemin, donnees)
    print(f"Journal : {chemin}")


if __name__ == "__main__":
    main()
