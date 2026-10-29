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
UMAMI_SRC = 'https://cloud.umami.is/script.js'
UMAMI_DOMAINE = 'www.fractal-innov.fr'
UUID = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
CALENDRIER = 'calendar.app.google'
# Début d'adresse des liens de contact → événement attendu sur chacun.
LIENS_CONTACT = {
    'https://s.blinq.me/': 'ouvrir-carte-visite',
    'mailto:': 'ecrire-email',
    'https://www.linkedin.com/': 'ouvrir-linkedin',
    'https://www.instagram.com/': 'ouvrir-instagram',
}


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
        self._profondeur = 0   # sections ouvertes dans #questions
        self._cache = 0        # profondeur dans <script> / <style>

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style'):
            self._cache += 1
        if tag == 'a':
            self.liens.append(a)
        if 'data-launch-demo' in a:
            self.lanceurs.append(a)
        if tag == 'section' and self._dans_faq:
            self._profondeur += 1
        elif tag == 'section' and a.get('id') == 'questions':
            self._dans_faq, self._profondeur = True, 1
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
        if tag == 'section' and self._dans_faq:
            self._profondeur -= 1
            self._dans_faq = self._profondeur > 0
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
    page.html = html
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


def noeud_faq_ld(blocs):
    """Le premier nœud FAQPage trouvé, tel quel, sinon {}."""
    for brut in blocs:
        donnees = json.loads(brut)
        noeuds = donnees.get('@graph', [donnees]) if isinstance(donnees, dict) else donnees
        for n in noeuds:
            if n.get('@type') == 'FAQPage':
                return n
    return {}


def controle_faq(page):
    questions = [q for q, _ in page.faq]
    faq_ld = trouver_faq_ld(page.jsonld)
    noeud = noeud_faq_ld(page.jsonld)
    return [
        ('Nœud FAQPage avec son adresse et sa langue',
         noeud.get('url') == 'https://www.fractal-innov.fr/stand/' and noeud.get('inLanguage') == 'fr-FR',
         {k: noeud.get(k) for k in ('url', 'inLanguage')}),
        ('FAQ en vraies questions', questions == QUESTIONS_ATTENDUES, questions),
        ('FAQ : une réponse non vide par question',
         len(page.faq) == len(QUESTIONS_ATTENDUES) and all(r for _, r in page.faq), page.faq),
        ('Nœud FAQPage identique à la FAQ visible', faq_ld == page.faq, faq_ld),
    ]


def controle_liens_contact(page):
    resultats = []
    for debut, evenement in LIENS_CONTACT.items():
        liens = [l for l in page.liens if (l.get('href') or '').startswith(debut)]
        resultats.append((f'Clics mesurés : {evenement} ({len(liens)} liens)',
                          bool(liens) and all(l.get('data-umami-event') == evenement for l in liens),
                          [l.get('data-umami-event') for l in liens]))
    return resultats


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
        # Umami annule le clic d'un <a data-umami-event> sans target=_blank et
        # navigue après l'envoi : sur un lien interne, le défilement de la page
        # (allerSection) ne part plus. Ces clics se mesurent en JS.
        ('Aucun lien interne avec data-umami-event',
         not [l for l in page.liens
              if (l.get('href') or '').startswith('#') and 'data-umami-event' in l],
         [l for l in page.liens
          if (l.get('href') or '').startswith('#') and 'data-umami-event' in l]),
        ('Lancements de la démo mesurés en JS',
         bool(page.lanceurs) and "umami.track('tester-demo')" in page.html, len(page.lanceurs)),
        ('Ancres exclues des pages vues', script.get('data-exclude-hash') == 'true',
         script.get('data-exclude-hash')),
        ('Ouverture de la démo dans un onglet mesurée',
         len(nouvel_onglet) == 1 and nouvel_onglet[0].get('data-umami-event') == 'ouvrir-demo-onglet',
         nouvel_onglet),
        *controle_liens_contact(page),
        ("Aucun nom d'outil de statistiques visible", 'Umami' not in texte, 'Umami'),
        ('Aucun « STAND » visible comme nom de produit', not re.search(r'\bSTAND\b', texte), 'STAND'),
    ]


def controles(page):
    return controle_faq(page) + controle_mesure(page)


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
