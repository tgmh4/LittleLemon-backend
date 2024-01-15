from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.all(name='Pizza', price=12.99)
        Menu.objects.all(name='Salad', price=6.99)

    