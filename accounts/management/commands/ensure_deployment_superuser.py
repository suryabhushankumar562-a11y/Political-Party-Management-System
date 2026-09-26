import os

from django.core.management.base import BaseCommand, CommandError

from accounts.models import CustomUser


class Command(BaseCommand):
    help = "Create the configured deployment superuser if its username is unused."

    def handle(self, *args, **options):
        username = os.environ.get("SUPERUSER_USERNAME", "").strip()
        email = os.environ.get("SUPERUSER_EMAIL", "").strip()
        password = os.environ.get("SUPERUSER_PASSWORD", "")

        missing = [
            name
            for name, value in (
                ("SUPERUSER_USERNAME", username),
                ("SUPERUSER_EMAIL", email),
                ("SUPERUSER_PASSWORD", password),
            )
            if not value
        ]
        if missing:
            raise CommandError(
                "Set the required environment variable(s): " + ", ".join(missing)
            )

        if CustomUser.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(
                    f"User '{username}' already exists; leaving it unchanged."
                )
            )
            return

        CustomUser.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            role="SUPERADMIN",
        )
        self.stdout.write(self.style.SUCCESS("Deployment superuser created."))
