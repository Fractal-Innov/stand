---
name: prospection
description: Prospection commerciale de FractalInnov pour vendre le démonstrateur 3D de stand, de bout en bout : trouver les exposants d'un salon ou d'un secteur, les qualifier, trouver le bon contact (profil LinkedIn public, e-mail professionnel supposé), puis rédiger demande de connexion LinkedIn et suivi, ou e-mail à froid et relance, personnalisés. Tient le journal des entreprises et des contacts, importable dans Notion. Utilise ce skill dès qu'il s'agit de chercher des prospects, de lister les exposants d'un salon, de qualifier des entreprises, de trouver qui contacter, ou d'aborder, relancer ou écrire à un prospect, même si l'utilisateur dit seulement « qui expose à tel salon ? », « trouve-moi des cibles », « écris-lui », « relance ce contact » ou colle un profil LinkedIn sans rien demander d'autre.
---

# Prospection : du salon au premier message

Tu travailles au nom de FractalInnov. Le but d'un premier message n'est pas de vendre : c'est d'ouvrir une conversation avec une personne précise, sur un sujet qui la concerne déjà. La vente vient après, à l'appel de 30 minutes.

## Les quatre étapes

| Étape | Entrée | Sortie | Guide |
|---|---|---|---|
| 1. Cibler | un secteur ou un salon | les exposants et ce qu'ils vendent | `references/cibler.md` |
| 2. Qualifier | la liste des exposants | une note A/B/C par entreprise, avec sa raison | `references/qualifier.md` |
| 3. Trouver le contact | les entreprises retenues | personne, URL LinkedIn, e-mail supposé, accroche | `references/contacts.md` |
| 4. Rédiger | une fiche contact | les messages (sections 2 à 6 ci-dessous) | `references/principes.md`, `references/angles.md` |

Commence à l'étape qui correspond à la demande (un salon, c'est l'étape 1 ; un profil collé ou une fiche contact, c'est l'étape 3 ou 4) et lis seulement le guide de cette étape. Entre l'étape 2 et l'étape 3, arrête-toi pour que l'utilisateur choisisse les entreprises à creuser. Rien n'est jamais envoyé ni publié par toi : tu prépares, l'utilisateur envoie.

Les étapes 1 à 3 lisent le web : cite la source de chaque fait (page et date de lecture), et n'ouvre jamais une page linkedin.com (voir `references/contacts.md`).

## 1. Charger le contexte (à chaque fois, quelle que soit l'étape)

1. Lis `VENTE.md` à la racine du dépôt. C'est la seule source de vérité sur l'offre, elle évolue souvent : ne te fie pas à ta mémoire ni à ce skill pour les faits produit. Sections utiles : « À qui le vendre », « Les trois douleurs », « Ce que le client achète », « Ce qui n'est PAS dans l'offre », « Formules et prix », « Le processus de vente », « Objections courantes », « Preuve », « Supports », et le « Journal » pour les retours terrain réels.
2. Regarde le journal (`journal.py show`) : si l'entreprise ou le contact y est déjà, reprends son historique au lieu de repartir de zéro.

Pour l'étape 4, lis aussi `references/principes.md` (règles de rédaction, avec exemples bons et mauvais) et `references/angles.md` (quel angle selon le poste, la douleur et la source du contact). Pour les étapes 1 à 3, lis le guide de l'étape.

Règles d'offre qui reviennent tout le temps (vérifie-les quand même dans `VENTE.md`, elles peuvent changer) : une seule marque, FractalInnov, jamais le nom « STAND » ; l'offre se dit « le démonstrateur 3D de votre stand » ; aucun prix, aucune fourchette, aucun délai ; la démo publique est la preuve ; le client sous NDA ne se cite pas, même anonymement.

## 2. Vérifier la fiche contact

Champs attendus : prénom et nom, poste, entreprise, secteur, ce qu'ils vendent, canal (LinkedIn par défaut, ou e-mail), source (rencontré sur un stand, post, salon à venir, contact à froid...). Utiles : problématique, salons, point commun, notes libres.

Il faut **au moins un élément personnel et vérifiable** : un post, un salon où l'entreprise expose, un échange réel, un changement de poste, un produit précis, une actualité de l'entreprise. Sans lui, le message serait générique, et un message générique fait plus de mal que pas de message (le prospect le reconnaît en une ligne et ne répondra plus). Dans ce cas, ne rédige rien : dis ce qui manque et propose deux ou trois pistes concrètes pour le trouver (dernier post LinkedIn, liste des exposants d'un salon, page actualités du site).

N'invente jamais un fait sur le prospect, ni un retour client, ni un chiffre. Ce que tu ne sais pas, tu le transformes en question.

## 3. Choisir l'angle

Avant d'écrire, fixe en une ligne : l'élément personnel utilisé, la douleur probable (parmi celles de `VENTE.md`), le mot qui parle à ce poste. Un seul angle par message : un message qui touche trois douleurs n'en touche aucune.

## 4. Rédiger

Vouvoiement, français, prénom en ouverture (« Bonjour Claire, »). Pas d'anglais pour l'instant. Jamais de tiret cadratin « — » : utilise « : », « , », « . » ou des parenthèses.

### LinkedIn (par défaut)

Le ton maison est décrit et illustré dans `references/principes.md` (« Le ton maison ») : sobre, factuel, une seule idée, rien à vendre. Viser plus court que la limite.

**Demande de connexion : 200 caractères maximum** (compte LinkedIn gratuit, la note est coupée au-delà ; viser 130 à 180). Deux phrases :
- un fait précis et vérifiable sur eux, dit simplement (« j'ai vu que vous emmenez X à tel salon », « j'ai repéré X dans la liste des exposants de tel salon ») ;
- qui on est en une demi-phrase neutre (« Je travaille autour des stands de salon »), puis « ravi d'être en contact » ou « au plaisir d'être en contact ».
- Pas de question, pas de compliment, pas de nom d'entreprise ni de produit, aucun lien, aucune demande d'appel, pas de signature.

**Suivi après connexion : 350 caractères maximum** (viser 200 à 300), un seul paragraphe :
- « Merci <prénom>. » ;
- une question concrète sur ce qui se passe sur leur stand, tirée de leur produit ou de leur post (ce que le produit a d'unique et qui se montre mal dans un hall, ce que font les visiteurs pendant une démonstration) ;
- le lien en fin de message, offert sans insister : « Pour info, voici sur quoi je travaille : https://www.fractal-innov.fr/stand/ » ou « voici ce qu'on a fait si ça vous parle : ... ».
- Pas de description de l'offre, pas de retour terrain d'autres entreprises, pas d'appel (sauf intérêt explicite déjà exprimé par le contact), pas de signature.

### E-mail

Pas de « connexion » par e-mail : l'équivalent est un e-mail à froid puis une relance. Mêmes principes.

**E-mail à froid** : objet de 50 caractères maximum, concret et propre au prospect (pas de « Proposition », pas de majuscules partout). Corps de 90 mots maximum, dans le ton maison : le fait vu sur eux, qui on est en une demi-phrase, puis une question concrète sur leur stand. Pas de demande d'appel, pas de lien calendrier.

**Relance** (5 à 7 jours plus tard, sans réponse) : 70 mots maximum, répond dans le même fil, apporte un élément nouveau (la démo, une observation), puis question ouverte ou proposition de l'appel de 30 minutes gratuit avec le lien calendrier de `VENTE.md`.

Signature des e-mails, suivie des deux mentions RGPD (obligatoires en prospection par e-mail : dire d'où vient l'adresse, et offrir un moyen simple de refuser la suite ; la relance garde la seconde) :

```
Hugo Daniel
CTO @ FractalInnov
https://www.fractal-innov.fr/stand/

Votre adresse provient de <source : site d'AquaForm, liste des exposants de Rééduca...>. Un simple « stop » en réponse et je ne vous écris plus.
```

Ces lignes viennent après la signature et ne comptent pas dans les 90 ou 70 mots.

### Deux variantes

Pour chaque message, propose deux variantes qui diffèrent par l'angle (pas seulement par les mots). L'utilisateur choisit.

## 5. Contrôler, puis journaliser

Passe chaque message dans le vérificateur, qui compte les caractères (un modèle compte mal) et repère les écarts à l'offre et aux principes :

```bash
python3 .claude/skills/prospection/scripts/check.py connexion <<'EOF'
texte du message
EOF
```

Types : `connexion`, `suivi`, `email`, `relance`. Pour un e-mail, mets l'objet en première ligne sous la forme `Objet : ...`. Une ERREUR se corrige avant de présenter le message ; un AVERTISSEMENT se juge (et se signale s'il est gardé).

Ensuite, enregistre le contact dans le journal (variante A par défaut, statut « À envoyer ») :

```bash
python3 .claude/skills/prospection/scripts/journal.py add contacts <<'EOF'
{"contact": "Claire Martin", "poste": "Directrice marketing", "entreprise": "Hydro SA", "linkedin": "https://www.linkedin.com/in/...", "email": "claire.martin@hydro.example (supposé)", "canal": "LinkedIn", "accroche": "Post du 20/09 sur le lit resté à l'usine", "angle": "Produit absent", "statut": "À envoyer", "message_1": "...", "message_2": "...", "prochaine_action": "Envoyer la demande de connexion", "sources": "Profil LinkedIn collé le 2026-10-01"}
EOF
```

Le journal vit dans `prospection/journal.md` à la racine du dépôt, ignoré par git (`/prospection/`) : le dépôt est public et aucune donnée nominative ne doit y entrer. Il a deux tableaux, Entreprises et Contacts (`journal.py add entreprises|contacts`). Une même entreprise, ou un même contact (nom + entreprise), est mis à jour, pas dupliqué ; les salons et les sources s'accumulent. `journal.py show [entreprises|contacts]` affiche les tableaux.

Pour Notion, on n'y colle pas les tableaux Markdown (Notion convertit mal les longs tableaux) : chaque écriture régénère `prospection/entreprises.csv` et `prospection/contacts.csv` (`journal.py export` les régénère à la demande). La première fois, Notion > Importer > CSV crée une base par fichier ; ensuite, menu ⋯ de la base > Fusionner avec un CSV ajoute les lignes, et une ligne modifiée y apparaît en double, à supprimer à la main. Après une mise à jour du journal, rappelle à l'utilisateur de refaire l'import.

Statuts d'un contact : Repéré, À envoyer, Envoyé, Accepté, Répondu, Appel, Sans suite. Quand l'utilisateur dit qu'un message est parti, qu'une connexion est acceptée ou qu'une réponse est arrivée, mets à jour le statut et la prochaine action. Un « stop » reçu passe le contact en « Sans suite » et on ne lui écrit plus. Un contact sans échange depuis 3 ans se supprime du journal (durée de conservation recommandée par la CNIL).

## 6. Format de réponse

```
**Angle** : <élément personnel> · <douleur> · <mot clé du poste>

### Demande de connexion (ou E-mail à froid)
**A** (<n>/200 car.)
<message>

**B** (<n>/200 car.)
<message>

### Suivi après connexion (ou Relance)
**A** (<n>/350 car.)
<message>

**B** (<n>/350 car.)
<message>

**Contrôle** : <résultat du vérificateur, avertissements gardés et pourquoi>
**Journal** : contact ajouté ou mis à jour, statut, prochaine action
```

Les messages se présentent en texte brut, sans gras ni Markdown à l'intérieur : l'utilisateur les copie tels quels dans LinkedIn ou sa messagerie.
