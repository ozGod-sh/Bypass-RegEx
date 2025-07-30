# -*- coding: utf-8 -*-
# Auteur: ozGod

import argparse
from urllib.parse import quote, quote_plus

def display_banner():
    """Affiche une bannière stylisée pour l'outil."""
    VERSION = "1.0.0"
    AUTHOR = "ozGod"
    banner = f"""
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  🎭 Bypass-RegEx v{VERSION}                                  ║
║                                                              ║
║  Générateur de chaînes pour contourner les filtres RegEx.   ║
║  Créé par {AUTHOR}                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)

def generate_case_variations(payload):
    """Génère des variations de casse (ex: 'SeLeCt')."""
    if len(payload) > 10: # Limite pour éviter une explosion combinatoire
        print("  - Variation de casse simple (majuscule/minuscule/titre)")
        yield payload.upper()
        yield payload.lower()
        yield payload.title()
        return

    print("  - Variations de casse mixtes...")
    # Génère toutes les combinaisons de casse possibles
    import itertools
    maps = itertools.product(*[[c.lower(), c.upper()] for c in payload])
    for i in maps:
        yield "".join(i)

def generate_url_encoded(payload):
    """Génère des variations encodées en URL."""
    print("\n--- Encodage URL ---")
    # Encodage standard
    encoded = quote(payload)
    print(f"  - Encodage Standard: {encoded}")
    # Encodage double
    double_encoded = quote(encoded)
    print(f"  - Encodage Double: {double_encoded}")
    # Encodage avec '+' pour les espaces
    print(f"  - Encodage avec '+': {quote_plus(payload)}")

def generate_html_entities(payload):
    """Génère des variations encodées en entités HTML."""
    print("\n--- Encodage Entités HTML ---")
    # Encodage décimal
    decimal_encoded = ''.join(f'&#{ord(c)};' for c in payload)
    print(f"  - Décimal: {decimal_encoded}")
    # Encodage hexadecimal
    hex_encoded = ''.join(f'&#x{ord(c):x};' for c in payload)
    print(f"  - Hexadécimal: {hex_encoded}")

def main():
    display_banner()
    parser = argparse.ArgumentParser(
        description="Génère des variations d'un payload pour contourner les filtres basés sur des expressions régulières.",
        epilog=f"Créé par ozGod."
    )
    parser.add_argument("payload", help="Le payload ou mot-clé à transformer (ex: '<script>alert(1)</script>').")
    args = parser.parse_args()

    print(f"[*] Génération de variations pour le payload : '{args.payload}'\n")

    # Génération des variations
    generate_url_encoded(args.payload)
    generate_html_entities(args.payload)

    print("\n--- Variations de Cas ---")
    for variation in generate_case_variations(args.payload):
        print(f"  - {variation}")

if __name__ == "__main__":
    main()
