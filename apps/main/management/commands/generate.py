from main.models import MyUser 
from faker import Faker
from django.core.management.base import BaseCommand, CommandError
import random as rd


fake = Faker()

class Command(BaseCommand):
    def generate_users(self):
        n = 5000
        for i in range(n):
            print("\033[H\033[J")
            print(round((i/n)*100, 1),'%', 'I'*int((i/n)*100) + '_'*int(100 - int((i/n)*100)))
            MyUser.objects.create(
                email=rd.choice(['df','de', 'ec', 'e', 'd', 'w', 'dds'])+str(rd.randint(1, 99999))+fake.email(),
                nickname=fake.user_name(),
                description=fake.sentence(),
                is_staff=False
            )


    def handle(self, *args, **kwargs):
        print("Start processings")
        self.generate_users()
        print("Complete")