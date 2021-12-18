from faker import Faker

from django.core.management.base import BaseCommand
from app.models import Table


class Command(BaseCommand):
    help = 'Заполняет базу данных случайными данными.'

    def add_arguments(self, parser):
        parser.add_argument('quantity', action='append', type=int)
    
    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        for _ in range(options['quantity'][0]):
            Table.objects.create(
                name=fake.address(),
                date=fake.date(),
                quantity=fake.bothify('###'),
                distance=fake.bothify('###'),
            )
