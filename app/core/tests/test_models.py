from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Creating a new user with email successful"""
        email = 'test@email.com'
        password = 'Test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """The email for a new user is normalized"""
        email = 'test@EMAIL.COM'
        user = get_user_model().objects.create_user(email, 'Test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test1234')

    def test_create_new_superuser(self):
        """Creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@email.com',
            'Test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
