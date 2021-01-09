from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username = 'fadi', email='fadi@gmail.com', password='fadi000000')
        self.assertEqual(user.email, 'fadi@gmail.com')

    def test_create_duplicate_user(self):        
        try:
            User = get_user_model()
            User.objects.create_user(username = 'fadi', email='fadi@gmail.com', password='fadi123456')
        except Exception as e:
            print(e)
        
    def test_create_none_user(self):
        User = get_user_model()
        with self.assertRaises(Exception):
            User.objects.create_user(username = '', email='', password="fadi123456")