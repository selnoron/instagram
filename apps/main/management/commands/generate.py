from main.models import MyUser  
from faker import Faker
from django.core.management.base import BaseCommand, CommandError


fake = Faker()

class Command(BaseCommand):
    def generate_users(self):
        user_list = []
        for i in range(1000000):
            user = MyUser(
                email=fake.email(),
                nickname=fake.user_name(),
                description=fake.sentence(),
                is_staff=False 
            )
            user_list.append(user)

        MyUser.objects.bulk_create(user_list)

    def handle(self, *args, **kwargs):
        self.generate_users()
        print("FINISH")