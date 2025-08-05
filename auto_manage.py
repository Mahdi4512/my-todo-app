# auto_manage.py

import os
import django

# این خط مهمه، چون settings داخل project هست
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.core.management import call_command

try:
    print("📦 Running migrate...")
    call_command("migrate")

    print("🎨 Running collectstatic...")
    call_command("collectstatic", interactive=False, verbosity=0)

except Exception as e:
    print("❌ Error during auto_manage:", e)
