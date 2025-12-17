#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
スクリプト: HTML ファイルを走査し、既知のボタン要素に統一クラスを追加します。
対象:
 - id="btn" -> add "btn btn--outline"
 - .downloadButton a -> add "btn btn--primary"
 - .totickets a -> add "btn btn--primary"
 - input/button with class contact-submit -> add "btn btn--primary" (keep existing class)

実行前にファイルをバックアップ（.bak）として保存します。
"""
import sys
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
HTML_GLOB = "**/*.html"

def add_classes_to_file(path: Path):
    text = path.read_text(encoding='utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    changed = False

    # id="btn"
    el = soup.find(id='btn')
    if el:
        classes = el.get('class', [])
        if 'btn' not in classes:
            classes = classes + ['btn', 'btn--outline']
            el['class'] = classes
            changed = True

    # .downloadButton a
    for parent in soup.select('.downloadButton'):
        for a in parent.find_all('a'):
            classes = a.get('class', [])
            if 'btn' not in classes:
                classes = classes + ['btn', 'btn--primary']
                a['class'] = classes
                changed = True

    # .totickets a
    for parent in soup.select('.totickets'):
        for a in parent.find_all('a'):
            classes = a.get('class', [])
            if 'btn' not in classes:
                classes = classes + ['btn', 'btn--primary']
                a['class'] = classes
                changed = True

    # input/button.contact-submit
    for inp in soup.select('.contact-submit'):
        classes = inp.get('class', [])
        if 'btn' not in classes:
            classes = classes + ['btn', 'btn--primary']
            inp['class'] = classes
            changed = True

    if changed:
        bak = path.with_suffix(path.suffix + '.bak')
        bak.write_text(text, encoding='utf-8')
        path.write_text(str(soup), encoding='utf-8')
        print(f"Updated: {path}")
    else:
        print(f"No change: {path}")


def main():
    files = list(ROOT.glob(HTML_GLOB))
    for f in files:
        # skip files in scripts folder itself
        if 'scripts' in f.parts:
            continue
        add_classes_to_file(f)

if __name__ == '__main__':
    main()
