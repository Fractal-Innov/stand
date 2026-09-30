# STAND, landing page

La fiche de vente de référence est `VENTE.md` (offre, prix, objections, journal) : tout wording de la page doit lui être conforme.

Site statique d'une seule page (`index.html`, CSS et JS inclus dedans), déployé par GitHub Pages sur https://www.fractal-innov.fr/stand. Le workflow publie une **liste blanche** (`index.html`, `favicon.ico`, `site.webmanifest`, `assets/`, `CNAME`) : `VENTE.md`, `CLAUDE.md` et `docs/` restent dans le dépôt. Un fichier ajouté au site doit être ajouté à la liste dans `.github/workflows/jekyll-gh-pages.yml`. La démo embarquée est servie depuis https://stand-demonstrateur.osc-fr1.scalingo.io/.

## Commits : Conventional Commits 1.0.0

Tous les messages de commit suivent https://www.conventionalcommits.org/en/v1.0.0/ :

```
<type>(<scope optionnel>): <description>

[corps optionnel]

[pied optionnel]
```

- Types : `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
- Description à l'impératif, en minuscules, sans point final.
- Rupture de compatibilité : `!` après le type/scope et/ou un pied `BREAKING CHANGE: ...`.
- Le corps explique le pourquoi et liste ce qui change.

## Rédaction du wording (texte vu par les prospects)

- Jamais de tiret cadratin « — » : utiliser « : », « . », « , » ou des parenthèses.
- Pas de point final dans les titres (H2, H3, H4, questions de la FAQ).
- La page doit rester fidèle à l'offre vendue :
  - l'écran tactile et le téléphone de pilotage ne sont pas fournis, le client les loue sur place ;
  - le flight case, le mobilier, la modélisation 3D, l'écran de veille 3D et la présentation à emporter sur mobile sont des options sur devis ;
  - les vidéos et fiches sont produites par le client, STAND les affiche ;
  - le support couvre l'installation avant le salon, pas le salon lui-même ;
  - pas de mode en ligne, pas de redémarrage ni de lancement automatique en standard (seule exception : la présentation à emporter sur mobile, option sur devis) ;
  - aucun prix ni délai affiché : le devis et le délai suivent l'atelier, qui suit l'appel de 30 minutes (l'appel n'est pas l'atelier) ;
  - une seule marque, Fractal Innov : aucun nom produit affiché (« STAND » n'est que le nom du dépôt et de la démo) ; l'offre se dit « le démonstrateur 3D de votre stand ».

## Démonstrateur et médias

- `assets/demo/` : captures du démonstrateur (webp, 1600 px de large). `vue-ensemble`, `attirer`, `presenter`, `emporter`, `logiciel`, `materiel` servent la lecture guidée ; `step-*` sont des recadrages sans l'interface ; `poster-portrait` n'est plus utilisé par la page depuis le 30/09/2026 (le téléphone reprend `vue-ensemble`).
- Hero : boucle vidéo `hero-loop.webm` / `hero-loop.mp4` (720p, sans son, ~1 Mo chacune, encodées depuis le rendu Needle), `hero-poster.webp` est sa première image. La vidéo ne joue que visible à l'écran et reste sur le poster si `prefers-reduced-motion` ou `saveData`.
- L'iframe de la démo n'est créée qu'au clic (« Lancer la démo », ou « Tester la démo » et la vidéo du hero via `data-launch-demo`, qui défilent et lancent en un seul geste) pour masquer le démarrage à froid du serveur Render. L'origine est définie une seule fois dans le script (`DEMO_ORIGIN`).
- **Une seule scène 3D dans la page** (30/09/2026) : l'unique iframe vit dans le calque `#scene3d`, enfant de `<body>`, posé par-dessus l'emplacement le plus visible (`data-scene-slot="demo"` : l'écran de la section démo ; `"parcours"` : les images du « Jumeau 3D »). On déplace le calque, jamais l'iframe (la déplacer dans le DOM la rechargerait). Gestionnaire `scene` : `charger`, `aller`, `placer`, `manipuler`, `pleinEcran` ; état sur `<body data-scene>` (`vide`, `chargement`, `prete`, `erreur`) et `data-scene-ici`. Prête au premier message de la démo, erreur « La 3D ne répond pas, réessayer » après 20 s. Écran tactile : la 3D se regarde, « Manipuler » lui donne le doigt. Le plein écran est le même calque sous une barre « Quitter ». Journal : `?debug` ou `__debug.on()` ; `?demo-origin=http://<hôte local>:<port>` pour tester une démo locale (refusé hors localhost et réseau local).
- Contrat avec le démonstrateur (`useContratPoi.ts` côté borne) : `?poi=<id>` à l'ouverture, `postMessage({ type: 'stand:goto', poi })` une fois chargé (`poi` null = vue de départ), retour `{ type: 'stand:poi', poi }` à chaque changement d'item, ce qui synchronise l'onglet de la lecture guidée. Identifiants : `votre-stand`, `attirer`, `presenter`, `emporter`, `logiciel`, `materiel`. La page lance toujours avec `?demarrer=auto` (pas de porte « Démarrer ») ; la borne annonce sa présence par un premier `stand:state` ; `postMessage({ type: 'stand:affichage', dock, marqueurs })` retire le dock et les marqueurs dans le parcours. L'étape « Vue d'ensemble » envoie `stand:goto` sans POI (vue de départ). Reprise du média : `?media=<id>&t=<s>&page=<n>` à l'ouverture ; retour `{ type: 'stand:state', poi, media, mediaType, t, page }` à chaque changement, stocké sur `<body>` (`data-media`, `data-media-type`, `data-t`, `data-page`) pour le lien partagé.
- La télécommande est chargée depuis `REMOTE_URL` (`/remote/public`, sans PIN). Les deux iframes reçoivent le même `?salle=<id>` généré à chaque chargement de page : une télécommande ne pilote que sa borne.

## Partage en salon

- Aperçu de partage : `assets/share/og-image-v3.jpg` (1200 × 630, composé depuis le hero ; refait le 30/09/2026 : logo seul, badge « Démonstrateur interactif », pied « fractal-innov.fr/stand · appel de 30 min », sans nom produit ni tarifs). Changer d'image = changer de nom de fichier, sinon LinkedIn garde l'ancienne en cache ; Open Graph et Twitter en URL absolues dans `<head>`. Icônes : `favicon.ico`, `assets/icons/`, `site.webmanifest`.
- Farfadet (`#share`, bas droite) : partage l'endroit courant par QR, lien copié ou feuille de partage native. L'état vit sur `<body>` en `data-section` (scroll-spy), `data-poi` (lecture guidée et démo) et `data-demo` (démo lancée). URL produite : `https://www.fractal-innov.fr/stand/?poi=<id>&demo=1#<section>` ; à l'arrivée, `?poi=` ouvre l'onglet et `&demo=1` relance la démo au même POI. Le mode « Télécommande » donne `REMOTE_URL?salle=<id>` : le téléphone qui scanne pilote la démo affichée sur cet écran (relais WebSocket sur Render, aucun wifi commun requis). Un `document.dispatchEvent(new CustomEvent('stand:share', { detail: 'place' | 'remote' }))` ouvre le farfadet dans ce mode (utilisé par « Sur votre téléphone » sous la démo).
- QR généré côté client avec `assets/js/qrcode.min.js` (qrcode-generator 1.4.4, MIT).
