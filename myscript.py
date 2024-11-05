import os

# Récupérer les variables d'environnement
badhash = os.getenv('BAD_HASH')
goodhash = os.getenv('GOOD_HASH')

# Si BAD_HASH n'est pas défini, utiliser le commit actuel comme point de départ
if not badhash:
    badhash = os.popen("git rev-parse HEAD").read().strip()

# Si GOOD_HASH n'est pas défini, chercher le dernier commit valide (qui a passé les tests)
if not goodhash:
    # Trouver le dernier commit qui a passé les tests
    goodhash = os.popen("git log --grep='Tests passed' -1 --pretty=format:'%H'").read().strip()

# Vérifier que les variables sont correctement définies (après initialisation)
if not badhash or not goodhash:
    raise ValueError("Unable to determine both BAD_HASH and GOOD_HASH.")

# Exécuter les commandes
os.system(f"git bisect start {badhash} {goodhash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")
