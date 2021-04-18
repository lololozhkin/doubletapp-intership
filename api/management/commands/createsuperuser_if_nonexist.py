from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Create a superuser if none exist
    Example:
        manage.py createsuperuser_if_nonxist --user=admin --password=ilovejs
    """

    def add_arguments(self, parser):
        parser.add_argument("--username", required=True)
        parser.add_argument("--password", required=True)
        parser.add_argument("--email", default="doubletap@example.com")

    def handle(self, *args, **options):
        User = get_user_model()

        username = options["username"]
        password = options["password"]
        email = options["email"]

        if User.objects.filter(username=username).exists():
            return

        User.objects.create_superuser(
            username=username,
            password=password,
            email=email
        )

        self.stdout.write(f'Superuser "{username}" was created')