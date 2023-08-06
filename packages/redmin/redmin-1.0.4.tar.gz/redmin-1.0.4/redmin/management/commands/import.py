import logging
import time

import django.apps
import requests
from django.core.management.commands import loaddata

logger = logging.getLogger(__name__)


# python manage.py import host.com
class Command(loaddata.Command):
    def add_arguments(self, parser):
        super().add_arguments(parser)

    def handle(self, *args, **options):
        logger.info("import begin")
        from django.conf import settings
        app_name = getattr(settings, "APP_NAME")
        if not settings.DEBUG: return

        logger.info("Clear all models start")
        for model in django.apps.apps.get_models():
            model.objects.all().delete()
        logger.info("Clear all models end")
        host = args[0]
        today = time.strftime("%Y-%m-%d")
        name = f"{today}.json.gz"
        url = f"https://{host}/backup/{app_name}/{name}"
        logger.info(f"download {url} start")
        r = requests.get(url, stream=True)
        file = f"/tmp/{app_name}-{name}"
        f = open(file, "wb")
        for chunk in r.iter_content(chunk_size=512):
            if chunk: f.write(chunk)
        f.close()

        logger.info(f"{url} -> {file}")
        logger.info("loaddata begin")
        super().handle(*(file,), **options)
        logger.info("loaddata end")
        logger.info("import end")
