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
- L'iframe de la démo n'est créée qu'au clic (« Lancer la démo ») pour masquer le démarrage à froid du serveur Render. L'origine est définie une seule fois dans le script (`DEMO_ORIGIN`).
- Contrat avec le démonstrateur (`useContratPoi.ts` côté borne) : `?poi=<id>` à l'ouverture, `postMessage({ type: 'stand:goto', poi })` une fois chargé (`poi` null = vue de départ), retour `{ type: 'stand:poi', poi }` à chaque changement d'item, ce qui synchronise l'onglet de la lecture guidée. Identifiants : `votre-stand`, `attirer`, `presenter`, `emporter`, `logiciel`, `materiel`.
- La télécommande est chargée depuis `REMOTE_URL` (`/remote/public`, sans PIN). Les deux iframes reçoivent le même `?salle=<id>` généré à chaque chargement de page : une télécommande ne pilote que sa borne.
