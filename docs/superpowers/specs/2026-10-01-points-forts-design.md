# Haut de page en présentation produit : hero épuré, Points forts, navbar d'apparition

Date : 01/10/2026. Cadrage en co-création (réponses A1 à C4 et navbar mobile dans la conversation du jour).

## Pourquoi

Retour d'un directeur commercial sur la page : soignée, mais exhaustive au point de neutraliser la curiosité.
Il conseille de l'aborder comme une présentation de produit : quelques visuels et points marquants qui disent
vite l'essentiel. En parallèle, l'offre s'élargit dans le discours : le démonstrateur sert en salon, mais aussi
en showroom, en rendez-vous sur site et en visio avec partage d'écran, et il mesure l'usage.

Références : pages produit Apple (hero épuré, « Points forts » en slider automatique, barre produit collante).

## Critère de réussite

En dix secondes, un prospect qui ouvre la page sur mobile voit le visuel, lit le titre, fait défiler six
points forts et sait où cliquer (« La démo », « 30 min »). Rien de ce qui suit les Points forts ne disparaît.

## Décisions

| Réf. | Décision |
|---|---|
| A1 | En visio ou en showroom, la démo tourne sur le mini PC du kit (écran partagé) **ou** sur le portable du commercial via l'application autonome |
| A2 | Point 5 : « Votre produit présenté, sans le transporter » ; « toute votre gamme » cité comme option |
| A3 | Statistiques : « Sans cookie, aucune donnée personnelle ». Pas de nom d'outil, pas de « hébergé en Europe » |
| A4 | Point 4 : « dans un navigateur ou une application » |
| A5 | Titre du hero inchangé ; seule la phrase d'accroche s'élargit |
| B1, B2 | « Le défi » et « Ce que vous gagnez » restent tels quels ; à revoir après la restructuration |
| B3 | Ordre inchangé après les Points forts |
| B4 | Navbar : logo + deux boutons, plus de liens de section ni de burger |
| B5 | Le hero garde ses deux CTA |
| C1 | Publication avec la boucle vidéo actuelle ; l'animation 3D la remplacera au même emplacement |
| C2 | Animation future : vidéo pré-calculée, deux rendus sur la même timeline (16:9 et 9:16), moins de 1,5 Mo chacun |
| C3 | Visuels des slides statiques en v1, partout |
| C4 | La slide suivante dépasse sur le bord |
| Mobile | Boutons de la navbar : « La démo » et « 30 min » (libellés complets dès que la place le permet) |

## 1. Ordre de la page

Hero, **Points forts** (nouvelle section `#points-forts`), Démo, Le défi, Ce que vous gagnez, Jumeau 3D,
Ce qui est livré, Déroulé, FAQ, Contact.

## 2. Hero

- En haut, le logo seul, dans le flux (il défile avec la page).
- « Démonstrateur interactif », puis le titre actuel, inchangé.
- Accroche : « Le jumeau 3D de votre produit, sur votre stand, en showroom ou en visio. Le visiteur l'explore
  du doigt, votre commercial le pilote depuis son téléphone. »
- Visuel en grand : la boucle `hero-loop` actuelle (poster, lecture seulement visible, respect de
  `prefers-reduced-motion` et `saveData` conservés). `data-launch-demo` conservé.
- Sous le visuel, une barre avec « Tester la démo » et « Réserver 30 min ».
- Retirés : les trois piliers `.hero-pillars` (Attirer, Expliquer, Réutiliser), doublons des Points forts.

## 3. Points forts

Titre de section : « Points forts ». Six slides, chacune un titre (une phrase, sans point final) et un visuel.

| # | Titre | Sous-titre | Visuel v1 |
|---|---|---|---|
| 1 | Une interface épurée, que le visiteur comprend seul | | capture `vue-ensemble` |
| 2 | Un seul démonstrateur, sur tous vos écrans | Stand, showroom, visio | montage : écran tactile, portable, tablette |
| 3 | Pilotez la présentation depuis votre téléphone | | capture `presenter` + téléphone |
| 4 | La fluidité de la 3D, dans un navigateur ou une application | | capture de la scène |
| 5 | Votre produit présenté, sans le transporter | Toute votre gamme, en option | recadrage `step-*` |
| 6 | Mesurez ce qui intéresse vos visiteurs | Sans cookie, aucune donnée personnelle | montage d'un tableau de bord, sans marque d'outil |

Comportement :

- Piste horizontale en `scroll-snap` : glisser au doigt, la slide suivante dépasse sur le bord.
- Pilule de points + bouton pause / lecture. Le point actif s'allonge et se remplit en 5 s.
- Défilement automatique toutes les 5 s, seulement si la section est visible (IntersectionObserver).
  Il s'arrête au clic sur un point ou au glissement manuel (le bouton passe en « lecture ») ; pause au survol et au focus.
- Le visuel suit le point actif ; le titre apparaît avec un léger délai puis flotte doucement.
- `prefers-reduced-motion` : pas de défilement automatique, pas de flottement, titres affichés directement.
- Accessibilité : `role="region"` + `aria-roledescription="carrousel"`, slides en `role="group"` avec
  « n sur 6 », points en boutons nommés, bouton pause nommé selon son état.
- Journal pédagogique sous `?debug` (changement de slide, raison : auto, point, glissement).

## 4. Navbar

- Masquée au chargement et tant que le hero est à l'écran.
- Apparaît quand le haut des Points forts atteint le haut de la fenêtre : glissement depuis le haut (transition
  CSS sur `transform`), disparaît quand on remonte dans le hero. `prefers-reduced-motion` : apparition sans glissement.
- Contenu : logo, « Tester la démo », « Réserver 30 min » ; sur mobile « La démo » et « 30 min ».
  Une seule rangée (règle navbar), pas de burger.
- Ancres (`allerSection`) : la hauteur de la barre est comptée même quand elle est masquée, pour que la
  section n'atterrisse pas dessous au moment où elle apparaît.
- Les liens de section restent dans le pied de page.

## Contrats à ne pas casser

`data-launch-demo`, `#demo` et la scène 3D unique, scroll-spy (`data-section` du farfadet), `#step-*`
(liens entrants), `?poi=` / `&demo=1`, `.masthead-bg` lu par les ancres, lien « Descendre » du hero.

## `VENTE.md`

- Livré : l'application autonome s'installe aussi sur le portable du commercial (visio, rendez-vous).
- Supports : la landing parle de salon, showroom, rendez-vous et visio.
- Journal : retour du directeur commercial et restructuration.

## Hors v1

Animation 3D du hero, visuels animés sur ordinateur, sort de « Le défi » et « Ce que vous gagnez ».

## Vérification

Rendu 375 / 500 / 1440 ; largeur du document = largeur de la fenêtre sur mobile ; défilement automatique,
pause, glissement, apparition / disparition de la navbar, ancres à 24 px sous la barre, aucune erreur console ;
`prefers-reduced-motion` émulé. Validation visuelle par l'utilisateur.
