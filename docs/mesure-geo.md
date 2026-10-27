# Mesure GEO : est-ce que les assistants nous citent ?

Journal de mesure de la visibilité de `fractal-innov.fr/stand/` dans les réponses des assistants. Un passage = les mêmes questions, posées de la même façon, à date fixe. On compare les passages entre eux, jamais un passage seul à une impression.

## Protocole

1. **Sans mémoire, sans compte si possible.** Conversation temporaire (ChatGPT), mémoire coupée, navigation privée. Sinon l'assistant te connaît déjà et le résultat est faussé.
2. **Recherche web activée** dans chaque moteur, et la question collée telle quelle, sans rien ajouter.
3. **Une question = une nouvelle conversation.**
4. **On note ce qui est dit, pas ce qu'on espère** : codes ci-dessous, plus les concurrents et les sources citées (le domaine suffit).
5. **Les questions ne changent pas d'un passage à l'autre.** Une nouvelle question s'ajoute en bas avec sa date d'entrée, elle n'en remplace aucune.
6. **Q1 et B1 se posent deux fois** dans chaque moteur : si les deux réponses diffèrent, c'est le bruit de l'assistant, pas un effet de nos correctifs.

Protocole complet et indicateurs (présence, recommandation, part de voix) : `Needle5/.claude/skills/veilleur/mesure.md`.

Codes : **R** = Fractal Innov recommandé (nommé comme solution) ; **C** = cité en source, avec lien vers le site ; **M** = mentionné sans lien ; **0** = absent.

## Les questions

Écrites avec les mots d'un acheteur, sans notre nom (Q1 à Q8), puis deux questions de marque (B1, B2) qui testent si l'assistant sait qui nous sommes.

| # | Question | Étape | D'où elle vient |
| --- | --- | --- | --- |
| Q1 | Bonjour, je recherche une société qui peut me permettre de faire des représentations 3D de ce que font nos machines industrielles, qui sont trop grosses pour être déplacées sur des salons. | Recherche de prestataire | Binôme de l'atelier IA SEO, 14/10 |
| Q2 | Comment présenter sur un salon professionnel une machine trop lourde ou trop coûteuse à transporter ? | Découverte | Douleur n° 1, produit absent |
| Q3 | Comment faire une démonstration produit sur un salon quand notre produit est encore un prototype ? | Découverte | Greentech, 08/10 |
| Q4 | Quel prestataire en France pour une borne tactile qui présente notre produit en 3D sur notre stand ? | Recherche de prestataire | Offre |
| Q5 | Existe-t-il une présentation 3D interactive pour salon qui fonctionne sans wifi ni connexion internet ? | Évaluation | FAQ de la page |
| Q6 | Comment occuper les visiteurs de notre stand quand toute l'équipe commerciale est déjà en rendez-vous ? | Découverte | Rééduca, 18/09 |
| Q7 | Comment montrer notre gamme complète sur un petit stand de salon ? | Découverte | Rééduca, 18/09 |
| Q8 | Quel prestataire peut montrer notre produit en réalité augmentée à l'échelle 1 pendant nos rendez-vous commerciaux ? | Recherche de prestataire | Rendez-vous du 12/10 |
| B1 | Qui est Fractal Innov ? | Marque | Identité vérifiable |
| B2 | Que propose Fractal Innov pour les salons professionnels ? | Marque | Identité vérifiable |

## Indice préalable : 14/10/2026

Pris par Claude avec son outil de recherche web (ce n'est pas Claude.ai tel qu'un acheteur l'utilise). Page mesurée : l'ancienne landing, avant la v7.
- Q1 : 0. Réponses citées : xpert.digital (réalité augmentée en salon), 3drepublika (cas HEMO, scan Artec), maverickframe (rendu 3D de robot), maquettes imprimées. L'assistant conclut qu'il ne trouve pas de société française spécialisée.
- « Fractal Innov démonstrateur 3D salon » : 0. Aucun résultat sur Fractal Innov ; l'assistant propose « Fractal Systems » (Dubaï), sans lien. La marque n'est pas reconnue, même nommée.

## Passage 0 : 27/10/2026

- **Page mesurée : la v7**, alignée sur la plaquette de synthèse, en ligne depuis le **15/10/2026** (PR #25, fusionnée à 16:03).
- **État de l'indexation le jour de la mesure** (Search Console) : Google a choisi l'accueil `https://www.fractal-innov.fr/` comme canonique de `/stand/` (l'accueil y redirige par meta refresh à 0). La landing est donc indexée sous l'adresse de l'accueil, qui ne sert aux robots sans JavaScript qu'une page de passage. Bing connaît `/stand/` sans inscription à Bing Webmaster Tools.
- **Correctifs publiés entre l'indice et ce passage** : la v7 (15/10), le `lastmod` du sitemap passé au 2026-10-15.

Conditions, à garder identiques aux passages suivants :

| Assistant | Conditions |
| --- | --- |
| ChatGPT | sans compte, navigation privée, un nouveau chat par question |
| Claude | claude.ai, discussion incognito, recherche web seule (mode « Recherche » coupé) |
| Perplexity | sans compte, navigation privée, recherche par défaut |
| Gemini | connecté, discussion temporaire, modèle Pro (sélectionné d'office) |
| Copilot | connecté (connexion obligatoire), personnalisation coupée, navigation privée |

Grille (Q1 et B1 : premier essai / second essai) :

| # | ChatGPT | Claude | Perplexity | Gemini | Copilot |
| --- | --- | --- | --- | --- | --- |
| Q1 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| Q2 | 0 | 0 | 0 | 0 | 0 |
| Q3 | 0 | 0 | 0 | 0 | 0 |
| Q4 | 0 | 0 | 0 | 0 | 0 |
| Q5 | 0 (hors sujet : « salon de coiffure ») | 0 | 0 | 0 | 0 |
| Q6 | 0 | 0 | 0 | 0 | 0 |
| Q7 | 0 | 0 | 0 | 0 | 0 |
| Q8 | 0 | 0 | 0 | 0 | 0 |
| B1 | C / C | C / C | C / C | M / M | C / C |
| B2 | C | C | C | C | C |

Indicateurs, par assistant :

| Assistant | Présence (Q1 à Q8) | Recommandation | Marque (B1, B2) | Bruit (Q1, B1) |
| --- | --- | --- | --- | --- |
| ChatGPT | 0 / 8 | 0 / 8 | 3 / 3 en C | concordant, concurrents stables |
| Claude | 0 / 8 | 0 / 8 | 3 / 3 en C | concordant en code, concurrents variables |
| Perplexity | 0 / 8 | 0 / 8 | 3 / 3 en C | concordant, concurrents identiques |
| Gemini | 0 / 8 | 0 / 8 | 2 / 3 en M, 1 / 3 en C | concordant, noyau stable |
| Copilot | 0 / 8 | 0 / 8 | 3 / 3 en C | concordant en code, aucun concurrent commun |

Part de voix : non calculée (aucune apparition sur les questions d'acheteur).

Concurrents cités (nom, moteur, question) :

- **Digilor** (bornes tactiles) : Claude Q4, Perplexity Q4, Gemini Q4, Copilot Q4
- **Stooko** : ChatGPT Q1 (×2), Q4, Q8 ; Gemini Q1 (×2)
- **3D Interactions** : ChatGPT Q1, Gemini Q4, Copilot Q1
- **Visuality** (AR sans application) : ChatGPT Q8, Perplexity Q5, Gemini Q8
- **Metasense** (« démonstrateurs 3D interactifs pour salons ») : Perplexity Q4 (recommandé en premier), Q5, Q8
- **Symétrie 3D** : ChatGPT Q1 (×2), Perplexity Q1 (×2)
- **Visao** (jumeaux numériques de machines, AR) : Gemini Q1 (×2)
- **Maverick Frame** : Perplexity Q1 (×2), Gemini Q1, Copilot Q1
- **Synthes'3D** : ChatGPT Q1, Gemini Q1, Q4
- **Vectary** (visionneuse 3D hors ligne) : ChatGPT Q5, Claude Q5
- **Display Media** : ChatGPT Q4, Claude Q4
- **Augment** (« Field Sales ») : Claude Q8 ; **4CAD Group** (« AR Sales ») : Copilot Q8
- Autres cités (une ou deux fois) : dotprod, IMASCIENCE, Itekube, Attractive Labs, 3Dswipe, 3DCREATION, Purple Reality, Realitim, Point Flottant, Animoz, Holovisio, TechViz, Tharsis, Lumiscaphe, Dassault 3DEXCITE, Holoprods, WebRotate 360, Frame Sixty, Plattar, Conseil 3D, RCad'Touch, id3D Studio, Comète, Serious Frames, R&M Consultants, Vuframe, MTC Modellbau, La Borne Multimédia, Digitronix, K2 Corp, Ubiqua, District 3D, Augmentalix, Virtual Odyssey, Obrive, ARGO, Arthur Conception, N-etudes, Artefacto, Pharos Digital, Wanadev, Kaviar Tech, Digital Broker, Eurolocation, Borne Concept, Digital-Events, S3D Engineering, SCAD Engineering, Electron Industrie, Digital Strada, industrial.film, Huntertainment, Reality, RetailVR, Wonder Partner's, Bear SAS, Intuiface, Ventuz

Sources citées le plus souvent (domaine, nombre de liens relevés dans les réponses collées) :

- Sites de prestataires, sur **une page dédiée à la question** : symetrie-3d.fr (9), stooko.fr (5), meta-sense.fr (5), visuality.fr (4), digilor.fr (4), maverickframe.com (5), 3dinteractions.fr (4), vectary.com (2)
- Blogs de conseil aux exposants : s-com.eu (7), jecreemonstand.com (6), totmexposition.com (2), standiste.net (2), ctn-event.com (2)
- Guides et blogs généralistes : seineetmarne.cci.fr (4), shopify.com (5), blog.hubspot.fr (2)
- Annuaires et presse : lafabriquedunet.fr (2), lespepitestech.com (2), europages.fr, hellopro.fr, clubic.com, maddyness.com, digitalengineering247.com (2)
- Sur Fractal Innov : linkedin.com (page entreprise et profils, la source la plus citée), fractal-innov.fr/stand/, pappers.fr, infogreffe.fr, theorg.com, cbinsights.com, net1901.org, la racine du serveur de la démo (Scalingo)
- Sans aucune source : la plupart des réponses de méthode (Q2, Q3, Q6, Q7) chez ChatGPT, Claude, Gemini et Copilot ; Perplexity cite toujours

Ce que les assistants disent de Fractal Innov quand ils en parlent (exact ? daté ?) :

- **Exact et fidèle à la v7** : Perplexity (B1, « démonstrateurs 3D interactifs pour salons, showrooms et sites web », produit « trop grand, trop lourd, confidentiel ou pas encore fabriqué »), Copilot (B1, B2 : jumeau numérique à partir des CAO, télécommande sur smartphone, hors ligne avec mini-PC, statistiques, réutilisation en rendez-vous), Claude B2 (après lecture directe de `/stand/`, sa recherche n'ayant pas trouvé la page).
- **Exact mais ancien positionnement** : ChatGPT (B1, B2), tiré de LinkedIn et du registre : ingénierie numérique, 3D, AR, WebXR, exemple Midipile ; ni stand, ni aide à la vente.
- **Erroné** :
  - un **prix et un délai** (« premier projet en ligne en 15 jours, à partir de 4 900 € ») : Claude B1 (×2, attribué « à son site »), Perplexity B2. Origine : anciennes pages encore publiées sur le domaine (dépôt agence) et copie périmée d'une page déménagée ;
  - une **adresse de contact** qui n'est plus la bonne (`contact@`) : Claude B1 ;
  - « projets de **bâtiments** pour les collectivités », « études techniques liées au bâtiment » : Gemini B1 (×2), via The Org et Infogreffe ; le même classement apparaît dans un annuaire automatique (Omizi) ;
  - « **association** » : net1901.org, repris en filigrane par Copilot ;
  - Copilot B2 laisse croire que la borne tactile est fournie (elle est louée par le client).
- **Datation** : aucun assistant ne date ce qu'il dit de Fractal Innov.

Enseignements pour la suite (détail dans la roadmap de la mission) :

1. Les concurrents cités ont **une page par question** ; la landing en couvre beaucoup, sur une seule adresse que Google range sous l'accueil.
2. Sur les questions de méthode (Q2, Q3, Q6, Q7), les assistants ne nomment personne, ou citent des **contenus de conseil aux exposants** : une place à prendre par le conseil, pas par la vente.
3. **Cases vides** : Copilot Q4 (aucune agence 3D nommée) et Q5 (il décrit un mini-PC avec une présentation WebGL hors ligne, sans prestataire).
4. **Mots des assistants absents de la page** : réalité augmentée, échelle 1, sans application à installer, aide à la vente, jumeau numérique, visualisation 3D industrielle, prototype augmenté, démo en libre-service. « Salon » seul est ambigu : écrire « salon professionnel ».
5. **Objection relevée** : la confidentialité d'un modèle 3D publié (réponse donnée par un assistant : un modèle allégé ne permet pas la rétro-ingénierie).
