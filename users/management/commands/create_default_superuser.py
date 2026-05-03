from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Create default admin superuser"

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin123", role="admin")
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created (password: admin123)"))
        else:
            self.stdout.write("Superuser 'admin' already exists")
