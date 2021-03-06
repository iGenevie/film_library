from django.test import TestCase, Client
from django.utils import timezone
from .models import User, Film


class UserTestCase(TestCase):
    def setUp(self):
        self.mary = User.objects.create(login='Mary', created_date=timezone.now())
        self.vladislav = User.objects.create(login='Vladislav', created_date=timezone.now())

    def test_users_str(self):
        self.assertEqual(self.mary.__str__(), 'Mary')
        self.assertEqual(self.vladislav.__str__(), 'Vladislav')


class FilmTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(login='user', created_date=timezone.now())
        self.garfield = Film.objects.create(
            user=user,
            original_title='Garfield',
            production="Davis Entertainment Company",
            country="United States",
            year='2004',
            added_date=timezone.now()
        )

    def test_film_str(self):
        self.assertEqual(self.garfield.__str__(), 'Garfield')


class TestURLs(TestCase):
    def test_users_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_new(self):
        client = Client()
        response = client.get('/user/new/')
        self.assertEqual(response.status_code, 200)
