import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User

# Credentials
USERNAME = "admin"
PASSWORD = "johnadrielle2020001874"
EMAIL = "jammandap.student@ua.edu.ph"

# Logic: Create user only if it doesn't exist
if not User.objects.filter(username=USERNAME).exists():
    print(f"Creating superuser: {USERNAME}")
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
else:
    print("Superuser already exists. Skipping creation.")