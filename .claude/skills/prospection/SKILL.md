---
name: prospection
description: Rédige les messages de prospection commerciale de FractalInnov pour vendre le démonstrateur 3D de stand : demande de connexion LinkedIn et message de suivi, ou e-mail à froid et relance, personnalisés à partir d'une fiche contact (secteur, poste, produit vendu, problématique, salons). Tient aussi le journal des prospects, copiable dans Notion. Utilise ce skill dès qu'il s'agit d'aborder, relancer ou écrire à un prospect, un exposant, un contact de salon ou un décideur repéré sur LinkedIn, même si l'utilisateur dit seulement « écris-lui », « relance ce contact », « prépare une approche » ou colle un profil sans rien demander d'autre.
---

# Prospection : messages LinkedIn et e-mail

Tu écris au nom de FractalInnov. Le but d'un premier message n'est pas de vendre : c'est d'ouvrir une conversation avec une personne précise, sur un sujet qui la concerne déjà. La vente vient après, à l'appel de 30 minutes.

## 1. Charger le contexte (à chaque fois)

1. Lis `VENTE.md` à la racine du dépôt. C'est la seule source de vérité sur l'offre, elle évolue souvent : ne te fie pas à ta mémoire ni à ce skill pour les faits produit. Sections utiles : « À qui le vendre », « Les trois douleurs », « Ce que le client achète », « Ce qui n'est PAS dans l'offre », « Formules et prix », « Le processus de vente », « Objections courantes », « Preuve », « Supports », et le « Journal » pour les retours terrain réels.
2. Lis `references/principes.md` (règles de rédaction, avec exemples bons et mauvais).
3. Lis `references/angles.md` (quel angle selon le poste, la douleur et la source du contact).
4. Regarde le journal des prospects (section 5) : si le contact y est déjà, reprends son historique au lieu de repartir de zéro.

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

**Demande de connexion : 200 caractères maximum** (compte LinkedIn gratuit, la note est coupée au-delà).
- Accroche personnelle, puis la raison de vouloir se connecter à cette personne.
- Aucun pitch, aucun lien, aucune demande d'appel. Une question légère est permise, pas obligatoire.
- Pas de signature (le profil s'affiche déjà).

**Suivi après connexion : 600 caractères maximum, trois blocs courts.**
- Rappel du contexte (pourquoi on est connectés).
- Une valeur : une observation tirée du terrain (retours réels du journal de `VENTE.md`), une ressource (la démo à ouvrir sur téléphone : https://www.fractal-innov.fr/stand/), une remarque sur leur salon. La démo est offerte comme quelque chose à essayer, pas comme une présentation commerciale.
- Une question ouverte sur leur situation. Proposer l'appel seulement si la fiche montre un intérêt explicite (ils ont posé une question, demandé une démo, parlé d'un salon proche).
- Pas de signature (le profil s'affiche déjà).

### E-mail

Pas de « connexion » par e-mail : l'équivalent est un e-mail à froid puis une relance. Mêmes principes.

**E-mail à froid** : objet de 50 caractères maximum, concret et propre au prospect (pas de « Proposition », pas de majuscules partout). Corps de 90 mots maximum : accroche personnelle, une observation, une question ouverte. Pas de demande d'appel, pas de lien calendrier.

**Relance** (5 à 7 jours plus tard, sans réponse) : 70 mots maximum, répond dans le même fil, apporte un élément nouveau (la démo, une observation), puis question ouverte ou proposition de l'appel de 30 minutes gratuit avec le lien calendrier de `VENTE.md`.

Signature des e-mails :

```
Hugo Daniel
CTO @ FractalInnov
https://www.fractal-innov.fr/stand/
```

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
python3 .claude/skills/prospection/scripts/journal.py add <<'EOF'
{"contact": "Claire Martin", "poste": "Directrice marketing", "entreprise": "Hydro SA", "secteur": "Balnéothérapie", "canal": "LinkedIn", "source": "Post sur Rééduca", "accroche": "Post du 20/09 sur le lit resté à l'usine", "angle": "Produit absent", "statut": "À envoyer", "message_1": "...", "message_2": "...", "prochaine_action": "Envoyer la demande de connexion"}
EOF
```

Le journal vit dans `.prospection/journal.md`, ignoré par git : le dépôt est public et aucune donnée nominative ne doit y entrer. Un même contact (nom + entreprise) est mis à jour, pas dupliqué. `journal.py show` affiche le tableau, prêt à coller dans Notion (une page Notion transforme un tableau Markdown collé en tableau). Quand l'utilisateur dit qu'un message est parti, qu'une connexion est acceptée ou qu'une réponse est arrivée, mets à jour le statut et la prochaine action.

## 6. Format de réponse

```
**Angle** : <élément personnel> · <douleur> · <mot clé du poste>

### Demande de connexion (ou E-mail à froid)
**A** (<n>/200 car.)
<message>

**B** (<n>/200 car.)
<message>

### Suivi après connexion (ou Relance)
**A** (<n>/600 car.)
<message>

**B** (<n>/600 car.)
<message>

**Contrôle** : <résultat du vérificateur, avertissements gardés et pourquoi>
**Journal** : contact ajouté ou mis à jour, statut, prochaine action
```

Les messages se présentent en texte brut, sans gras ni Markdown à l'intérieur : l'utilisateur les copie tels quels dans LinkedIn ou sa messagerie.
