import shutil
import os
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Copy static files to staticfiles folder'

    def handle(self, *args, **options):
        src = settings.STATICFILES_DIRS[0]
        dst = settings.STATIC_ROOT
        os.makedirs(dst, exist_ok=True)
        shutil.copytree(src, dst, dirs_exist_ok=True)
        self.stdout.write('Static files copied successfully!')