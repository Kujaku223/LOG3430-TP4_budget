import os
import sys

badhash = sys.argv[1]
goodhash = sys.argv[2]


os.system(f"git bisect start {badhash} {goodhash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")