import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protwo.settings")

import django
django.setup()

from Apptwo.models import User
from faker import Faker

fakergen = Faker()

def populate(N=5):
	for entry in range(N):
		fake_name = fakergen.name().split()
		fake_first_name = fake_name[0]
		fake_last_name = fake_name[1]
		fake_email = fakergen.email()

		# New entry
		user = User.objects.get_or_create(first_name=fake_first_name,
										last_name=fake_last_name,
										email=fake_email)[0]

if __name__=="__main__":
	print("populate Database")
	populate(20)
	print("complete")
	
