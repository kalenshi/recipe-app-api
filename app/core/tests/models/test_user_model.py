"""
Tests the custom user model
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTest(TestCase):
    """
    Tests the default user model
    """

    def test_create_user_with_email_successful(self):
        """
        Test creating user model with email is successful.
        """
        email = "test@example.com"
        password = "testpassword123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test email is normalized for new users
        """
        sample_emails = [
            ["test1@EXAMPLE.COM", "test1@example.com"],
            ["Test2@EXAMPLE.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """
        Test creating a user without email raises a ValueError
        """
        with self.assertRaises(ValueError) as ve:
            _ = get_user_model().objects.create_user(email="", password="password123")
        self.assertEqual(str(ve.exception), "Email must be provided for all users.")

    def test_create_superuser(self):
        """
        Test creating a superuser
        """
        user = get_user_model().objects.create_superuser(
            email="test@example.com",
            password="test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
