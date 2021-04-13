#!python ./manage.py shell
from base0.models import *



# LeftSide.objects.get(pk=1)
# BsInTsm.objects.get(bs="10")

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()
# now your code can go here...
print(BsInTsm.objects.all())