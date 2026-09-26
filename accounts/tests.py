from io import StringIO
from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase

from accounts.models import CustomUser


class EnsureDeploymentSuperuserTests(TestCase):
    def setUp(self):
        self.environment = patch.dict(
            "os.environ",
            {
                "SUPERUSER_USERNAME": "deployment-admin",
                "SUPERUSER_EMAIL": "admin@example.com",
                "SUPERUSER_PASSWORD": "A-strong-deployment-password-482!",
            },
        )
        self.environment.start()
        self.addCleanup(self.environment.stop)

    def test_creates_configured_superuser(self):
        call_command("ensure_deployment_superuser", stdout=StringIO())

        user = CustomUser.objects.get(username="deployment-admin")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.role, "SUPERADMIN")
        self.assertTrue(user.check_password("A-strong-deployment-password-482!"))

    def test_leaves_existing_username_unchanged(self):
        user = CustomUser.objects.create_user(
            username="deployment-admin",
            email="original@example.com",
            password="Original-password-482!",
        )

        call_command("ensure_deployment_superuser", stdout=StringIO())

        user.refresh_from_db()
        self.assertEqual(user.email, "original@example.com")
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password("Original-password-482!"))
