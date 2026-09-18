# STAND, landing page

Site statique d'une seule page (`index.html`, CSS et JS inclus dedans), déployé par GitHub Pages sur https://stand.fractal-innov.fr. La démo embarquée est servie depuis https://salon-demo-app.onrender.com/.

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
  - le flight case, le mobilier, la modélisation 3D et l'écran de veille 3D sont des options sur devis ;
  - les vidéos et fiches sont produites par le client, STAND les affiche ;
  - le support couvre l'installation avant le salon, pas le salon lui-même ;
  - pas de mode en ligne, pas de redémarrage ni de lancement automatique en standard ;
  - formules affichées : Logiciel 4 900 € HT (livré en 4 semaines) et Kit complet 6 900 € HT.

## Démonstrateur et médias

- `assets/demo/` : captures du démonstrateur (webp, 1600 px de large). `vue-ensemble`, `attirer`, `presenter`, `emporter`, `logiciel`, `materiel` servent la lecture guidée ; `poster-portrait` et `step-*` sont des recadrages sans l'interface.
- Hero : boucle vidéo `hero-loop.webm` / `hero-loop.mp4` (720p, sans son, ~1 Mo chacune, encodées depuis le rendu Needle), `hero-poster.webp` est sa première image. La vidéo ne joue que visible à l'écran et reste sur le poster si `prefers-reduced-motion` ou `saveData`.
- L'iframe de la démo n'est créée qu'au clic (« Lancer la démo », ou « Tester la démo » et la vidéo du hero via `data-launch-demo`, qui défilent et lancent en un seul geste) pour masquer le démarrage à froid du serveur Render. L'origine est définie une seule fois dans le script (`DEMO_ORIGIN`).
- Contrat avec le démonstrateur (`useContratPoi.ts` côté borne) : `?poi=<id>` à l'ouverture, `postMessage({ type: 'stand:goto', poi })` une fois chargé (`poi` null = vue de départ), retour `{ type: 'stand:poi', poi }` à chaque changement d'item, ce qui synchronise l'onglet de la lecture guidée. Identifiants : `votre-stand`, `attirer`, `presenter`, `emporter`, `logiciel`, `materiel`. Reprise du média : `?media=<id>&t=<s>&page=<n>` à l'ouverture ; retour `{ type: 'stand:state', poi, media, mediaType, t, page }` à chaque changement, stocké sur `<body>` (`data-media`, `data-media-type`, `data-t`, `data-page`) pour le lien partagé.
- La télécommande est chargée depuis `REMOTE_URL` (`/remote/public`, sans PIN). Les deux iframes reçoivent le même `?salle=<id>` généré à chaque chargement de page : une télécommande ne pilote que sa borne.

## Partage en salon

- Aperçu de partage : `assets/share/og-image.jpg` (1200 × 630, composé depuis le hero), Open Graph et Twitter en URL absolues dans `<head>`. Icônes : `favicon.ico`, `assets/icons/`, `site.webmanifest`.
- Farfadet (`#share`, bas droite) : partage l'endroit courant par QR, lien copié ou feuille de partage native. L'état vit sur `<body>` en `data-section` (scroll-spy), `data-poi` (lecture guidée et démo) et `data-demo` (démo lancée). URL produite : `https://stand.fractal-innov.fr/?poi=<id>&demo=1#<section>` ; à l'arrivée, `?poi=` ouvre l'onglet et `&demo=1` relance la démo au même POI. Le mode « Télécommande » donne `REMOTE_URL?salle=<id>` : le téléphone qui scanne pilote la démo affichée sur cet écran (relais WebSocket sur Render, aucun wifi commun requis). Un `document.dispatchEvent(new CustomEvent('stand:share', { detail: 'place' | 'remote' }))` ouvre le farfadet dans ce mode (utilisé par « Sur votre téléphone » sous la démo).
- QR généré côté client avec `assets/js/qrcode.min.js` (qrcode-generator 1.4.4, MIT).

