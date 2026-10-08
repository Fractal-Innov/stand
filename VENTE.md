# STAND : fiche de vente

Source de vérité de l'offre. Tout support (landing, démonstrateur, brochure) doit lui être conforme. Mise à jour à chaque fait nouveau, daté dans le journal.

## En une phrase

Le démonstrateur 3D de stand de Fractal Innov (nom interne : STAND, jamais affiché depuis le 30/09/2026) est un kiosque d'exposition interactif qui met le produit du client en 3D sur un écran tactile, avec ses vidéos et ses fiches, piloté depuis un téléphone, et qui fonctionne sans réseau. Le client garde l'outil et le réutilise après le salon.

## Le pitch en 30 secondes

« Sur un salon, vous avez trois minutes pour vous faire comprendre, et votre produit est souvent trop grand, trop fragile ou pas encore fini pour être là. le démonstrateur le remplace par son jumeau 3D : le visiteur l'explore du doigt, comprend seul le problème et la solution, et votre commercial reprend la conversation avec le même support à chaque fois. Le kit tient dans une caisse, tourne sans wifi, et vos équipes changent les contenus elles-mêmes. Ce n'est pas un stand pour un salon, c'est un outil de vente que vous gardez. »

## À qui le vendre

- Industriels et fabricants dont le produit ne monte pas sur un stand : machines, équipements lourds, systèmes intégrés, produits en cours de développement.
- Entreprises qui font plusieurs salons par an ou ont un showroom : la réutilisation est l'argument économique.
- Interlocuteurs : direction commerciale, marketing produit, responsable salons. Le mot qui parle à chacun : « attirer » (marketing), « expliquer sans moi » (commercial), « réutiliser » (direction).
- Sur un stand, chercher celui qui a signé le bon de commande du stand, pas le commercial de terrain.
- **Ne pas viser** (leçon de Rééduca, 30/09/2026) : les exposants à stand de quelques mètres carrés et à budget salon serré. Le démonstrateur se paie sur un produit qu'on ne peut pas montrer et sur plusieurs salons ou un showroom ; un petit stand avec un produit transportable n'a ni la douleur ni le budget. Question de tri sur place : « Combien de salons par an, et avez-vous un showroom ? »

## Les trois douleurs

1. Le produit est absent : trop grand, trop fragile, trop cher à déplacer, ou pas fini.
2. Le stand ne raconte rien tout seul : tant qu'un commercial n'est pas libre, chacun explique à sa façon.
3. Trois minutes ne suffisent pas : un produit complexe ne s'explique pas d'un coup d'œil.

## Ce que le visiteur vit (à faire tester, pas à décrire)

- Le produit en 3D, sous tous les angles, du bout du doigt.
- Un menu qui guide la visite : chaque sujet amène la caméra au bon endroit, avec vidéo ou fiche au moment où la question se pose.
- Bilingue FR / EN d'un geste.
- La démo revient seule à sa vue de départ pour le visiteur suivant.

La démo web publique (https://stand-demonstrateur.osc-fr1.scalingo.io/, intégrée sur https://www.fractal-innov.fr/stand/) est le meilleur argument : la faire ouvrir sur le téléphone du prospect pendant l'échange. Elle reste éveillée : un moniteur UptimeRobot, mis en place par l'associé, l'interroge toutes les 5 minutes et alerte par e-mail si elle tombe (vérifié le 30/09/2026 : réponse en 0,06 s). Avant un salon ou une relance, l'ouvrir une fois pour s'en assurer.

## Ce que le client achète

| # | Bénéfice | Preuve dans le produit |
|---|---|---|
| 01 | Attirer | expérience interactive plutôt que panneau ; écran de veille 3D en option |
| 02 | Expliquer | jumeau 3D + parcours guidé + contenus au bon moment, sans attendre un commercial |
| 03 | Faire vendre | le commercial pilote depuis son téléphone (QR + PIN, sans appli) et s'appuie sur le même récit à chaque conversation |
| 04 | Réutiliser | même contenu en showroom, en rendez-vous, sur les salons suivants ; contenus modifiables par l'équipe du client, sans développeur |
| 05 | Mesurer le salon | statistiques Umami : visites par jour, boutons (CTA) touchés, médias vus jusqu'au bout, événements d'interaction ; synchronisées quand une connexion apparaît |
| 06 | Montrer toute la gamme | plusieurs produits dans la même expérience : **sur devis** |

## Ce qui est livré

- **L'expérience** : le jumeau 3D du produit, le parcours, l'affichage des vidéos et fiches FR / EN du client, la régie d'administration (accès par code), la télécommande téléphone. Application autonome (Electron) sur le PC du client, qui s'installe aussi sur le portable du commercial (showroom, rendez-vous, visio avec partage d'écran). Les statistiques de visite se synchronisent quand une connexion apparaît.
- **Le principe** (07/10/2026) : accessible sur un maximum d'appareils, avec le moins d'équipement spécifique. Fractal Innov est fournisseur de solution logicielle, pas standiste : le PC et le routeur sont un complément, le mobilier et le flight case passent par nos partenaires, avec leurs propres délais.
- **Le kit hors ligne** : mini PC préparé, routeur de voyage (réseau fermé, indépendant du wifi du lieu), câbles, alimentation. Installation par le client en dix minutes, quatre câbles. Guide d'une page. Support à distance **avant** le salon pour l'installation et le setup.
- **Deux façons d'avoir le kit** : Fractal Innov l'achète, le configure et le livre prêt à brancher (le client en est propriétaire), ou le client achète sur nos références et nous installons à distance ou en atelier.
- **Options sur devis** : plusieurs produits ou toute une gamme dans la même expérience, modélisation 3D (conversion + optimisation, dépend des fichiers du client), mobilier et présentoir avec nos partenaires, flight case, écran de veille 3D animé, présentation à emporter sur mobile (le visiteur scanne un QR code et retrouve la présentation sur son téléphone ; demande un hébergement en ligne, chiffré au devis).

## Ce qui n'est PAS dans l'offre (à dire clairement, ça rassure)

- Les écrans tactiles : loués sur place par le client auprès de son loueur de salon, à chaque événement (ni stockage, ni transport, ni obsolescence). Prérequis : entrée HDMI et sortie USB tactile.
- Le téléphone ou la tablette de pilotage : celui du client, avec un navigateur, rien à installer. Rien à louer pour le pilotage.
- Les vidéos et fiches : produites par le client, STAND les affiche.
- Une équipe sur place et un stock de rechange : le kit est conçu pour ne demander personne.
- Le support pendant le salon.
- Le mode en ligne en standard : la seule exception est la présentation à emporter sur mobile, option sur devis.
- Le redémarrage automatique du mini PC et le lancement automatique de l'expérience : possibles en option, pas en standard. Ne pas le promettre.

## Formules et prix

- **Aucun prix annoncé**, ni sur la page ni dans les relances : la section tarifs a été retirée de la landing le 23/09/2026 ; confirmé le 30/09/2026. Les anciens montants ne sont à recopier nulle part.
- **Aucun délai annoncé** : il dépend de trop de critères (données du client, contexte de déploiement). Délai et prix sont fixés au devis, **après l'atelier**.
- Confirmé le 05/10/2026 : même le document « De l'appel à votre salon » n'affiche aucune durée. Un projet peut prendre 4 semaines comme 16 selon l'objectif fixé à l'atelier.
- Sur devis : modélisation 3D, plusieurs produits ou toute la gamme, mobilier, flight case, écran de veille 3D, présentation à emporter sur mobile.

## Le processus de vente

1. **Appel de 30 minutes, gratuit et sans engagement** : le prospect décrit son produit et son prochain salon ; on vérifie que le démonstrateur répond au besoin et on prépare l'atelier. Ce n'est **pas** l'atelier.
2. **L'atelier** (2 h, en visio par défaut, sur site si le client le juge nécessaire) : qualifie le besoin et réunit tout ce qu'il faut pour le devis. Le client présente ses fichiers 3D, photos et vidéos en partage d'écran, avec les personnes qui peuvent les fournir ; il nous en donne l'accès une fois le devis validé. **Pas de facturation à part** : son coût est intégré au devis, et payé seulement si le projet est lancé (décidé le 30/09/2026). À dire ainsi : « l'atelier est compris dans le projet ».
3. **Le devis et le délai**, issus de l'atelier, **remis sous 24 h**. Un imprévu sur la date de l'atelier se règle par message direct, pas par un lien de réservation.
4. Production à partir des fichiers du client, puis livraison du kit avant le salon.

## Objections courantes

- « On a déjà des vidéos » : elles sont dedans, au bon moment du parcours, et le visiteur les choisit lui-même.
- « Pas de wifi sur le salon » : le kit embarque son réseau, c'est justement conçu pour ça.
- « Nos équipes ne sont pas techniques » : régie par code, contenus changés sans développeur, installation en quatre câbles.
- « C'est pour un seul salon » : non, c'est l'argument central : showroom, rendez-vous, salons suivants.
- « On n'a pas de fichiers 3D » : on l'évalue à l'atelier ; photos et plans suffisent souvent pour démarrer, la modélisation est alors sur devis.
- « Combien ça coûte ? » : cela dépend du produit et des fichiers ; le devis suit l'atelier, et l'atelier est compris dans le projet. Jamais de fourchette.
- « Qui est sur place pendant le salon ? » : personne, et c'est voulu ; accompagnement avant le salon.

## Preuve

Un premier acteur industriel, sous NDA : « nous ne pouvons pas le citer, nous pouvons vous raconter comment nous l'avons accompagné ». Rien de ce client n'apparaît sur la page, pas même un fait anonyme (décidé le 30/09/2026).

**En attendant une référence, la démo publique est la preuve** : la page invite à la manipuler, puis enchaîne sur l'appel (« avec votre produit à la place de ce stand »).

**Devenir une référence : une opportunité, jamais une condition.** Au moment du devis, on propose au client, s'il le souhaite, d'être cité après son salon (nom, logo, une phrase, une photo du stand) pour une promotion mutuelle : sa présence sur nos supports, la nôtre sur les siens. Le devis est le même qu'il dise oui ou non ; un refus ne se discute pas.

- Formulation type : « Si l'idée vous plaît, votre salon peut devenir une vitrine pour vous comme pour nous : après l'événement, nous le présentons sur notre page, avec votre accord sur chaque mot. En remerciement, [contrepartie à confirmer]. C'est une proposition, pas une condition. »
- Quand la proposer : à la remise du devis, pas avant (elle ne doit pas peser sur la décision d'achat).
- Ce que le client valide : le texte, les visuels et la date de publication, par écrit.
- Contrepartie (état au 30/09/2026) : **pas de remise**, la trésorerie doit financer la suite de l'activité. Piste retenue mais non confirmée : une mise à jour offerte (contenus ou produit) avant son salon suivant. D'autres pistes restent à étudier avec l'associé, dont une publication croisée (article, post LinkedIn) qui ne coûte rien.

## Supports

- Landing https://www.fractal-innov.fr/stand/ : accroche et prise de contact. Lue comme une présentation produit (hero, six points forts, puis le détail) ; elle parle de salon, showroom, rendez-vous et visio, pas seulement de salon. Calendrier https://calendar.app.google/SDuiKb9ZBQ6BcbED6, carte de visite https://s.blinq.me/wEhJoOeZIrvGvSIe46Yy?bs=icl.
- Démonstrateur : montrer le produit.
- Brochure PDF : closing, détails de tout le produit. Pas encore produite.
- « De l'appel à votre salon » (PDF, 2 pages en double page) : remis après l'appel de 30 minutes, et affiché comme média dans la démo (parfois avant l'appel). Six étapes sans durée (Échanger, Cadrer, Lancer, Partager vos fichiers, Produire et valider, Installer), points de décision signalés (Ensemble, Vous décidez, Vous validez), puis la liste « Pour préparer l'Atelier ». Générateur et versions : dépôt privé Fractal-Innov/marketing (`brochures/`).

## Journal

- 2026-09-17 : landing réécrite pour coller à l'offre (écran non fourni, options sur devis, prix affichés, FAQ objections). Prix rendus publics « dans un premier temps ».
- 2026-09-18 : salon Rééduca, Paris Porte de Versailles. Douze exposants ciblés, en deux niveaux de priorité : fabricants d'équipements de rééducation et de bien-être (balnéothérapie, dispositifs motorisés, réalité virtuelle, mobilier et aménagement de cabinet). La liste nominative est tenue hors de ce dépôt public.
- 2026-09-18, fin de salon : cinq contacts qualifiés sur leur stand (fabricant de lits hydromassants, VR et plateformes motorisées, rameurs design, attelles motorisées, cabinets clés en main). Douleurs entendues : produit trop gros pour venir, salons jugés trop chers, visiteurs à occuper quand l'équipe est prise, gamme trop large pour le stand, ROI du salon à mesurer. Relance par e-mail avec lien calendrier ; le détail nominatif est tenu hors de ce dépôt public.
- 2026-09-23 : section tarifs retirée de la landing.
- 2026-09-30 : pivot décidé avec l'associé. Le démonstrateur de stand est la seule offre qui a rapporté ; www.fractal-innov.fr renvoie vers cette landing. Une seule marque, Fractal Innov : plus de nom produit affiché (« STAND » reste le nom du dépôt). Aucun prix ni délai annoncé ; l'appel de 30 min précède l'atelier, le devis suit l'atelier. Douleurs de Rééduca ajoutées à la page : la gamme (sur devis) et la mesure du salon (statistiques Umami).
- 2026-09-30, cohérence de la page : « Ce que vous gagnez » dit les résultats, « Le jumeau 3D » les fonctions ; la télécommande n'est détaillée qu'une fois ; FAQ : « Combien ça coûte ? » remplace « C'est pour un seul salon ? » ; « pas de fichiers 3D » reste en FAQ sous l'angle du coût (modélisation sur devis), la note sous le jumeau garde l'angle « des photos suffisent ». Pas de scène 3D dans « Ce que vous gagnez » (même stand trois sections de suite). « Emporter sur mobile » devient une option sur devis (hébergement en ligne).
- 2026-09-30, suivi Rééduca : silence des cinq contacts après la première relance ; un e-mail n'est pas parti (adresse erronée). Requalification : la plupart tiennent de petits stands à budget serré, en décalage avec l'offre. Trois gardent la douleur « produit absent » (lits hydromassants, plateformes motorisées, cabinets clés en main) et reçoivent une relance n° 2 de qualification ; les deux autres (produits transportables) un dernier message porte ouverte, puis clôture. Leçon ajoutée dans « À qui le vendre ».
- 2026-10-01, retour d'un directeur commercial sur la landing : soignée, on a envie d'y rester, mais exhaustive au point de neutraliser la curiosité ; l'aborder comme une présentation de produit. Restructuration du haut de page sur le modèle des pages produit Apple : hero épuré, six points forts en slider (interface épurée, tous les écrans, télécommande, fluidité de la 3D, produit présenté sans le transporter avec la gamme en option, statistiques sans cookie ni donnée personnelle), barre qui apparaît aux Points forts. « Le défi » et « Ce que vous gagnez » gardés, à revoir après. Le démonstrateur se vend aussi pour le showroom, les présentations sur site et la visio.
- 2026-10-02 : le slider des points forts devient une grille « bento » statique. Un carrousel à défilement automatique n'est vu qu'à sa première slide et cache les cinq autres ; la grille montre les six points forts d'un regard, sans mouvement imposé.
- 2026-09-30, étape 3 (preuve) : pas de référence citable, la démo sert de preuve (passage vers l'appel sous la démo). Clause de référence ajoutée, proposée comme une opportunité au devis ; contrepartie à confirmer, sans remise.
- 2026-10-07 : préparation du premier appel découverte avec un prospect de Rééduca. Positionnement précisé : solution logicielle, pas standiste ; PC et routeur en complément, mobilier et flight case via nos partenaires (leurs délais) ; écran loué à chaque salon, pilotage sur le téléphone ou la tablette du client (principe : un maximum d'appareils, le moins d'équipement spécifique). Atelier de 2 h en visio par défaut, devis sous 24 h. PDF « De l'appel à votre salon » refait en six étapes ; brochure « Démonstrateur 3D » alignée.
- 2026-10-08 : 8e Rencontre du commerce de la ville où l'agence est installée (invitation du service Développement économique). Le public commerce de proximité ne colle pas à l'offre ; l'élu au commerce et le responsable de l'unité Commerce et Artisanat orientent vers l'élu chargé des entreprises, à contacter de leur part. Piste locale à réorienter du commerce vers les entreprises qui exposent ou reçoivent en showroom ; noms tenus hors de ce dépôt public.
