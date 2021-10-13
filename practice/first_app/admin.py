from django.contrib import admin
# from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# print("this is admin page", BASE_DIR)
from .models import Contact
admin.site.register(Contact)
# Register your models here.

# from first_app.models import Contact