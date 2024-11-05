import os
import sys

badhash = sys.argv[1]
goodhash = sys.argv[2]
command = "git bisect start" + badhash + " " + goodhash

os.system(command)
os.system("git bisect run python manage.py test")