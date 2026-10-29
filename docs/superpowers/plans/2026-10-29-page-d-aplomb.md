# Remettre la page d'aplomb : plan d'implémentation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Faire en sorte que Google, Bing et les IA lisent, rangent et mesurent correctement `https://www.fractal-innov.fr/stand/` (v7 du 15/10/2026), en traitant ce qui reste ouvert après le passage de mesure 0 du 27/10/2026 (levier 1 du plan entrant, semaines 1 et 2).

**Architecture:** Trois livraisons. (1) Une branche du dépôt `stand` qui modifie `index.html` par scripts Python (FAQ en vraies questions et nœud `FAQPage` resynchronisé, mesure Umami) et ajoute deux outils non publiés, `outils/verif_seo.py` et `outils/faq_jsonld.py`. (2) Une branche du dépôt racine `Fractal-Innov.github.io` : `llms.txt` et date du plan du site. (3) Des actions manuelles et une décision : l'adresse que Google retient pour la page (aujourd'hui l'accueil), Search Console, Bing, aperçu de la démo (Needle5), page « village ».

**Tech Stack:** HTML statique publié par GitHub Pages ; Python 3 (bibliothèque standard seulement) ; Umami Cloud (`https://cloud.umami.is`) ; Google Search Console ; Bing Webmaster Tools.

**Spec:** document « FractalInnov, stratégie marketing digitale », onglet « Plan entrant · Hugo », levier 1 (https://claude.ai/artifact/UEzYF68yzFzJkzPmB4pJ8A), corrigé par l'état constaté le 29/10/2026 dans `docs/cadrage-seo-geo.md` et `docs/mesure-geo.md` (passage 0). Ce qui est déjà fait n'est pas refait : titre et H1 de la v7, `FAQPage` présent, `robots.txt` ouvert aux IA, PageSpeed mobile 99 / 94, page indexée dans Search Console.

## Global Constraints

- `index.html` s'édite par script Python avec `assert s.count(old) == 1`, jamais avec l'outil Edit.
- Tout texte visible suit `CLAUDE.md` et `VENTE.md` : l'offre se dit « le démonstrateur 3D de votre produit », exemples salon d'abord ; aucun prix, aucun délai ; jamais « STAND » visible ; jamais de nom d'outil de statistiques visible ; en ligne et hors ligne sont deux diffusions du même contenu 3D, sans synchronisation promise.
- La page suit la plaquette de synthèse : toute reformulation visible (ici, les questions de la FAQ) se valide avec Corentin avant la PR.
- Texte visible : jamais de tiret cadratin « — », pas de point final dans les titres, `&nbsp;?` avant le point d'interrogation.
- Le workflow du dépôt `stand` publie une liste blanche (`index.html`, `favicon.ico`, `site.webmanifest`, `assets/`, `CNAME`) : `outils/` et `docs/` ne partent jamais en ligne.
- Le dépôt racine `Fractal-Innov.github.io` publie sa branche `main`.
- La démo se modifie dans Needle5 (`Needle5/Needle/Salon`), jamais dans le miroir `salon_demo_app`.
- Mesure GEO : les questions et le protocole sont ceux de `docs/mesure-geo.md`, sans en changer une.
- Une branche et une PR par livraison ; Hugo fusionne. Conventional Commits en français, pied `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. `git add` avec des chemins explicites (ne jamais ajouter `docs/proposition-refonte-page.md`).

## Review Focus

- **Visites locales comptées :** ouvrir la page en local ou en aperçu ne doit rien envoyer à Umami (`data-domains`). Contrôle et test réseau en Tâche 2.
- **Bloqueur de publicité :** `cloud.umami.is` bloqué, le calendrier s'ouvre et la démo se lance quand même. Test manuel en Tâche 2.
- **Clic sur le calendrier :** l'attribut d'événement n'empêche pas la navigation et n'ouvre pas deux onglets. Test manuel en Tâche 2.
- **FAQ modifiée plus tard à la main :** le nœud `FAQPage` doit suivre. `verif_seo.py` échoue s'ils divergent (Tâche 1).
- **Accents de `llms.txt` :** servi en UTF-8, sinon les IA lisent « dÃ©monstrateur ». Contrôle `curl -sI` en Tâche 5.

---

### Tâche 1 : l'outil de contrôle et la FAQ en vraies questions

**Files:**
- Create: `outils/verif_seo.py`
- Create: `outils/faq_jsonld.py`
- Modify: `index.html` (6 titres `<h3>` de `#questions`, nœud `FAQPage` du bloc JSON-LD de `<head>`)

**Interfaces:**
- Produces: `outils/verif_seo.py` avec `normaliser(texte) -> str`, `lire_page(html) -> Page` (attributs `faq: list[list[str]]` de paires `[question, réponse]`, `jsonld: list[str]`, `scripts: list[dict]`, `liens: list[dict]`, `lanceurs: list[dict]`, `visible: list[str]`), `trouver_faq_ld(blocs) -> list | None`, `controles(page) -> list[tuple[str, bool, object]]`, `main(argv) -> int`. La Tâche 2 ajoute `controle_mesure` et la branche dans `controles`.
- Produces: `outils/faq_jsonld.py` : `python3 outils/faq_jsonld.py [index.html]` remplace le nœud `FAQPage` du `@graph` par la FAQ visible. À relancer après toute modification de `#questions`.

- [ ] **Step 1: Valider les nouvelles questions avec Corentin**

Envoyer à Corentin le tableau ci-dessous ; attendre son accord (ou ses corrections, à reporter dans `QUESTIONS_ATTENDUES` et le Step 6). Les réponses ne changent pas.

| Aujourd'hui | Proposé |
| --- | --- |
| Peut-on l'avoir sur notre site ? | inchangé |
| Nous avons déjà des vidéos | Peut-on utiliser nos vidéos existantes ? |
| Il n'y a pas de wifi sur le salon | Le démonstrateur fonctionne-t-il sans wifi sur le salon ? |
| Nos équipes ne sont pas techniques | Faut-il des compétences techniques pour l'utiliser ? |
| Combien ça coûte ? | Combien coûte le démonstrateur 3D de notre produit ? |
| Nous n'avons pas de fichiers 3D | Faut-il des fichiers 3D de notre produit ? |
| Qui est sur place pendant le salon ? | inchangé |

Pourquoi : les assistants et Google répondent à des questions ; une objection (« Nous avons déjà des vidéos ») ne correspond à aucune question tapée par un acheteur.

- [ ] **Step 2: Créer la branche**

```bash
cd /Users/hugsdaniel/code/HugsDaniel/freelance/FractalInnov/stand_landing_official
git switch master && git pull
git switch -c feat/page-aplomb
```

- [ ] **Step 3: Écrire l'outil de contrôle**

Créer `outils/verif_seo.py` :

```python
#!/usr/bin/env python3
"""Contrôles de la page /stand pour le levier 1 du plan entrant (SEO et GEO).

Usage : python3 outils/verif_seo.py [chemin/vers/index.html]
Affiche OK ou ÉCHEC par contrôle ; code de sortie 1 s'il y a au moins un
échec (tous les contrôles tournent, pour voir la liste complète).
Fichier de travail : `outils/` n'est pas dans la liste blanche du workflow,
il ne part jamais en ligne.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

QUESTIONS_ATTENDUES = [
    "Peut-on l'avoir sur notre site ?",
    'Peut-on utiliser nos vidéos existantes ?',
    'Le démonstrateur fonctionne-t-il sans wifi sur le salon ?',
    "Faut-il des compétences techniques pour l'utiliser ?",
    'Combien coûte le démonstrateur 3D de notre produit ?',
    'Faut-il des fichiers 3D de notre produit ?',
    'Qui est sur place pendant le salon ?',
]


def normaliser(texte):
    """Espaces insécables en espaces, blancs regroupés, bords retirés."""
    return re.sub(r'\s+', ' ', texte.replace('\xa0', ' ')).strip()


class Page(HTMLParser):
    """Relève ce que les contrôles regardent : FAQ, JSON-LD, scripts, liens."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.faq = []          # [[question, réponse]], dans l'ordre de la page
        self.jsonld = []       # contenus bruts des blocs application/ld+json
        self.scripts = []      # attributs des <script src=…>
        self.liens = []        # attributs de tous les <a>
        self.lanceurs = []     # attributs des éléments data-launch-demo
        self.visible = []      # texte hors <script> et <style>
        self._capture = None   # 'q' | 'r' | 'ld'
        self._fin = None       # balise qui termine la capture
        self._texte = []
        self._dans_faq = False
        self._cache = 0        # profondeur dans <script> / <style>

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style'):
            self._cache += 1
        if tag == 'a':
            self.liens.append(a)
        if 'data-launch-demo' in a:
            self.lanceurs.append(a)
        if tag == 'section' and a.get('id') == 'questions':
            self._dans_faq = True
        if self._capture:
            return
        if self._dans_faq and tag == 'h3':
            self._debut('q', 'h3')
        elif (self._dans_faq and self.faq and tag in ('p', 'li')
              and 'faq-more' not in (a.get('class') or '')):
            self._debut('r', tag)
        elif tag == 'script' and a.get('type') == 'application/ld+json':
            self._debut('ld', 'script')
        elif tag == 'script' and a.get('src'):
            self.scripts.append(a)

    def _debut(self, quoi, fin):
        self._capture, self._fin, self._texte = quoi, fin, []

    def handle_data(self, data):
        if self._capture:
            self._texte.append(data)
        if not self._cache:
            self.visible.append(data)

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self._cache -= 1
        if tag == 'section':
            self._dans_faq = False
        if self._capture and tag == self._fin:
            texte = ''.join(self._texte)
            if self._capture == 'ld':
                self.jsonld.append(texte)
            elif self._capture == 'q':
                self.faq.append([normaliser(texte), ''])
            else:
                self.faq[-1][1] = normaliser(self.faq[-1][1] + ' ' + texte)
            self._capture = None


def lire_page(html):
    page = Page()
    page.feed(html)
    page.close()
    return page


def trouver_faq_ld(blocs):
    """Paires [question, réponse] du premier nœud FAQPage trouvé, sinon None."""
    for brut in blocs:
        donnees = json.loads(brut)
        noeuds = donnees.get('@graph', [donnees]) if isinstance(donnees, dict) else donnees
        for n in noeuds:
            if n.get('@type') == 'FAQPage':
                return [[e['name'], e['acceptedAnswer']['text']] for e in n['mainEntity']]
    return None


def controle_faq(page):
    questions = [q for q, _ in page.faq]
    faq_ld = trouver_faq_ld(page.jsonld)
    return [
        ('FAQ en vraies questions', questions == QUESTIONS_ATTENDUES, questions),
        ('FAQ : une réponse non vide par question',
         len(page.faq) == len(QUESTIONS_ATTENDUES) and all(r for _, r in page.faq), page.faq),
        ('Nœud FAQPage identique à la FAQ visible', faq_ld == page.faq, faq_ld),
    ]


def controles(page):
    return controle_faq(page)


def main(argv):
    chemin = Path(argv[1] if len(argv) > 1 else 'index.html')
    page = lire_page(chemin.read_text(encoding='utf-8'))
    echecs = 0
    for nom, ok, detail in controles(page):
        print(('OK     ' if ok else 'ÉCHEC  ') + nom)
        if not ok:
            print(f'       obtenu : {detail}')
            echecs += 1
    print(f'\n{echecs} échec(s)')
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Lancer le contrôle et le voir échouer**

Run: `python3 outils/verif_seo.py index.html`
Expected: `ÉCHEC  FAQ en vraies questions` (obtenu : « Nous avons déjà des vidéos »…), `OK     FAQ : une réponse non vide par question`, `OK     Nœud FAQPage identique à la FAQ visible`, `1 échec(s)`. Si le deuxième ou le troisième échoue, le relevé de la page est faux (ou le nœud écrit à la main diverge déjà) : lire le détail `obtenu` et corriger `Page` avant de continuer.

- [ ] **Step 5: Écrire le générateur du nœud FAQPage**

Créer `outils/faq_jsonld.py` :

```python
#!/usr/bin/env python3
"""Remplace le nœud FAQPage du JSON-LD de index.html par la FAQ visible.

Usage : python3 outils/faq_jsonld.py [chemin/vers/index.html]
À relancer après toute modification de la section #questions : le contrôle
« Nœud FAQPage identique à la FAQ visible » de verif_seo.py échoue sinon.
"""
import json
import re
import sys
from pathlib import Path

from verif_seo import lire_page

BLOC = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)


def noeud_faq(faq):
    return {
        '@type': 'FAQPage',
        '@id': 'https://www.fractal-innov.fr/stand/#faq',
        'mainEntity': [
            {
                '@type': 'Question',
                'name': question,
                'acceptedAnswer': {'@type': 'Answer', 'text': reponse},
            }
            for question, reponse in faq
        ],
    }


def main(argv):
    p = Path(argv[1] if len(argv) > 1 else 'index.html')
    s = p.read_text(encoding='utf-8')
    blocs = BLOC.findall(s)
    assert len(blocs) == 1, f'{len(blocs)} blocs JSON-LD, 1 attendu'
    donnees = json.loads(blocs[0][1])
    graphe = donnees['@graph']
    places = [i for i, n in enumerate(graphe) if n.get('@type') == 'FAQPage']
    assert len(places) == 1, f'{len(places)} nœuds FAQPage, 1 attendu'
    page = lire_page(s)
    graphe[places[0]] = noeud_faq(page.faq)
    contenu = json.dumps(donnees, ensure_ascii=False, indent=2)
    s = BLOC.sub(lambda m: m.group(1) + '\n' + contenu + '\n  ' + m.group(3), s)
    p.write_text(s, encoding='utf-8')
    print(f'{len(page.faq)} questions écrites dans le nœud FAQPage')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
```

- [ ] **Step 6: Reformuler les questions**

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('index.html')
s = p.read_text(encoding='utf-8')
remplacements = [
    ('<h3>Nous avons déjà des vidéos</h3>',
     '<h3>Peut-on utiliser nos vidéos existantes&nbsp;?</h3>'),
    ("<h3>Il n'y a pas de wifi sur le salon</h3>",
     '<h3>Le démonstrateur fonctionne-t-il sans wifi sur le salon&nbsp;?</h3>'),
    ('<h3>Nos équipes ne sont pas techniques</h3>',
     "<h3>Faut-il des compétences techniques pour l'utiliser&nbsp;?</h3>"),
    ('<h3>Combien ça coûte&nbsp;?</h3>',
     '<h3>Combien coûte le démonstrateur 3D de notre produit&nbsp;?</h3>'),
    ("<h3>Nous n'avons pas de fichiers 3D</h3>",
     '<h3>Faut-il des fichiers 3D de notre produit&nbsp;?</h3>'),
]
for old, new in remplacements:
    assert s.count(old) == 1, (old, s.count(old))
    s = s.replace(old, new)
p.write_text(s, encoding='utf-8')
PY
```

- [ ] **Step 7: Voir le nœud FAQPage diverger, puis le régénérer**

Run: `python3 outils/verif_seo.py index.html`
Expected: `OK     FAQ en vraies questions`, `ÉCHEC  Nœud FAQPage identique à la FAQ visible`, `1 échec(s)`.

Run: `python3 outils/faq_jsonld.py index.html`
Expected: `7 questions écrites dans le nœud FAQPage`

- [ ] **Step 8: Relancer le contrôle et relire le diff du JSON-LD**

Run: `python3 outils/verif_seo.py index.html`
Expected: 3 lignes `OK`, `0 échec(s)`.

Run: `git diff --stat index.html && git diff index.html | grep -c '^[-+] '`
Expected: seuls les titres de la FAQ et le nœud FAQPage changent. Si le bloc JSON-LD entier apparaît modifié (indentation ou ordre), c'est que le fichier n'était pas écrit au format `json.dumps(indent=2)` : vérifier que seules des espaces changent hors du nœud FAQPage, le noter dans le corps du commit.

- [ ] **Step 9: Vérifier le balisage chez Google et à l'écran**

Ouvrir https://search.google.com/test/rich-results, onglet « Code », coller `index.html`.
Expected: « FAQ » détecté, 7 questions, aucune erreur (l'avertissement « pas éligible aux résultats enrichis » est normal : Google réserve cet affichage aux sites publics et de santé ; le balisage reste lu).

Puis `python3 -m http.server 4201`, ouvrir `http://localhost:4201/#questions` à 375 px et 1280 px : chaque question tient dans sa carte, chevron aligné, ouverture et fermeture correctes ; dans la console, `document.documentElement.scrollWidth === window.innerWidth` vaut `true`. Arrêter le serveur.

- [ ] **Step 10: Commit**

```bash
git add outils/verif_seo.py outils/faq_jsonld.py index.html
git commit -m "feat(stand): reformuler la FAQ en vraies questions

Les titres étaient des objections (« Nous avons déjà des vidéos »), pas
les questions qu'un acheteur tape dans Google ou pose à un assistant. Les
réponses ne changent pas. Le nœud FAQPage est désormais généré depuis la
FAQ visible (outils/faq_jsonld.py) et outils/verif_seo.py vérifie qu'ils
restent identiques. Questions validées avec Corentin.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Tâche 2 : mesurer les visites et les clics

**Files:**
- Modify: `outils/verif_seo.py` (ajoute `controle_mesure`)
- Modify: `index.html` (script Umami dans `<head>`, `data-umami-event` sur `#contactPrimary`, `#demoNewTab` et chaque lien `data-launch-demo`)

**Interfaces:**
- Consumes: `lire_page`, `normaliser`, `controles` de la Tâche 1.
- Produces: les événements `reserver-appel`, `tester-demo`, `ouvrir-demo-onglet`, suivis chaque lundi dans le plan entrant.

- [ ] **Step 1: Créer le site dans Umami (manuel, Hugo)**

Sur https://cloud.umami.is, avec le compte qui mesure déjà la démo (`analytics.umamiWebsiteId` de la configuration produit) : « Settings », « Websites », « Add website », nom `Page stand`, domaine `www.fractal-innov.fr`. Copier le « Website ID » (`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`). Sans accès au compte, demander à Corentin de le partager avant de continuer.

- [ ] **Step 2: Ajouter le contrôle de la mesure**

Dans `outils/verif_seo.py`, ajouter sous `QUESTIONS_ATTENDUES` :

```python
UMAMI_SRC = 'https://cloud.umami.is/script.js'
UMAMI_DOMAINE = 'www.fractal-innov.fr'
UUID = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
CALENDRIER = 'calendar.app.google'
```

Ajouter avant `def controles` :

```python
def controle_mesure(page):
    umami = [s for s in page.scripts if s.get('src') == UMAMI_SRC]
    script = umami[0] if len(umami) == 1 else {}
    calendrier = [l for l in page.liens if CALENDRIER in (l.get('href') or '')]
    nouvel_onglet = [l for l in page.liens if l.get('id') == 'demoNewTab']
    texte = normaliser(' '.join(page.visible))
    return [
        ('Script de mesure présent une seule fois', len(umami) == 1, len(umami)),
        ('Script de mesure en defer', 'defer' in script, script),
        ('Identifiant du site au bon format',
         bool(UUID.match(script.get('data-website-id') or '')), script.get('data-website-id')),
        ('Mesure limitée au domaine de production',
         script.get('data-domains') == UMAMI_DOMAINE, script.get('data-domains')),
        ('Clics sur le calendrier mesurés',
         bool(calendrier) and all(l.get('data-umami-event') == 'reserver-appel' for l in calendrier),
         calendrier),
        ('Lancements de la démo mesurés',
         bool(page.lanceurs) and all(l.get('data-umami-event') == 'tester-demo' for l in page.lanceurs),
         page.lanceurs),
        ('Ouverture de la démo dans un onglet mesurée',
         len(nouvel_onglet) == 1 and nouvel_onglet[0].get('data-umami-event') == 'ouvrir-demo-onglet',
         nouvel_onglet),
        ("Aucun nom d'outil de statistiques visible", 'Umami' not in texte, 'Umami'),
        ('Aucun « STAND » visible comme nom de produit', not re.search(r'\bSTAND\b', texte), 'STAND'),
    ]
```

Remplacer `controles` par :

```python
def controles(page):
    return controle_faq(page) + controle_mesure(page)
```

- [ ] **Step 3: Lancer le contrôle et le voir échouer**

Run: `python3 outils/verif_seo.py index.html`
Expected: `ÉCHEC` sur les 7 premiers contrôles de mesure, `OK` sur les deux derniers et sur les 3 de la FAQ, `7 échec(s)`.

- [ ] **Step 4: Ajouter le script et les événements**

Remplacer `COLLER-ICI-LE-WEBSITE-ID` par l'identifiant du Step 1 :

```bash
UMAMI_ID='COLLER-ICI-LE-WEBSITE-ID' python3 - <<'PY'
import os, re
from pathlib import Path
ident = os.environ['UMAMI_ID']
assert re.fullmatch(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', ident), ident
p = Path('index.html')
s = p.read_text(encoding='utf-8')

old = '</head>'
assert s.count(old) == 1, s.count(old)
script = (
    "  <!-- Mesure d'audience sans cookie (Umami Cloud), seulement sur le domaine\n"
    "       de production : en local et en aperçu, rien n'est compté. Les clics\n"
    '       sont nommés par les attributs data-umami-event des liens\n'
    '       (reserver-appel, tester-demo, ouvrir-demo-onglet). Bloqué par un\n'
    '       bloqueur, le script manque et la page marche pareil. -->\n'
    f'  <script defer src="https://cloud.umami.is/script.js" data-website-id="{ident}"\n'
    '    data-domains="www.fractal-innov.fr"></script>\n'
)
s = s.replace(old, script + old)

for old, new in [
    ('id="contactPrimary" href=', 'id="contactPrimary" data-umami-event="reserver-appel" href='),
    ('id="demoNewTab" href=', 'id="demoNewTab" data-umami-event="ouvrir-demo-onglet" href='),
]:
    assert s.count(old) == 1, (old, s.count(old))
    s = s.replace(old, new)

lanceur = re.compile(r'(<a\b[^>]*?\sdata-launch-demo)(?=[\s>])')
n = len(lanceur.findall(s))
assert n >= 1, n
s = lanceur.sub(r'\1 data-umami-event="tester-demo"', s)
print(f'{n} liens data-launch-demo marqués')

p.write_text(s, encoding='utf-8')
PY
```

Expected: `N liens data-launch-demo marqués` (N = nombre de liens « Tester la démo », 3 le 29/10/2026). Si le contrôle « Lancements de la démo mesurés » échoue ensuite, un élément `data-launch-demo` n'est pas un `<a>` : lui ajouter l'attribut à la main par script, avec `assert s.count(old) == 1`.

- [ ] **Step 5: Relancer le contrôle**

Run: `python3 outils/verif_seo.py index.html`
Expected: tous les contrôles `OK`, `0 échec(s)`.

- [ ] **Step 6: Vérifier que rien n'est compté en local**

`python3 -m http.server 4201`, ouvrir `http://localhost:4201/`, onglet Réseau, filtre `umami`, cliquer « Tester la démo ».
Expected: `script.js` se charge, aucune requête vers `cloud.umami.is/api/send`.

- [ ] **Step 7: Vérifier la page avec la mesure bloquée**

Onglet Réseau, clic droit sur `script.js`, « Bloquer l'URL de la requête », recharger. « Tester la démo » lance la démo ; le bouton du calendrier de la section contact ouvre le calendrier une seule fois ; « Ouvrir dans un nouvel onglet » ouvre un seul onglet. Retirer le blocage, arrêter le serveur.

- [ ] **Step 8: Commit**

```bash
git add outils/verif_seo.py index.html
git commit -m "feat(stand): mesurer les visites et les clics de la page

La page n'avait aucune mesure : impossible de savoir quel canal amène des
appels. Ajoute la mesure sans cookie déjà utilisée par la démo, limitée
au domaine de production, et nomme trois clics : réserver un appel,
tester la démo, l'ouvrir dans un onglet.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Tâche 3 : mise en ligne de la page et contrôle en production

**Files:**
- Aucun nouveau fichier.

**Interfaces:**
- Consumes: la branche `feat/page-aplomb`.
- Produces: la page en ligne et sa date de fusion (`AAAA-MM-JJ`), utilisée en Tâche 5.

- [ ] **Step 1: Pousser et ouvrir la PR**

```bash
git push -u origin feat/page-aplomb
gh pr create --base master --title "feat(stand): FAQ en vraies questions et mesure de la page" --body "Levier 1 du plan entrant :

- FAQ reformulée en vraies questions (réponses inchangées, validée avec Corentin), nœud FAQPage généré depuis la FAQ visible
- Mesure sans cookie limitée au domaine de production, trois clics nommés
- outils/verif_seo.py et outils/faq_jsonld.py, hors liste blanche

Contrôle : \`python3 outils/verif_seo.py index.html\` → 0 échec.

🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

- [ ] **Step 2: Hugo relit et fusionne, puis attend la publication**

Run: `gh run watch $(gh run list --branch master --limit 1 --json databaseId -q '.[0].databaseId')`
Expected: le job `deploy` se termine en succès.

- [ ] **Step 3: Contrôler la page en ligne**

```bash
curl -s https://www.fractal-innov.fr/stand/ -o "$TMPDIR/stand.html"
python3 outils/verif_seo.py "$TMPDIR/stand.html"
```

Expected: `0 échec(s)` (cache de 10 minutes : relancer si l'ancienne FAQ revient).

- [ ] **Step 4: Vérifier la mesure en production**

Fenêtre privée sans bloqueur, https://www.fractal-innov.fr/stand/, cliquer « Tester la démo ». Umami, site `Page stand`, vue « Realtime ».
Expected: 1 visiteur et l'événement `tester-demo` dans la minute.

- [ ] **Step 5: Noter la date de fusion**

Run: `git switch master && git pull && git log -1 --format=%cs`
Expected: une date `AAAA-MM-JJ`, à reporter en Tâche 5.

---

### Tâche 4 : décider de l'adresse que Google retient (Hugo et Corentin)

Le passage 0 (`docs/mesure-geo.md`) a établi que Google a choisi l'accueil `https://www.fractal-innov.fr/` comme adresse canonique de `/stand/`. L'accueil redirige par une balise `meta refresh` à 0 ; les robots qui ne la suivent pas n'y lisent qu'une page de passage de 3 Ko. C'est le correctif qui pèse le plus sur le GEO ; il ne s'implémente pas dans ce plan, il se décide.

**Files:**
- Modify: `docs/cadrage-seo-geo.md` (ajouter la décision en fin de fichier)

- [ ] **Step 1: Constater l'état actuel dans Search Console**

Search Console (propriété existante ; si Hugo n'y a pas accès, Corentin l'ajoute comme utilisateur « Complet »), barre « Inspecter » : `https://www.fractal-innov.fr/stand/`. Noter « URL canonique déclarée par l'utilisateur » et « URL canonique sélectionnée par Google ». Recommencer avec `https://www.fractal-innov.fr/`.
Expected: les deux valeurs du passage 0 (déclarée `/stand/`, sélectionnée `/`), ou un changement à noter avec sa date.

- [ ] **Step 2: Choisir une option (30 minutes)**

| Option | Ce qu'on fait | Pour | Contre |
| --- | --- | --- | --- |
| A. Insister | Garder la redirection ; « Demander l'indexation » de `/stand/` ; réinspecter dans 3 semaines | Rien à changer | Google a déjà tranché une fois ; les liens extérieurs (LinkedIn, annuaires) visent l'accueil |
| B. La page à l'accueil | Publier la page à `https://www.fractal-innov.fr/` ; `/stand/` redirige vers l'accueil (QR codes et liens imprimés continuent de marcher) | Une seule adresse forte, celle que Google a déjà choisie et que citent les sources extérieures | Change la publication des deux dépôts ; plan séparé |
| C. Un vrai accueil | L'accueil devient une courte page réelle (offre en 3 phrases, lien vers `/stand/`), sans redirection | Chaque page a son adresse ; les robots lisent quelque chose à l'accueil | Deux pages à tenir ; l'accueil reste mince |

Recommandation : **B**, parce que Google et les sources extérieures pointent déjà vers l'accueil ; A seulement si une réinspection montre que Google a changé d'avis.

- [ ] **Step 3: Noter la décision**

Ajouter à la fin de `docs/cadrage-seo-geo.md` :

```markdown
## Décision : adresse canonique de la page (AAAA-MM-JJ)

- Constat Search Console : canonique déclarée `[…]`, sélectionnée par Google `[…]`.
- Option retenue : [A | B | C], parce que [raison].
- Suite : [plan séparé `docs/superpowers/plans/AAAA-MM-JJ-adresse-canonique.md` | réinspection le AAAA-MM-JJ].
```

Remplacer les crochets par les valeurs réelles, puis :

```bash
git switch -c docs/decision-canonique
git add docs/cadrage-seo-geo.md
git commit -m "docs(seo): décider de l'adresse canonique de la page

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -u origin docs/decision-canonique
gh pr create --base master --title "docs(seo): décision sur l'adresse canonique" --body "🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

---

### Tâche 5 : `llms.txt` et date du plan du site (dépôt racine)

**Files:**
- Create: `llms.txt` (racine de `Fractal-Innov.github.io`)
- Modify: `sitemap.xml` (`<lastmod>` de `/stand/`)

**Interfaces:**
- Consumes: la date de fusion (Tâche 3). Si la Tâche 4 retient l'option B, les liens de `llms.txt` changeront avec le plan séparé.

- [ ] **Step 1: Récupérer le dépôt racine et créer la branche**

```bash
cd /Users/hugsdaniel/code/HugsDaniel/freelance/FractalInnov
[ -d Fractal-Innov.github.io ] || gh repo clone Fractal-Innov/Fractal-Innov.github.io
cd Fractal-Innov.github.io
git switch main && git pull
git switch -c feat/llms-txt
sed -n 50,80p .github/workflows/publier.yml
```

Expected: le workflow publie le dépôt. Si une étape `run:` retire des fichiers avant publication, vérifier qu'elle ne retire pas `*.txt` ; sinon, garder `llms.txt` dans le même commit.

- [ ] **Step 2: Vérifier que `llms.txt` n'existe pas en ligne**

Run: `curl -s -o /dev/null -w '%{http_code}\n' https://www.fractal-innov.fr/llms.txt`
Expected: `404`

- [ ] **Step 3: Écrire `llms.txt`**

Créer `llms.txt` (texte aligné sur la v7 et `CLAUDE.md` ; à faire relire par Corentin dans la PR) :

```markdown
# Fractal Innov

> Fractal Innov conçoit le démonstrateur 3D de votre produit : son jumeau 3D, sur votre stand de salon (même sans réseau), sur votre site et en rendez-vous, piloté depuis un téléphone. Un contenu 3D, produit une fois, que le client garde.

Fractal Innov est une entreprise française installée à Suresnes (Île-de-France). Elle travaille dans toute la France.

## Pour qui

- Les industriels et fabricants dont le produit ne peut pas être montré facilement : trop grand, trop lourd, trop fragile ou pas encore fabriqué (machines, équipements, systèmes intégrés).
- Les entreprises qui font plusieurs salons par an, reçoivent en showroom ou présentent leur produit en rendez-vous.

## Ce que fait le démonstrateur

- Le visiteur explore le produit en 3D du bout du doigt, sous tous les angles.
- Un parcours guidé amène la caméra au bon endroit et affiche la vidéo ou la fiche au moment où la question se pose.
- Le commercial pilote la présentation depuis son téléphone, sans application à installer.
- Sur un salon, le kit fonctionne hors ligne, avec son propre réseau, indépendant du wifi du lieu.
- Les contenus se changent sans développeur, en français et en anglais.
- Des statistiques de visite indiquent ce qui a intéressé les visiteurs.

## Options sur devis

- La version en ligne, sur le site du client, et la réalité augmentée. En ligne et hors ligne sont deux diffusions du même contenu 3D, livrées et mises à jour séparément.
- La modélisation 3D du produit, plusieurs produits dans la même expérience, le mobilier et le flight case.

## Ce qui n'est pas inclus

- L'écran tactile, loué sur place auprès du loueur du salon.
- Les vidéos et les fiches, fournies par le client.
- Une équipe sur place pendant le salon : l'accompagnement a lieu avant.

## Comment travailler avec Fractal Innov

1. Un appel de 30 minutes, gratuit et sans engagement.
2. Un atelier de 2 heures, compris dans le projet, pour réunir les éléments du devis.
3. Le devis, remis sous 24 heures après l'atelier. Le prix dépend du produit et des fichiers disponibles : il n'y a pas de tarif public.

## Liens

- [Démonstrateur 3D de votre produit](https://www.fractal-innov.fr/stand/) : l'offre, les questions fréquentes et la prise de rendez-vous
- [Démo en ligne](https://stand-demonstrateur.osc-fr1.scalingo.io/) : un stand d'exemple à manipuler depuis un navigateur
- [Contact](mailto:corentin.duboc@fractal-innov.fr)
```

- [ ] **Step 4: Contrôler le texte**

```bash
grep -nE '€|euros?|semaines|STAND|—|synchronis' llms.txt && echo "À CORRIGER" || echo "OK"
```

Expected: `OK` (ni prix, ni durée, ni « STAND », ni tiret cadratin, ni synchronisation promise).

- [ ] **Step 5: Dater `/stand/` dans le plan du site**

Remplacer `AAAA-MM-JJ` par la date de la Tâche 3, Step 5 :

```bash
DATE='AAAA-MM-JJ' python3 - <<'PY'
import os, re
from pathlib import Path
date = os.environ['DATE']
assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', date), date
p = Path('sitemap.xml')
s = p.read_text(encoding='utf-8')
motif = re.compile(r'(<loc>https://www\.fractal-innov\.fr/stand/</loc>\s*<lastmod>)\d{4}-\d{2}-\d{2}(</lastmod>)')
assert len(motif.findall(s)) == 1, len(motif.findall(s))
s = motif.sub(lambda m: m.group(1) + date + m.group(2), s)
p.write_text(s, encoding='utf-8')
PY
grep -n 'stand/' sitemap.xml
```

Expected: la ligne `/stand/` porte la nouvelle date.

- [ ] **Step 6: Commit, PR, fusion**

```bash
git add llms.txt sitemap.xml
git commit -m "feat: ajouter llms.txt et dater la page stand dans le plan du site

llms.txt résume l'entreprise et l'offre pour les assistants, aligné sur
la v7 de la page : ni prix ni délai, options sur devis, en ligne et hors
ligne livrés séparément. La date de /stand/ suit sa dernière mise à jour.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -u origin feat/llms-txt
gh pr create --base main --title "feat: llms.txt et date de la page stand" --body "Levier 1 du plan entrant. Relecture du texte de llms.txt par Corentin avant fusion.

🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

Corentin relit le texte, Hugo fusionne et attend le workflow `Publier sur GitHub Pages`.

- [ ] **Step 7: Contrôler `llms.txt` en ligne et son encodage**

```bash
curl -s https://www.fractal-innov.fr/llms.txt | head -3
curl -sI https://www.fractal-innov.fr/llms.txt | grep -i '^content-type'
```

Expected: première ligne `# Fractal Innov`, accents corrects, `content-type: text/plain; charset=utf-8`. Sans `charset`, vérifier les accents dans Chrome ; s'ils sont cassés, le signaler avant de continuer.

---

### Tâche 6 : Search Console et Bing (manuel, Hugo)

**Files:**
- Aucun.

- [ ] **Step 1: Soumettre le plan du site à Google**

Search Console, « Sitemaps » : si `sitemap.xml` n'est pas listé, le saisir et « Envoyer ».
Expected: état « Opération effectuée », date de dernière lecture postérieure à la Tâche 5.

- [ ] **Step 2: Demander l'indexation de la page**

« Inspecter » `https://www.fractal-innov.fr/stand/`, « Tester l'URL en direct ».
Expected: « L'URL est disponible pour Google », la FAQ apparaît dans « Données structurées ». Cliquer « Demander l'indexation ».

- [ ] **Step 3: S'inscrire à Bing Webmaster Tools**

Le passage 0 note que Bing connaît `/stand/` sans inscription ; le dépôt racine contient `BingSiteAuth.xml`, donc une vérification a déjà été faite pour un compte. Se connecter à https://www.bing.com/webmasters ; si le site n'apparaît pas pour Hugo, utiliser « Importer depuis Google Search Console » ou demander l'accès au compte qui l'a vérifié.
Expected: `https://www.fractal-innov.fr/` visible dans le tableau de bord.

- [ ] **Step 4: Soumettre le plan du site et la page à Bing**

« Sitemaps » : `https://www.fractal-innov.fr/sitemap.xml`, « Envoyer ». « Soumission d'URL » : `https://www.fractal-innov.fr/stand/`.
Expected: sitemap « Réussi » (quelques heures) ; URL acceptée.

---

### Tâche 7 : l'aperçu de la démo (Needle5, Corentin)

**Files:**
- Modify: `Needle5/Needle/Salon/index.html` (dépôt privé, absent de la machine de Hugo)

**Interfaces:**
- Consumes: `https://www.fractal-innov.fr/stand/assets/share/og-image-v3.jpg` (1200 × 630, en ligne).
- Produces: un aperçu soigné quand le lien de la démo est collé dans un e-mail ou sur LinkedIn (plan sortant).

- [ ] **Step 1: Vérifier l'absence d'aperçu**

Run: `curl -s https://stand-demonstrateur.osc-fr1.scalingo.io/ | grep -c 'og:image'`
Expected: `0`

- [ ] **Step 2: Ajouter les balises dans Needle5 (Corentin)**

Dans `Needle5/Needle/Salon/index.html`, juste après `<title>…</title>` (ou dans le gabarit qui produit `<title>` depuis la configuration produit, si c'est le cas) :

```html
    <meta name="description" content="Testez le démonstrateur 3D de Fractal Innov : explorez un stand du bout du doigt et pilotez-le depuis votre téléphone." />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Fractal Innov" />
    <meta property="og:url" content="https://stand-demonstrateur.osc-fr1.scalingo.io/" />
    <meta property="og:title" content="Fractal Innov · Démonstrateur 3D" />
    <meta property="og:description" content="Testez le démonstrateur 3D de Fractal Innov : explorez un stand du bout du doigt et pilotez-le depuis votre téléphone." />
    <meta property="og:image" content="https://www.fractal-innov.fr/stand/assets/share/og-image-v3.jpg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="twitter:card" content="summary_large_image" />
```

- [ ] **Step 3: Synchroniser le miroir et déployer (Corentin)**

Commit dans Needle5, `npm run sync:miroir`, relire `git status` de `salon_demo_app` (une suppression signale un fichier non rapatrié), commit, push ; Scalingo redéploie.

- [ ] **Step 4: Vérifier l'aperçu**

Run: `curl -s https://stand-demonstrateur.osc-fr1.scalingo.io/ | grep -c 'og:image'`
Expected: `3` (les lignes `og:image`, `og:image:width`, `og:image:height`). Puis https://www.linkedin.com/post-inspector/ avec l'URL de la démo : image, titre et description s'affichent.

---

### Tâche 8 : page « village », journal et suivi

**Files:**
- Modify: `stand_landing_official/VENTE.md` (« Journal »)
- Modify (selon la décision): `Fractal-Innov.github.io/sitemap.xml`

- [ ] **Step 1: Décider avec Corentin (15 minutes)**

| Question | Option A | Option B |
| --- | --- | --- |
| La page `/village/` (ancienne page d'accueil, publiée comme démonstrateur) et les démos Midipile, Rayon X, Moulage, encore dans le plan du site | Les garder, présentées sur une future page « Réalisations » reliée à la page (plan séparé ; Midipile en vidéo seulement, sa réalité augmentée ne marche plus sur les téléphones récents) | Retirer du plan du site celles qui ne servent pas l'offre actuelle |

- [ ] **Step 2: Appliquer la décision sur le plan du site (si option B)**

Pour chaque adresse retirée (exemple avec `/village/`) :

```bash
cd /Users/hugsdaniel/code/HugsDaniel/freelance/FractalInnov/Fractal-Innov.github.io
git switch main && git pull && git switch -c chore/sitemap-demos
ADRESSE='https://www.fractal-innov.fr/village/' python3 - <<'PY'
import os
from pathlib import Path
adresse = os.environ['ADRESSE']
p = Path('sitemap.xml')
s = p.read_text(encoding='utf-8')
lignes = [l for l in s.splitlines(keepends=True) if f'<loc>{adresse}</loc>' in l]
assert len(lignes) == 1, len(lignes)
s = s.replace(lignes[0], '')
p.write_text(s, encoding='utf-8')
PY
grep -c 'village' sitemap.xml
```

Expected: `0`. Puis commit `chore: retirer du plan du site les démos hors offre` (pied `Co-Authored-By`), push, PR, Hugo fusionne.

- [ ] **Step 3: Écrire le journal dans `VENTE.md`**

Remplacer les crochets par les valeurs réelles avant d'exécuter :

```bash
cd /Users/hugsdaniel/code/HugsDaniel/freelance/FractalInnov/stand_landing_official
git switch master && git pull && git switch -c docs/journal-page-aplomb
cat >> VENTE.md <<'MD'
- [AAAA-MM-JJ] : levier 1 du plan entrant. FAQ reformulée en vraies questions (réponses inchangées), nœud FAQPage généré depuis la FAQ visible ; mesure sans cookie de la page (réserver un appel, tester la démo, l'ouvrir dans un onglet) ; llms.txt à la racine du site ; plan du site soumis à Google et Bing. Adresse canonique : option [A | B | C]. Démos du plan du site : [décision].
MD
tail -2 VENTE.md
git add VENTE.md
git commit -m "docs(vente): journal du levier 1 du plan entrant

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -u origin docs/journal-page-aplomb
gh pr create --base master --title "docs(vente): journal du levier 1 du plan entrant" --body "🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

Expected: la dernière ligne du journal porte la date et les décisions, sans crochets.

- [ ] **Step 4: Planifier le passage de mesure 1**

Ajouter un rappel deux semaines après la mise en ligne de `llms.txt` pour refaire le passage de `docs/mesure-geo.md` (mêmes questions, mêmes conditions) et comparer au passage 0. Cocher les lignes « Semaines 1 et 2 » de l'onglet « Plan entrant · Hugo ».
