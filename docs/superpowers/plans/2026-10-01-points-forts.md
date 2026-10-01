# Haut de page en présentation produit : plan d'implémentation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal :** transformer le haut de `index.html` en présentation produit (hero épuré, six Points forts en slider automatique, navbar qui apparaît à partir des Points forts) sans rien retirer de ce qui suit.

**Architecture :** tout reste dans `index.html` (CSS et JS inclus, comme aujourd'hui). CSS ajouté en blocs de surcharge commentés avant la fermeture de la feuille ; JS ajouté dans le script existant, en blocs numérotés comme les autres (« 2c. POINTS FORTS », « 2d. NAVBAR D'APPARITION »). Deux visuels composés en HTML jetable puis rendus en webp par Chrome sans affichage.

**Tech stack :** HTML / CSS / JS sans dépendance, `scroll-snap`, IntersectionObserver, Chrome headless + `cwebp` (ou `sips` à défaut) pour les montages.

**Spec :** `docs/superpowers/specs/2026-10-01-points-forts-design.md`

**Préférence de l'auteur :** plan en intentions et points de décision ; le code s'écrit au moment de la tâche. Pas de suite de tests dans ce dépôt : le « test qui échoue » de chaque tâche est une assertion JS lancée dans le navigateur intégré (`javascript_tool`) sur le serveur `stand-local` (`.claude/launch.json` du dossier GitHub), vue rouge avant le code, verte après.

## Global Constraints

- Éditer `index.html` par script python/Bash, jamais avec l'outil Edit (il ouvre un onglet `file://`).
- Jamais de tiret cadratin « — » dans un texte visible ; pas de point final dans les titres.
- Aucun prix, aucun délai, aucun nom d'outil de statistiques (pas « Umami »), aucun nom produit (« STAND »).
- Navbar sur une seule rangée, jamais deux lignes.
- Tout ce qui bouge a sa variante `prefers-reduced-motion: reduce`.
- Toute nouvelle logique a ses lignes dans le journal `logScene` (visible sous `?debug`).
- Un fichier ajouté au site doit être dans la liste blanche du workflow : les nouveaux visuels vont sous `assets/`, déjà publié.
- Mobile : largeur du document = largeur de la fenêtre (aucun défilement horizontal de page).
- Commits Conventional Commits, pied `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Review Focus

1. **Farfadet sans liens de navbar** : `updateNavActiveFromScroll` sort tout de suite si `#mainNav .nav-link` est vide, donc `body[data-section]` ne serait plus posé. Attendu : le partage garde la section courante (Tâche 3).
2. **Lien entrant `#points-forts` ou `?poi=…&demo=1#demo`** à l'ouverture, navbar encore masquée : la section doit atterrir à 24 px sous la barre, pas dessous (Tâche 3).
3. **Slider hors écran** : le défilement automatique ne doit pas tourner (ni faire défiler la page) quand la section n'est pas visible ; `scrollTo` de la piste ne doit jamais bouger la fenêtre (Tâche 2).
4. **Onglet en arrière-plan puis retour** : pas de rafale de changements de slide (Tâche 2).
5. **Clavier** : Tab atteint les points et le bouton pause ; le focus dans le slider le met en pause ; la navbar masquée n'est pas atteignable au clavier (Tâche 2 et 3).

---

### Tâche 1 : la section Points forts, statique

**Fichiers :** `index.html` (nouvelle `<section id="points-forts">` entre la fin du hero, `</div>` de `.hero-wrapper`, et `#demo` ; bloc CSS « POINTS FORTS »).

**Produit :** `#points-forts` avec `.pf__piste` (piste), six `.pf__slide[role=group][aria-label="n sur 6"]`, chacune `.pf__titre`, `.pf__sous-titre` facultatif, `.pf__visuel img` ; `.pf__commandes` avec six `button.pf__point[aria-label="Point fort n : …"]` et `button.pf__lecture`.

- [ ] Assertion rouge : `document.querySelectorAll('#points-forts .pf__slide').length === 6` → `false`.
- [ ] Markup des six slides avec les titres et sous-titres exacts du tableau de la spec ; visuels v1 provisoires : `vue-ensemble`, `presenter`, `attirer`, `step-expliquer` (slides 2, 4, 5, 6 recalées en Tâche 5).
- [ ] CSS : cartes arrondies sur fond clair de la page, piste en `scroll-snap-type: x mandatory`, carte à ~86 % de la largeur sur mobile et ~78 % sur ordinateur pour laisser dépasser la suivante, pilule de points + bouton rond centrés dessous (référence Apple). Point actif allongé avec un remplissage `::after` piloté par une variable `--pf-progres`.
- [ ] Titre de section « Points forts » avec le même surtitre `.section-number` que les autres sections (les ancres s'y calent).
- [ ] Assertion verte ; rendu 375 et 1440 ; `document.documentElement.scrollWidth === innerWidth` sur mobile.
- [ ] Commit `feat(stand): ajouter la section Points forts`.

**Point de décision :** couleur de fond de la section (gris clair Apple ou le fond actuel de `.page-rest`). Par défaut : le fond actuel, cartes un ton plus clair.

### Tâche 2 : le slider (défilement automatique, points, pause)

**Fichiers :** `index.html` (JS « 2c. POINTS FORTS », CSS d'animation du titre).

**Consomme :** le markup de la Tâche 1. **Produit :** `#points-forts[data-actif="n"]`, `[data-lecture="on|off"]`.

- [ ] Assertion rouge : après 6 s avec la section visible, `#points-forts` a `data-actif="1"` (index 0 au départ).
- [ ] JS : `aller(n, raison)` fait défiler la piste avec `piste.scrollTo({ left })` (jamais `scrollIntoView`, qui bougerait la fenêtre), met à jour points, `aria-current`, `data-actif`, et journalise `points forts : slide n (auto | point | glissement)`.
- [ ] Minuterie de 5 s par `requestAnimationFrame` qui alimente `--pf-progres` ; tourne seulement si la section est visible (IntersectionObserver, seuil 0.4) et l'onglet visible (`visibilitychange`, temps remis à zéro au retour).
- [ ] Arrêt définitif (bouton → « lecture ») au clic d'un point ou au glissement manuel (`scrollend`, ou un `scroll` stabilisé, non provoqué par `aller`) ; pause temporaire au survol et au focus dans la section.
- [ ] Titre : entrée avec ~250 ms de retard, puis flottement lent (`translateY` de quelques px, boucle de ~6 s) sur la slide active seulement.
- [ ] `prefers-reduced-motion` : `data-lecture="off"` dès le départ, pas de flottement, titres visibles.
- [ ] Assertions vertes : avance auto ; clic sur le point 4 → `data-actif="3"` et `data-lecture="off"` ; `scrollY` inchangé pendant un changement de slide déclenché hors écran.
- [ ] Commit `feat(stand): faire défiler les Points forts`.

### Tâche 3 : la navbar d'apparition

**Fichiers :** `index.html` (header `.masthead`, CSS « NAVBAR D'APPARITION », JS 0b, 2, 2b, nouveau 2d).

**Consomme :** `#points-forts`. **Produit :** `body[data-barre="visible|cachee"]`.

- [ ] Assertions rouges : en haut de page, `getComputedStyle(document.querySelector('.masthead')).transform` n'est pas une translation négative ; `document.querySelector('.burger')` existe.
- [ ] Markup : logo + deux liens `.masthead-cta`, « Tester la démo » (`href="#demo" data-launch-demo`) et « Réserver 30 min » (`#contact`), chacun avec un libellé court (`La démo`, `30 min`) affiché sous 560 px (deux `<span>`, l'un masqué selon la largeur ; `aria-label` complet). Retirer `.main-nav-links`, le burger et leur JS (bloc 2).
- [ ] Apparition : IntersectionObserver sur le haut de `#points-forts` (ou une sentinelle posée juste avant) ; `body[data-barre]` bascule ; CSS `transform: translateY(-110%)` → `0` en ~350 ms `cubic-bezier(.2,.8,.2,1)` ; `visibility: hidden` une fois cachée (clavier). Reduced motion : pas de transition.
- [ ] Scroll-spy (0b) : retirer le `return` sur `navLinksAll` vide pour que `body[data-section]` reste posé ; ajouter `points-forts` à `sectionIdsNav`.
- [ ] Ancres (2b) : `basBarre` = hauteur de la barre affichée (mesurée sur `.masthead-bg` en ignorant la translation, ou `offsetTop + offsetHeight`), pour que la cible soit juste quand la barre est cachée au moment du clic.
- [ ] `scroll-padding-top` de `<html>` : vérifier qu'il reste cohérent (il sert encore au saut natif hors sections).
- [ ] Assertions vertes : barre cachée en haut, visible quand `#points-forts` touche le haut, recachée en remontant ; `body.dataset.section === 'demo'` après défilement sur la démo ; clic depuis le hero sur un lien `#demo` → repère à 24 px ± 2 sous le bas de la barre ; ouverture `?r=N#livre` idem ; rangée unique à 375 px (`.masthead-inner` sur une ligne, pas de débordement).
- [ ] Commit `feat(stand): faire apparaître la barre à partir des Points forts`.

**Point de décision :** seuil d'apparition (haut des Points forts au haut de la fenêtre, ou légèrement avant). Par défaut : quand le hero a quitté l'écran à 90 %.

### Tâche 4 : le hero épuré

**Fichiers :** `index.html` (hero, CSS `.hero-pillars` et surcharges hero).

- [ ] Assertions rouges : `document.querySelector('.hero-pillars')` existe ; le texte de `.hero-lead` ne contient pas « visio ».
- [ ] Logo dans le flux en haut du hero (même image, `width`/`height` conservés, `alt="Fractal Innov"`), visible tant que la barre est cachée.
- [ ] Accroche de la spec, mot pour mot. Titre et surtitre inchangés.
- [ ] Visuel en grand (la vidéo prend la largeur de la colonne), puis barre CTA dessous avec les deux boutons existants (`data-launch-demo` conservé).
- [ ] Retirer `.hero-pillars` et son CSS ; vérifier que les `#step-*` restent atteignables ailleurs (ils sont dans #valeur, gardée).
- [ ] Le lien « Descendre » du hero vise désormais `#points-forts`.
- [ ] Assertions vertes ; rendu 375 / 500 / 1440 ; aucun défilement horizontal ; LCP : le poster garde `fetchpriority="high"`.
- [ ] Commit `feat(stand): épurer le hero`.

### Tâche 5 : les deux montages (écrans, tableau de bord)

**Fichiers :** `_montage-ecrans.html`, `_montage-stats.html` (jetables, scratchpad), `assets/points-forts/ecrans.webp`, `assets/points-forts/stats.webp` (+ recadrages webp des visuels 4 et 5 si besoin).

- [ ] Montage écrans : la capture `vue-ensemble` dans trois cadres (écran tactile sur pied, portable, tablette), fond transparent ou au ton des cartes, 1600 px de large.
- [ ] Montage statistiques : un tableau de bord stylisé aux couleurs de la page, données factices plausibles mais génériques (visites par jour, boutons touchés, médias vus jusqu'au bout), sans marque d'outil ni nom de client.
- [ ] Rendu Chrome headless → PNG → webp qualité ~82 ; poids cible < 150 Ko chacun.
- [ ] Brancher les visuels dans les slides 2 et 6 (`width`/`height`, `loading="lazy"`, `alt` descriptif).
- [ ] Supprimer les HTML jetables. Commit `feat(stand): illustrer les Points forts`.

**Point de décision :** validation visuelle des deux montages par l'auteur avant le commit.

### Tâche 6 : fiche de vente et notes du dépôt

**Fichiers :** `VENTE.md`, `CLAUDE.md`.

- [ ] `VENTE.md` : l'application autonome s'installe aussi sur le portable du commercial (visio, rendez-vous) ; Supports : la landing parle de salon, showroom, rendez-vous, visio ; journal du 01/10 (retour du directeur commercial, restructuration).
- [ ] `CLAUDE.md` : Points forts (structure, slider, journal), barre d'apparition (`body[data-barre]`), scroll-spy indépendant de la navbar, nouveaux assets.
- [ ] Commit `docs(stand): consigner la présentation produit`.

### Tâche 7 : vérification d'ensemble et PR

- [ ] Parcours complet sur `stand-local` : 375, 500, 1440 ; reduced motion émulé ; console sans erreur ; farfadet (QR de la section courante) ; démo lancée depuis la navbar puis depuis le hero ; ancres du pied de page.
- [ ] Captures pour l'auteur (hero mobile et ordinateur, slider, barre apparue).
- [ ] Push, PR vers `master`, commande de fusion donnée à l'auteur.

## Ordre et dépendances

1 → 2 (le slider anime le markup) → 3 (la barre s'accroche à `#points-forts`) → 4 → 5 → 6 → 7. Les tâches 4 et 5 sont indépendantes l'une de l'autre.
