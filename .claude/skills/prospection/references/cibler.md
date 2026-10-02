# Étape 1 : cibler (secteur ou salon, puis liste d'exposants)

But : partir d'un secteur ou d'un nom de salon et sortir la liste des entreprises qui exposent, avec ce qu'elles vendent. Une liste d'exposants est la meilleure source de prospects : chaque entreprise paie déjà un stand, et le salon fournit une accroche datée et vérifiable.

## Trouver le salon

- **Nom de salon donné** : trouve son site officiel (recherche web), puis note dates, lieu et organisateur. Si plusieurs salons portent un nom proche, ou si le nom ne correspond à aucun salon, arrête-toi : présente les candidats (nom exact, dates, lieu, édition passée ou à venir) et laisse l'utilisateur choisir. Une liste d'exposants du mauvais salon fait perdre plus de temps qu'une question.
- **Secteur donné** : cherche les salons du secteur en France dans les 12 prochains mois (« salon <secteur> 2027 exposants », annuaires de salons, sites des fédérations professionnelles). Propose 3 à 5 salons avec dates et lieu, puis laisse l'utilisateur choisir avant d'aller plus loin.

Un salon passé reste utile : sa liste d'exposants reste souvent en ligne et l'édition suivante est une accroche (« vous y retournez en <année> ? »).

## Récupérer la liste des exposants

Où chercher, dans l'ordre :

1. La page « Exposants », « Liste des exposants », « Annuaire » ou « Catalogue » du site du salon.
2. Le plan du salon en PDF (souvent nom et numéro de stand).
3. Les communiqués des exposants (« retrouvez-nous stand B12 à ... ») via une recherche web sur le nom du salon.
4. L'édition précédente, si la liste de l'édition à venir n'est pas encore publiée. Dans ce cas, la présence à la prochaine édition n'est pas acquise : note l'année de la liste dans `salons` (« Rééduca 2025, exposant ») et mets « présence 2026 confirmée » seulement si une source le dit (communiqué, page de l'exposant). Les messages en tiendront compte.

Beaucoup de listes sont des pages dynamiques que la lecture de page ne voit pas. Si la page revient vide ou incomplète : cherche une version PDF ou une page par exposant. Sinon, demande à l'utilisateur d'ouvrir la page dans son navigateur et de coller le texte (Ctrl+A, Ctrl+C). N'invente jamais un exposant pour compléter la liste.

## Ce qu'on garde

Pour chaque exposant : nom, numéro de stand si connu, site web, une ligne sur ce qu'il vend. Écarte d'emblée ceux qui ne sont manifestement pas des cibles (organismes de formation, presse, associations, assurances, revendeurs sans produit propre) et dis combien ont été écartés et pourquoi, en une ligne.

Au-delà de 40 exposants, ne lis pas tous les sites : fais un premier tri sur la ligne de description, puis qualifie seulement les plausibles.

Enregistre chaque exposant retenu dans la table Entreprises, statut « Repéré » :

```bash
python3 .claude/skills/prospection/scripts/journal.py add entreprises <<'EOF'
{"entreprise": "AquaForm", "site": "https://aquaform.example", "secteur": "Balnéothérapie", "produit": "Lits et baignoires de balnéothérapie", "salons": "Rééduca 2026 (B12)", "statut": "Repéré", "sources": "Liste des exposants, site du salon, consultée le 2026-10-01"}
EOF
```

Dans `sources`, une entrée par page lue, citée une seule fois (URL et date de lecture) : les étapes suivantes n'ajoutent que les pages nouvelles.

Puis passe à l'étape 2 (`qualifier.md`) dans la foulée : la liste brute sans tri n'aide pas l'utilisateur.
