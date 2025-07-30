# 🎭 Bypass-RegEx - Générateur de Contournement de Filtres

**Créé par ozGod-sh**

## Description

Bypass-RegEx est un outil spécialisé dans la génération de variations de payloads pour contourner les filtres basés sur des expressions régulières. Il transforme les chaînes d'entrée en utilisant différentes techniques d'encodage et de manipulation pour éviter la détection.

## Fonctionnalités

### 🔄 Techniques de contournement
- **Encodage URL** : Standard, double encodage, et encodage avec '+'
- **Entités HTML** : Encodage décimal et hexadécimal
- **Variations de casse** : Toutes les combinaisons majuscule/minuscule
- **Optimisation intelligente** : Limite les variations pour éviter l'explosion combinatoire

### 🎯 Applications de sécurité
- **Contournement WAF** : Éviter les Web Application Firewalls
- **Bypass de filtres** : Contourner les validations côté client/serveur
- **Tests d'injection** : Générer des payloads pour XSS, SQLi, etc.

## Installation

### Prérequis
- Python 3.6+
- Aucune dépendance externe (utilise la bibliothèque standard)

### Installation
```bash
cd Bypass-RegEx
# Aucune installation requise - utilise uniquement la stdlib Python
```

## Utilisation

### Syntaxe de base
```bash
python bypass_regex.py <PAYLOAD>
```

### Exemples d'utilisation

#### 1. Contournement XSS basique
```bash
python bypass_regex.py "<script>alert(1)</script>"
```

#### 2. Payload SQL Injection
```bash
python bypass_regex.py "' OR 1=1 --"
```

#### 3. Commande système
```bash
python bypass_regex.py "cat /etc/passwd"
```## St
ructure des fichiers

```
Bypass-RegEx/
├── bypass_regex.py     # Script principal
└── README.md          # Cette documentation
```

## Logique de fonctionnement

### 1. Encodage URL
```python
# Encodage standard
encoded = quote(payload)
# Encodage double
double_encoded = quote(encoded)
# Encodage avec '+' pour les espaces
quote_plus(payload)
```

### 2. Entités HTML
```python
# Encodage décimal
''.join(f'&#{ord(c)};' for c in payload)
# Encodage hexadécimal
''.join(f'&#x{ord(c):x};' for c in payload)
```

### 3. Variations de casse
```python
# Génération de toutes les combinaisons possibles
import itertools
maps = itertools.product(*[[c.lower(), c.upper()] for c in payload])
```

### 4. Optimisation pour les longues chaînes
- **Limite de 10 caractères** : Évite l'explosion combinatoire
- **Variations simples** : Majuscule, minuscule, titre pour les chaînes longues
- **Gestion mémoire** : Utilise des générateurs Python

## Cas d'usage

### Tests de sécurité web
- **Contournement XSS** : Éviter les filtres anti-XSS
- **Injection SQL** : Contourner les validations de requêtes
- **Command Injection** : Éviter les filtres de commandes système
- **Path Traversal** : Contourner les validations de chemins

### Audit de WAF
- **Tests de règles** : Vérifier l'efficacité des règles de filtrage
- **Détection de failles** : Identifier les patterns non couverts
- **Validation de configuration** : Tester les paramètres de sécurité

## Exemple de sortie

### Pour le payload `<script>alert(1)</script>`

```
[*] Génération de variations pour le payload : '<script>alert(1)</script>'

--- Encodage URL ---
  - Encodage Standard: %3Cscript%3Ealert%281%29%3C%2Fscript%3E
  - Encodage Double: %253Cscript%253Ealert%25281%2529%253C%252Fscript%253E
  - Encodage avec '+': %3Cscript%3Ealert%281%29%3C%2Fscript%3E

--- Encodage Entités HTML ---
  - Décimal: &#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;
  - Hexadécimal: &#x3c;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&#x3e;&#x61;&#x6c;&#x65;&#x72;&#x74;&#x28;&#x31;&#x29;&#x3c;&#x2f;&#x73;&#x63;&#x72;&#x69;&#x70;&#x74;&#x3e;

--- Variations de Cas ---
  - <SCRIPT>ALERT(1)</SCRIPT>
  - <script>alert(1)</script>
  - <Script>Alert(1)</Script>
  - <ScRiPt>AlErT(1)</ScRiPt>
  [... autres variations ...]
```

## Techniques de contournement supportées

### 1. Encodage URL
- **Standard (RFC 3986)** : Encode les caractères spéciaux
- **Double encodage** : Encode le résultat de l'encodage
- **Plus encoding** : Utilise '+' pour les espaces

### 2. Entités HTML
- **Décimal** : `&#65;` pour 'A'
- **Hexadécimal** : `&#x41;` pour 'A'
- **Nommées** : `&lt;` pour '<' (non implémenté)

### 3. Variations de casse
- **Alternance** : `ScRiPt`
- **Toutes majuscules** : `SCRIPT`
- **Toutes minuscules** : `script`
- **Première lettre** : `Script`

## Intégration avec d'autres outils

### Avec Burp Suite
```bash
# Générer les variations puis les importer dans Burp
python bypass_regex.py "payload" > variations.txt
```

### Avec des scripts d'automatisation
```python
import subprocess

def get_bypass_variations(payload):
    result = subprocess.run(['python', 'bypass_regex.py', payload], 
                          capture_output=True, text=True)
    return result.stdout.split('\n')
```

### Avec des frameworks de test
```bash
# Utiliser dans des tests automatisés
for payload in $(python bypass_regex.py "test"); do
    curl -d "input=$payload" http://target.com/test
done
```

## Limitations

### Techniques non couvertes
- **Unicode normalization** : Pas de support des caractères Unicode
- **Encodage Base64** : Non implémenté
- **Techniques de fragmentation** : Pas de division de payload
- **Encodage JSON** : Pas d'échappement JSON

### Performance
- **Explosion combinatoire** : Limitée à 10 caractères pour les variations de casse
- **Pas de parallélisation** : Traitement séquentiel
- **Mémoire** : Peut consommer beaucoup de mémoire pour de longs payloads

## Améliorations futures

### Nouvelles techniques
- Support Unicode et UTF-8
- Encodage Base64 et autres formats
- Techniques de fragmentation de payload
- Encodage spécifique aux contextes (JSON, XML, etc.)

### Optimisations
- Parallélisation des générations
- Cache des résultats
- Interface graphique
- Export en formats multiples (JSON, CSV)

### Intégrations
- Plugin Burp Suite
- Extension navigateur
- API REST pour intégration
- Base de données de techniques

## Contre-mesures

### Pour les développeurs
- **Validation stricte** : Ne pas se fier uniquement aux regex
- **Whitelist approach** : Autoriser uniquement les caractères valides
- **Normalisation** : Décoder et normaliser avant validation
- **Validation multicouche** : Client + serveur + base de données

### Pour les administrateurs WAF
- **Règles multiples** : Combiner plusieurs techniques de détection
- **Normalisation automatique** : Décoder avant analyse
- **Machine learning** : Utiliser des approches adaptatives
- **Mise à jour régulière** : Maintenir les signatures à jour

## Contextes d'application

### Web Applications
- **Formulaires** : Contourner la validation côté client
- **APIs** : Éviter les filtres de paramètres
- **Upload de fichiers** : Contourner les restrictions de noms

### Systèmes
- **Command injection** : Éviter les filtres de commandes
- **Path traversal** : Contourner les validations de chemins
- **Log injection** : Injecter dans les logs système

## Sécurité et éthique

⚠️ **Utilisation responsable uniquement**
- Testez uniquement vos propres applications
- Obtenez une autorisation écrite pour les tests de pénétration
- Respectez les lois locales sur la cybersécurité
- Utilisez pour améliorer la sécurité, pas pour nuire

## Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

---

**Bypass-RegEx v1.0.0** | Créé par ozGod-sh