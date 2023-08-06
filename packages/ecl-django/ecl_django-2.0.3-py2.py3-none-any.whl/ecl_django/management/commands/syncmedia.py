from django.core.management.base import BaseCommand
from django.conf import settings
from ecl_tools.deployment import sync_media_to_s3


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """
        Sync media to s3 using ecl_tools.deployment.sync_media_to_s3.
        """
        BUCKET_NAME = getattr(
            settings, "AWS_STATIC_STORAGE_BUCKET_NAME", settings.AWS_STORAGE_BUCKET_NAME
        )
        KEY = getattr(settings, "AWS_STATIC_ACCESS_KEY_ID", settings.AWS_ACCESS_KEY_ID)
        SECRET = getattr(
            settings, "AWS_STATIC_SECRET_ACCESS_KEY", settings.AWS_SECRET_ACCESS_KEY
        )
        HEADERS = getattr(settings, "AWS_HEADERS", None)
        DISTRIBUTION_ID = getattr(settings, "AWS_CF_DISTRIBUTION_ID", None)

        if len(args) > 0:
            folder = args[0]
        else:
            folder = settings.STATIC_ROOT

        sync_media_to_s3(BUCKET_NAME, KEY, SECRET, HEADERS, DISTRIBUTION_ID, folder)

