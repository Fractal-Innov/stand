#!/usr/bin/env python3
"""Tests des outils (verif_seo, faq_jsonld). Usage : python3 outils/test_outils.py"""
import subprocess
import sys
import tempfile
from pathlib import Path

from verif_seo import lire_page

ICI = Path(__file__).parent
LD = '<head><script type="application/ld+json">{"@graph":[{"@type":"FAQPage","mainEntity":[]}]}</script></head>'


def generer(html):
    """Lance faq_jsonld.py sur une copie ; rend (code de sortie, contenu après)."""
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / 'index.html'
        f.write_text(html, encoding='utf-8')
        r = subprocess.run([sys.executable, str(ICI / 'faq_jsonld.py'), str(f)],
                           capture_output=True, text=True)
        return r.returncode, f.read_text(encoding='utf-8')


def test_section_imbriquee_garde_les_questions_suivantes():
    page = lire_page('<section id="questions"><h3>Q1</h3><p>R1</p>'
                     '<section><p>x</p></section><h3>Q2</h3><p>R2</p></section>')
    assert [q for q, _ in page.faq] == ['Q1', 'Q2'], page.faq


def test_generateur_refuse_une_faq_vide():
    html = LD + '<body></body>'
    code, apres = generer(html)
    assert code != 0, 'FAQ vide acceptée'
    assert apres == html, 'fichier modifié malgré une FAQ vide'


def test_generateur_refuse_une_reponse_vide():
    html = LD + '<body><section id="questions"><h3>Q1</h3></section></body>'
    code, apres = generer(html)
    assert code != 0, 'réponse vide acceptée'
    assert apres == html, 'fichier modifié malgré une réponse vide'


if __name__ == '__main__':
    echecs = 0
    for nom, test in list(globals().items()):
        if nom.startswith('test_'):
            try:
                test()
                print('OK     ' + nom)
            except AssertionError as e:
                print(f'ÉCHEC  {nom} : {e}')
                echecs += 1
    sys.exit(1 if echecs else 0)
