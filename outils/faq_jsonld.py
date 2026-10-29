#!/usr/bin/env python3
"""Réécrit les questions du nœud FAQPage du JSON-LD de index.html depuis la FAQ visible.

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


def questions_faq(faq):
    return [
        {
            '@type': 'Question',
            'name': question,
            'acceptedAnswer': {'@type': 'Answer', 'text': reponse},
        }
        for question, reponse in faq
    ]


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
    # Seules les questions changent : le reste du nœud (url, inLanguage…) reste.
    graphe[places[0]]['mainEntity'] = questions_faq(page.faq)
    contenu = json.dumps(donnees, ensure_ascii=False, indent=2)
    s = BLOC.sub(lambda m: m.group(1) + '\n' + contenu + '\n  ' + m.group(3), s)
    p.write_text(s, encoding='utf-8')
    print(f'{len(page.faq)} questions écrites dans le nœud FAQPage')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
