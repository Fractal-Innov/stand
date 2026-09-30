# Une seule scène 3D sur la page /stand/

Conception validée en co-création le 30/09/2026.

## Intention

La section « Le jumeau 3D » montre la scène en direct à la place des images,
et la scène suit chaque étape du parcours. La page ne charge jamais deux
scènes : sur mobile, la scène (`STAND_01.glb`, 7,6 Mo, plus l'application)
coûte cher en données et en mémoire.

**Critères de succès**

- Suivant et Précédent déplacent la caméra de la 3D.
- Une seule iframe de démo existe dans la page, à tout moment.
- Un visiteur qui ne demande pas la 3D ne la télécharge pas.
- Passer de la section démo au parcours, et inversement, ne recharge rien :
  la caméra et le média en cours sont conservés.
- Sur écran tactile, le défilement de la page n'est jamais piégé par la 3D.

## Architecture : une scène, plusieurs emplacements

Déplacer une iframe dans le document la recharge (sauf Chrome récent avec
`moveBefore`, pas Safari). La scène vit donc dans un **calque** et ne change
jamais de place dans le DOM ; seuls sa position et sa taille changent.

- **Calque** `#scene3d` : enfant direct de `body`, `position: absolute`,
  contient l'unique iframe.
- **Emplacements** : `data-scene-slot="demo"` (écran de la section démo) et
  `data-scene-slot="parcours"` (zone média du parcours). Chacun garde son
  image d'aperçu en fond.
- **Choix de l'emplacement** : un `IntersectionObserver` sur les
  emplacements ; la scène va vers le plus visible. Aucun visible : elle
  reste où elle est.
- **Calage** : le calque prend le rectangle de l'emplacement actif en
  coordonnées de la page. Recalcul au changement d'emplacement et via
  `ResizeObserver` (rotation, redimensionnement), jamais pendant le
  défilement.
- **Mise à l'échelle** : l'emplacement démo garde son rendu « borne »
  (largeur de référence 1200 px, `--kiosk-scale`) ; l'emplacement parcours
  affiche la scène à sa taille réelle.
- **État** : le contrat existant reste la source de vérité. À l'arrivée dans
  le parcours, la scène reçoit `stand:goto` avec l'étape affichée ;
  `stand:poi` fait suivre l'étape quand le visiteur ouvre un sujet dans la 3D.
- **Plein écran** : le calque passe en `position: fixed` plein écran, sous une
  barre « Quitter » séparée de la scène (aucun bouton par-dessus la 3D). À la
  fermeture, il reprend son emplacement. L'ancienne iframe de plein écran
  (`#demoFullscreenIframe`) est supprimée.
- **Salle** : inchangée (`SALLE_ID` par chargement de page) ; la télécommande
  pilote l'unique scène, où qu'elle soit.

Le gestionnaire remplace `launchDemo` et l'overlay de plein écran actuels.

## Ce que vit le visiteur

### Section démo

| État | Affichage | Geste |
|---|---|---|
| Pas chargée | Image et « Lancer la démo » | Charge la scène avec `?demarrer=auto` |
| Chargement | Image, « La borne se réveille, une dizaine de secondes » | Attendre ou lire |
| Scène ici | 3D en direct | Manipuler, télécommande |
| Scène partie | Image et repère « La démo vous attend dans le parcours, plus bas ↓ » | Le repère fait défiler jusqu'au parcours |

« Manipuler » rejoint la rangée existante (« Ouvrir en plein écran · Sur
votre téléphone »).

### Parcours

| État | Affichage | Geste |
|---|---|---|
| Pas chargée | Image de l'étape et bouton « Explorer en 3D » sur l'image | L'image fait avancer d'une étape ; le bouton charge la scène |
| Chargement | Image de l'étape, indicateur discret | Le parcours continue ; la 3D rejoint l'étape affichée à la fin |
| Scène ici | 3D qui suit Suivant et Précédent ; l'étiquette « Suivant » sur l'image disparaît | Ordinateur : interactive. Mobile : voir ci-dessous |
| Sujet ouvert dans la 3D | L'étape suit (`stand:poi`) | |

Commandes : **première ligne du panneau de texte**, juste sous la scène sur
mobile, en haut du panneau à droite sur ordinateur. Liens texte sans fond
(environ 32 px) : « ✋ Manipuler · ⤢ Plein écran », présents seulement quand
la scène est dans le parcours. Ils remplacent « Voir dans la démo ».

### Manipuler (écran tactile, les deux emplacements)

- Par défaut, la scène se regarde : `pointer-events: none` sur l'iframe, le
  doigt fait défiler la page.
- « Manipuler » rend la scène interactive ; le libellé devient « Terminé »,
  qui rend le défilement.
- Écran à pointeur fin (souris) : interactive d'emblée, pas de bouton.
- Détection : `matchMedia('(pointer: coarse)')`.

## Côté démo (Needle5) : `?demarrer=auto`

- À la fin du chargement, la porte « Démarrer » se ferme seule.
- Son bloqué par le navigateur : vidéos en muet, indication « Toucher pour le
  son ».
- Sans le paramètre : comportement inchangé (borne de salon, liens directs).
- Journal : scope dédié, visible avec `__debug.on()`.
- La page ajoute `demarrer=auto` à tous ses lancements (démo, parcours,
  plein écran) : un seul geste sur toute la page.

## Erreurs

- Pas d'événement `load` de l'iframe après **20 s** : l'image reste, message
  « La 3D ne répond pas, réessayer » ; le parcours en images fonctionne.
- `navigator.connection.saveData` : aucun chargement automatique (déjà le cas :
  la scène ne se charge qu'au geste).
- Pas d'`IntersectionObserver` : la scène reste dans son emplacement de
  départ.

## Journal de débogage (page)

Interrupteur `?debug` ou `__debug.on()`. Le gestionnaire raconte le trajet :
changement d'emplacement (avec le taux de visibilité), `goto` envoyé,
Manipuler activé ou non, plein écran, délai dépassé.

## Livraison

1. PR `Needle5` : `?demarrer=auto`, puis sync du miroir `salon_demo_app` et
   déploiement Scalingo (lire `git status` du miroir avant tout ajout : une
   suppression signale un fichier non rapatrié).
2. PR `stand` : le gestionnaire de scène, les emplacements, Manipuler, le
   plein écran unique.

Les deux sont testées ensemble en local avant la mise en ligne.

## Vérifications

- 1440 px et 375 px : aller-retour démo ↔ parcours, caméra conservée, une
  seule iframe (`document.querySelectorAll('iframe[src*="scalingo"]').length === 1`).
- Suivant et Précédent déplacent la caméra ; un sujet ouvert dans la 3D fait
  suivre l'étape.
- Mobile : Manipuler et Terminé, défilement jamais piégé.
- Plein écran : ouverture et fermeture sans rechargement, « Quitter » hors de
  la scène.
- iPhone réel via le serveur local (`http://192.168.1.30:4201`).
- Démo injoignable (URL faussée) : message après 20 s, parcours intact.

## Hors périmètre

- Changer l'apparence de la démo elle-même (dock, marqueurs).
- La télécommande (iframe légère, sans scène 3D) : inchangée.
- Refaire les captures d'aperçu (passe séparée de l'utilisateur).
