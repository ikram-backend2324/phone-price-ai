from django.core.management.base import BaseCommand
from vehicles.models import PhoneBrand

BRANDS = [
    "Apple", "Samsung", "Google", "OnePlus", "Xiaomi",
    "Huawei", "Sony", "Motorola", "Nokia", "Oppo",
    "Vivo", "Realme", "Nothing", "Asus", "Other",
]

class Command(BaseCommand):
    help = "Seed default phone brands"

    def handle(self, *args, **options):
        created = 0
        for name in BRANDS:
            _, was_created = PhoneBrand.objects.get_or_create(name=name)
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} new brands"))
