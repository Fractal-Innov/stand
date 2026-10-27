# Cadrer la démarche SEO / GEO : préparation de la séance

Séance de travail à mener avec le rôle `/veilleur` (conseiller SEO/GEO). Préparée le 14/10/2026, le jour de l'atelier « IA SEO » (formation POLD x NeuillyLab). Notes de l'atelier dans Notion : Pilotage commercial > Dossiers > Atelier Formation POLD x NeuillyLab > « Atelier IA SEO ».

## Ce que l'atelier a dit (résumé des notes)

- **De la position à la précision.** On ne vise plus la première place sur un mot-clé, on vise d'être la réponse à une question précise posée à un assistant (qui peut aller chercher le 7e résultat Google).
- **Brave compte** : c'est le moteur de recherche dont se sert Claude. Une page en 404 n'y sort pas.
- **Quatre raisons pour lesquelles une IA ne vous cite pas :**
  1. elle ne peut pas vérifier qui vous êtes : toutes les sources externes doivent mener au site (LinkedIn est indexé et peut y renvoyer s'il est bien câblé) ;
  2. le contenu n'est pas structuré pour elle (données structurées JSON-LD) ;
  3. personne ne parle de vous ailleurs : des sources extérieures doivent confirmer le positionnement ;
  4. un concurrent occupe déjà la conversation.
- **Qualitatif avant quantitatif** : quelles questions les prospects se posent, et où y répondre (FAQ, article…).
- **Méthode de mesure** : poser de vraies questions d'acheteur aux cinq moteurs IA, lire si l'on est cité, ignoré ou remplacé par un concurrent. Score sur 100 de la structure des données, qui peut monter en quelques semaines.
- **Feuille de route AEO en 5 étapes** : mesure, autorité de marque, intelligence des requêtes (découvrir les questions des acheteurs), monitoring permanent. ⚠️ Les notes n'en nomment que quatre : retrouver la cinquième.

### La requête test, apportée par le binôme de l'atelier

> Bonjour, je recherche une société qui peut me permettre de faire des représentations 3D de ce que font nos machines industrielles, qui sont trop grosses pour être déplacées sur des salons.

C'est mot pour mot la douleur n° 1 de `VENTE.md` (« le produit est absent »). Elle sert de première question de mesure.

## Ce qui existe déjà (constaté dans les dépôts le 14/10)

| Sujet | État |
| --- | --- |
| Robots | `robots.txt` (dépôt agence) autorise tous les robots, y compris GPTBot, ClaudeBot, PerplexityBot, Google-Extended. |
| Sitemap | `sitemap.xml` (dépôt agence) : `/stand/` en `lastmod 2026-09-30`, alors que la page a changé jusqu'au 08/10. Il liste encore Midipile, Rayon X, Moulage, Village. |
| Données structurées | `/stand/` porte `WebSite`, `Service`, `Person`, `PostalAddress`, zones servies. **Pas de `FAQPage`**, alors que la page a six questions de FAQ (en `h3`). Pas d'`Organization` distincte à vérifier. |
| Fichiers de travail | `VENTE.md`, `docs/` répondent 404 volontairement (liste blanche du workflow). |
| `llms.txt` | Absent. |
| Indexation | `/stand/` indexée (Search Console, 30/09), PageSpeed mobile 99 / 94. |
| Sources externes | À recenser : LinkedIn (page entreprise, profils de Corentin et d'Hugo Daniel), fiche Google, annuaires, Catalyseur, NeuillyLab, partenaires. |

## Déroulé proposé (environ 1 h 30)

1. **Mesure de départ (30 min).** Écrire 8 à 10 questions d'acheteur à partir des douleurs entendues (Rééduca, Greentech, rendez-vous du 12/10), la requête du binôme en tête. Les poser à ChatGPT, Claude, Perplexity, Gemini et Copilot. Noter pour chacune : cité, ignoré, ou concurrent cité (lequel).
2. **Identité vérifiable (20 min).** Recenser les sources externes et vérifier que chacune renvoie à `fractal-innov.fr/stand/` avec le même nom et la même description.
3. **Structure (20 min).** Lister les correctifs de données : `FAQPage`, `Organization`, `lastmod` du sitemap, `llms.txt`, place des autres démos dans le sitemap après le pivot.
4. **Questions des acheteurs (15 min).** Choisir celles qui manquent à la page et où leur répondre (FAQ, section, article).
5. **Suivi (5 min).** Fréquence de la mesure (refaire les mêmes questions toutes les deux semaines ?) et endroit où la noter.

## Questions à trancher au début de la séance

Une à la fois, en options :

- **Périmètre** : `/stand/` seule, ou tout `fractal-innov.fr` (les autres démos comme preuves de savoir-faire) ?
- **Outil de mesure** : à la main dans les cinq moteurs, ou l'outil de score présenté à l'atelier ?
- **Ordre avec la piste « discours de vente »** (`docs/pistes-landing.md`, piste a) : les nouvelles questions de FAQ dépendent de ce que la page doit vendre (kit de salon, ou essai qualifié avec version en ligne).
- **Sources externes** : lesquelles existent déjà, lesquelles créer (et qui les tient).

## Garde-fous

- Toute réponse ajoutée à la page reste fidèle à l'offre (`CLAUDE.md`, `VENTE.md`) : pas de prix, pas de délai, écran non fourni, pas de nom produit.
- Aucun nom de client ou de prospect dans un contenu public, ni dans une question posée aux moteurs.
- Rédaction sans tiret cadratin et sans tournures « IA ».
