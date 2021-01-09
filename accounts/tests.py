from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class CreatUsersTests(TestCase):

    def test_create_user(self):
        self.user = get_user_model().objects.create_user(
            username = 'fadi',
            email='fadi@gmail.com',
            password='fadi000000',
            first_name = 'fadi',
            last_name = 'hb'
        )
        self.assertEqual(self.user.email, 'fadi@gmail.com')

    def test_create_duplicate_user(self):        
        self.user = get_user_model().objects.create_user(
            username = 'fadi', 
            email='fadi@gmail.com', 
            password='fadi123456',
            first_name = 'fadi',
            last_name = 'hb'
        )

        
    def test_create_none_user(self):
        self.user = get_user_model().objects.create_user(
            username = '', 
            email='', 
            password='',
            first_name = '',
            last_name = ''
        )