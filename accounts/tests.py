from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class CreateUsersTests(TestCase):

    def test_create_user(self):
        self.user = get_user_model().objects.create_user(
            username = 'fadi',
            email='fadi@gmail.com',
            password='fadi000000',
            first_name = 'fadi',
            last_name = 'hb'
        )
        self.assertEqual(self.user.email, 'fadi@gmail.com')