import os
import sys

# Récupérer les variables d'environnement
badhash = os.getenv('BAD_HASH')
goodhash = os.getenv('GOOD_HASH')

# Vérifier si les variables sont présentes
if not badhash or not goodhash:
    raise ValueError(f"Unable to determine both BAD_HASH and GOOD_HASH. BAD_HASH={badhash}, GOOD_HASH={goodhash}")

# Afficher les commits pour débogage
print(f"Using BAD_HASH: {badhash}")
print(f"Using GOOD_HASH: {goodhash}")

# Exécuter les commandes
os.system(f"git bisect start {badhash} {goodhash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")
