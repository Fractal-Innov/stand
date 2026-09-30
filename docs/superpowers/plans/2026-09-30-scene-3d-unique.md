# Une seule scène 3D : plan d'implémentation

> **Pour l'exécution :** plan en intentions et points de décision (préférence
> de co-création de l'utilisateur, confirmée le 30/09/2026). Le code s'écrit
> au moment de chaque tâche, après lecture du code réel ; chaque tâche finit
> par un **point de rendu** montré à l'utilisateur avant la suivante. Étapes
> en cases à cocher (`- [ ]`).

**Objectif :** la section « Le jumeau 3D » affiche la scène en direct, qui suit
le parcours, avec une seule scène 3D dans toute la page.

**Architecture :** une iframe unique dans un calque `#scene3d`, posé par-dessus
l'emplacement le plus visible (`data-scene-slot="demo"` ou `"parcours"`), jamais
déplacée dans le DOM. Le contrat existant (`?poi`, `stand:goto`, `stand:poi`,
`stand:state`) reste la source de vérité ; la démo gagne `?demarrer=auto`.

**Technique :** page statique (`stand/index.html`, JS et CSS en ligne) ;
démo React + Needle Engine (`Needle5/Needle/Salon`), socle partagé
`Needle5/socle/`, miroir `salon_demo_app` déployé sur Scalingo.

**Spec :** `docs/superpowers/specs/2026-09-30-scene-3d-unique-design.md`

## Contraintes globales

- Une seule iframe de démo dans la page, à tout moment.
- Aucun bouton par-dessus la 3D (commandes dans le panneau de texte, « Quitter »
  du plein écran dans une barre séparée).
- Délai « La 3D ne répond pas » : **20 s**.
- Sans `?demarrer=auto`, la démo se comporte exactement comme aujourd'hui.
- Écran tactile (`pointer: coarse`) : la 3D se regarde par défaut, « Manipuler »
  / « Terminé ».
- Texte visible : jamais de tiret cadratin, pas de point final dans les titres.
- `index.html` s'édite par script (Python, `assert s.count(old) == 1`), jamais
  par l'outil Edit (il ouvre un onglet `file://` qui gêne la QA).
- Logs pédagogiques : interrupteur de débogage runtime des deux côtés.
- Jamais démarrer ni tuer le serveur de dev Needle (lancé depuis Unity).
- Miroir : lire `git status` de `salon_demo_app` avant tout `git add` ; une
  suppression signale un fichier non rapatrié dans Needle5.
- Commits Conventional Commits, une branche + une PR par livraison ;
  l'utilisateur fusionne.

## Points de vigilance (non couverts par la spec, les plus probables d'abord)

1. **Aller-retour rapide entre les deux sections** : la scène ne doit pas faire
   de ping-pong. Attendu : un seuil de visibilité avec hystérésis (la scène
   ne change d'emplacement que si le nouveau est nettement plus visible).
   Vérifié en tâche 5.
2. **Rotation du téléphone, scène active** : le calque doit recoller à
   l'emplacement. Vérifié en tâche 5 (redimensionnement 375 → 812 de large).
3. **Plein écran ouvert pendant un défilement** : l'observateur ne doit pas
   déplacer la scène tant que le plein écran est ouvert. Vérifié en tâche 7.
4. **Scalingo répond une page d'erreur (502)** : l'événement `load` arrive
   quand même. Attendu : le délai de 20 s s'appuie sur un premier message de
   la démo (`stand:poi` ou `stand:state`), pas seulement sur `load`. Vérifié
   en tâche 4 avec une origine faussée.
5. **« Tester la démo » du hero cliqué, puis défilement direct au parcours** :
   la scène se charge dans l'emplacement démo, puis doit rejoindre le
   parcours à la fin du chargement. Vérifié en tâche 5.

---

## Livraison 1 : Needle5, `?demarrer=auto`

### Tâche 1 : la porte sait démarrer seule (socle)

**Fichiers :**
- Modifier : `Needle5/socle/ui/porteDeChargement.ts` (`ReglagesPorte`,
  `armerPorteDeChargement`)
- Tests : `Needle5/Needle/Salon/tests/suites/t04.mjs`

**Interfaces :**
- Produit : `ReglagesPorte.demarrageAuto?: boolean`. Vrai : `demarrer()` est
  appelé à l'armement, sans clic ; le reste (attente du chargement, secours,
  fermeture, événement `ui-porte:fermee`) est inchangé.

- [ ] Lire `t04.mjs` et la façon dont il simule `<needle-engine>` et
  `loadfinished`.
- [ ] Ajouter à `t04` deux cas : avec `demarrageAuto`, la porte se ferme au
  `loadfinished` sans clic ; sans l'option, elle reste ouverte tant qu'on ne
  clique pas.
- [ ] Lancer `bash tests/run.sh t04` (depuis `Needle/Salon`) : les deux cas
  échouent (le premier).
- [ ] Implémenter l'option, avec un log « Démarrage automatique demandé ».
- [ ] Relancer `bash tests/run.sh` (toutes les suites) : tout passe. Vérifier
  aussi la suite du site `Needle/fractal-innov` qui compile le même socle.
- [ ] Commit `feat(socle): la porte de chargement peut démarrer seule`.

### Tâche 2 : la démo lit `?demarrer=auto`

**Fichiers :**
- Modifier : `Needle5/Needle/Salon/src/main.tsx` (appel à
  `armerPorteDeChargement`)
- Modifier : `Needle5/Needle/Salon/src/hooks/useContratPoi.ts` (en-tête du
  contrat : documenter le paramètre, constante `PARAMETRE_DEMARRER`)

**Interfaces :**
- Consomme : `ReglagesPorte.demarrageAuto` (tâche 1).
- Produit : l'URL `…/?demarrer=auto&poi=<id>&salle=<id>` démarre sans geste.

- [ ] Lire `main.tsx` autour de `armerPorteDeChargement` ; passer
  `demarrageAuto: new URLSearchParams(location.search).get('demarrer') === 'auto'`.
- [ ] **Point de décision (son)** : chercher où les vidéos se lancent. Si
  aucune ne démarre seule avec le son (elles s'ouvrent au geste du
  visiteur), il n'y a rien à faire ; sinon, repli en muet avec « Toucher
  pour le son ». Montrer ce qu'on a trouvé avant de coder le repli.
- [ ] Documenter le paramètre dans l'en-tête de `useContratPoi.ts`.
- [ ] Construire le miroir et le lancer **en local** (pas le serveur Needle) :
  `npm run sync:miroir`, puis dans `salon_demo_app` `npm run build && PORT=4300 npm start`.
  Ouvrir `http://localhost:4300/?demarrer=auto&poi=attirer` : pas de
  « Démarrer », la caméra part vers Attirer. Sans le paramètre : « Démarrer »
  présent.
- [ ] **Point de rendu** : l'utilisateur ouvre les deux URL.
- [ ] Commit `feat(salon): ?demarrer=auto, la landing démarre la borne sans second geste`,
  PR Needle5. **Ne pas pousser le miroir** avant la fin de la livraison 2
  (test commun en local).

---

## Livraison 2 : stand, le gestionnaire de scène

### Tâche 3 : outillage (journal, origine locale)

**Fichiers :** modifier `stand/index.html` (script principal, bloc des
constantes `DEMO_ORIGIN`).

**Interfaces :**
- Produit : `logScene(message)` (n'écrit que si `?debug` est dans l'URL ou si
  `window.__debug.on()` a été appelé) ; `DEMO_ORIGIN` remplaçable par
  `?demo-origin=http://…` **uniquement** sur `localhost`, `127.0.0.1` ou
  `192.168.*` (test de la livraison 1 en local).

- [ ] Ajouter l'interrupteur et `logScene`, avec un premier log au chargement
  (« scène : prête, origine … »).
- [ ] Ajouter la surcharge d'origine, refusée hors réseau local (log si
  refusée).
- [ ] Vérifier : `http://localhost:4201/?debug&demo-origin=http://localhost:4300`
  affiche l'origine locale dans la console ; sur l'URL de prod, la surcharge
  est ignorée.
- [ ] Commit `feat(stand): journal de la scène et origine de démo locale pour les tests`.

### Tâche 4 : le calque et l'emplacement démo

**Fichiers :** modifier `stand/index.html` (markup de `#demoViewport`, CSS,
remplacement de `launchDemo`).

**Interfaces :**
- Consomme : `logScene`, `demoHref`, `DEMO_ORIGIN`, `SALLE_ID`.
- Produit :
  - `scene.charger(slotId, poi)` : crée l'iframe (une seule fois) avec
    `demarrer=auto`, la pose sur l'emplacement ;
  - `scene.aller(poi)` : `stand:goto` si chargée ;
  - `scene.placer(slotId)` : recale le calque sur l'emplacement ;
  - `scene.etat` : `'vide' | 'chargement' | 'prete' | 'erreur'` ;
  - `scene.slot` : l'emplacement courant ;
  - `document.body.dataset.scene` reflète `scene.etat` (pour le CSS).
- Tous les appels existants à `launchDemo(poi)` passent par
  `scene.charger('demo', poi)` ou `scene.aller(poi)`.

- [ ] Créer `#scene3d` (enfant de `body`) et marquer `#demoViewport` avec
  `data-scene-slot="demo"`.
- [ ] Déplacer la création d'iframe de `launchDemo` vers `scene.charger` ;
  garder la mise à l'échelle borne (`--kiosk-scale`) quand le slot est `demo`.
- [ ] Délai 20 s : l'état passe à `prete` au premier message `stand:poi` ou
  `stand:state` venu de `DEMO_ORIGIN` ; sinon `erreur`, message « La 3D ne
  répond pas, réessayer » avec un bouton qui relance.
- [ ] Vérifier avec la démo locale (tâche 2) : « Lancer la démo » charge sans
  « Démarrer », la télécommande pilote, `stand:poi` synchronise toujours le
  parcours ; une seule iframe (`document.querySelectorAll('iframe[src*="demarrer"]').length === 1`).
- [ ] Vérifier l'erreur : `?demo-origin=http://localhost:9` → message après
  20 s.
- [ ] **Point de rendu** : l'utilisateur relance la section démo sur Mac et
  iPhone ; rien ne doit avoir changé à l'œil, sauf l'absence de « Démarrer ».
- [ ] Commit `refactor(stand): la démo passe par un calque de scène unique`.

### Tâche 5 : l'emplacement parcours et le changement d'emplacement

**Fichiers :** modifier `stand/index.html` (markup du parcours, CSS, JS du
parcours et du gestionnaire).

**Interfaces :**
- Consomme : `scene.charger`, `scene.aller`, `scene.placer`, `scene.slot`,
  `scene.etat`, `activateTab` du parcours.
- Produit : `data-scene-slot="parcours"` sur la zone média ;
  `scene.observer()` (IntersectionObserver avec hystérésis) ; l'événement
  `scene:slot` (`detail: { slot }`) émis à chaque changement.

- [ ] Une seule zone média pour le parcours : les images des étapes restent,
  la zone porte `data-scene-slot="parcours"`.
- [ ] Bouton « Explorer en 3D » sur l'image (étape courante),
  `scene.charger('parcours', poiDeLEtape)`.
- [ ] Observateur : seuil et hystérésis (proposition : changer si le nouvel
  emplacement est visible à plus de 50 % et plus que l'actuel de 20 points).
  Log de chaque décision avec les taux.
- [ ] Sans `IntersectionObserver` : pas d'observateur, la scène reste dans
  l'emplacement où elle a été chargée (log « observateur indisponible »).
- [ ] Arrivée dans le parcours : `scene.aller(poiDeLEtape)`. Suivant,
  Précédent et la barre : `scene.aller` en plus de `activateTab` quand la scène
  est dans le parcours.
- [ ] Scène présente dans le parcours : l'étiquette « Suivant » de l'image se
  masque, la ligne « ✋ Manipuler · ⤢ Plein écran » remplace « Voir dans la
  démo » en tête du panneau de texte (Manipuler n'apparaît que sur
  `pointer: coarse`).
- [ ] Emplacement démo quitté : repère « La démo vous attend dans le parcours,
  plus bas ↓ », qui fait défiler jusqu'au parcours.
- [ ] Vérifier : aller-retour lent et rapide (pas de ping-pong), rotation
  simulée (375×812 → 812×375), cas du hero (« Tester la démo » puis défilement
  direct), caméra conservée, une seule iframe.
- [ ] **Point de rendu** : captures ordinateur et mobile des états « pas
  chargée », « chargement », « scène ici », repère ; l'utilisateur teste sur
  iPhone. Ajuster avant de continuer.
- [ ] Commit `feat(stand): la scène 3D rejoint le parcours et suit ses étapes`.

### Tâche 6 : Manipuler (écran tactile)

**Fichiers :** modifier `stand/index.html` (CSS du calque, JS du gestionnaire,
rangée `.demo-actions`).

**Interfaces :**
- Consomme : `scene.slot`, les commandes de la tâche 5.
- Produit : `scene.manipuler(on: boolean)` ; `#scene3d.is-manip` ; sans elle,
  `pointer-events: none` sur l'iframe si `pointer: coarse`.

- [ ] « Manipuler » dans la ligne du parcours et dans la rangée de la section
  démo ; libellé « Terminé » quand actif.
- [ ] Changement d'emplacement ou sortie de l'écran : retour automatique au
  mode « regarder ».
- [ ] Vérifier au navigateur en mode mobile : défilement libre par-dessus la
  3D, Manipuler rend la main à la scène, Terminé la reprend.
- [ ] **Point de rendu** : l'utilisateur fait le test du pouce sur iPhone.
- [ ] Commit `feat(stand): Manipuler, la 3D ne piège plus le défilement sur mobile`.

### Tâche 7 : le plein écran avec la même scène

**Fichiers :** modifier `stand/index.html` (overlay `#demoFullscreenOverlay`,
son JS, CSS du calque).

**Interfaces :**
- Consomme : `scene.charger`, `scene.placer`, l'observateur.
- Produit : `scene.pleinEcran(on: boolean)` ; l'observateur est suspendu
  tant que le plein écran est ouvert.

- [ ] Supprimer `#demoFullscreenIframe` ; le calque passe en `position: fixed`
  sous une barre « Quitter » séparée (hauteur réservée, rien sur la 3D).
- [ ] Déclencheurs : « Ouvrir en plein écran » (section démo) et « ⤢ Plein
  écran » (parcours). Scène pas chargée : `scene.charger` puis plein écran.
- [ ] Échap et « Quitter » ferment ; le focus revient au déclencheur ; le
  calque recolle à son emplacement.
- [ ] Vérifier : ouverture et fermeture sans rechargement (même `src`, même
  caméra), défilement de fond bloqué, observateur suspendu.
- [ ] **Point de rendu** : l'utilisateur ouvre et ferme sur Mac et iPhone.
- [ ] Commit `feat(stand): le plein écran reprend la même scène`.

### Tâche 8 : vérification commune et mise en ligne

- [ ] Parcours complet des vérifications de la spec, démo locale (tâche 2) +
  page locale, 1440 px, 375 px et iPhone réel (`http://192.168.1.30:4201`).
- [ ] Console sans erreur, `document.documentElement.scrollWidth` égal à la
  largeur de l'écran.
- [ ] Mettre à jour `VENTE.md` si un texte visible a changé (repère, boutons).
- [ ] PR stand. Ordre de mise en ligne : PR Needle5 fusionnée, sync du miroir,
  `git status` du miroir relu, push (déploiement Scalingo), vérification de
  `?demarrer=auto` en ligne, **puis** fusion de la PR stand.
- [ ] Après fusion : vérifier en ligne une seule iframe, l'aller-retour, le
  plein écran.
