#!/usr/bin/env python3
"""
Demo script to show examples of Czech typing exercises
This script displays sample exercises without requiring GUI
"""

import random

# Sample Czech words from the main application
czech_words_basic = [
    'ale', 'ano', 'až', 'bez', 'byl', 'být', 'den', 'dnes', 'dobrý', 'dva',
    'jeho', 'jen', 'již', 'když', 'kde', 'který', 'má', 'mít', 'můj', 'na',
    'nebo', 'než', 'není', 'nový', 'pak', 'pro', 'při', 'první', 'se', 'svůj',
    'také', 'tam', 'ten', 'třeba', 'už', 've', 'však', 'všechen', 'za', 'být'
]

czech_words_intermediate = [
    'člověk', 'český', 'často', 'číslo', 'děkuji', 'díky', 'další', 'důvod',
    'hlavní', 'ještě', 'jméno', 'několik', 'něco', 'nikdo', 'případ', 'příliš',
    'přijít', 'říci', 'společnost', 'škola', 'správný', 'určitě', 'úplně',
    'větší', 'věc', 'vůbec', 'začít', 'život', 'známý', 'žádný', 'žena'
]

czech_sentences = [
    'dobrý den jak se máte',
    'děkuji za vaši pomoc',
    'dnes je opravdu pěkné počasí',
    'učím se psát rychle na klávesnici',
    'česká klávesnice má speciální znaky',
    'příliš žluťoučký kůň úpěl ďábelské ódy',
    'procvičuji denně každé písmeno důkladně',
    'úspěch přijde s prací a trpělivostí'
]

print("=" * 80)
print("CZECH KEYBOARD TOUCH TYPING TUTOR - EXERCISE EXAMPLES")
print("=" * 80)
print()

print("LEVEL 4: Czech Basic Words")
print("-" * 80)
for i in range(5):
    exercise = ' '.join(random.choices(czech_words_basic, k=10))
    print(f"Exercise {i+1}: {exercise}")
print()

print("LEVEL 5: Czech Words with Diacritics")
print("-" * 80)
diacritic_words = [w for w in czech_words_basic + czech_words_intermediate 
                   if any(c in w for c in 'ěščřžýáíéúů')]
for i in range(5):
    exercise = ' '.join(random.choices(diacritic_words, k=8))
    print(f"Exercise {i+1}: {exercise}")
print()

print("LEVEL 6: Intermediate Czech Words")
print("-" * 80)
for i in range(5):
    exercise = ' '.join(random.choices(czech_words_intermediate, k=7))
    print(f"Exercise {i+1}: {exercise}")
print()

print("LEVEL 8: Czech Sentences")
print("-" * 80)
for i, sentence in enumerate(czech_sentences[:5], 1):
    print(f"Exercise {i}: {sentence}")
print()

print("=" * 80)
print("DIACRITICS FEATURED IN EXERCISES:")
print("-" * 80)
diacritics = {
    'ě': 'háček nad e', 'š': 'háček nad s', 'č': 'háček nad c',
    'ř': 'háček nad r', 'ž': 'háček nad z', 'ý': 'čárka nad y',
    'á': 'čárka nad a', 'í': 'čárka nad i', 'é': 'čárka nad e',
    'ú': 'čárka nad u', 'ů': 'kroužek nad u'
}
for char, desc in diacritics.items():
    print(f"  {char} - {desc}")
print()

print("=" * 80)
print("Total Exercises Available: 1,200+")
print("All exercises use authentic Czech vocabulary and proper diacritics!")
print("=" * 80)
