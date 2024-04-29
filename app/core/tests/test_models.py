"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTests(TestCase):
    """Test Models."""

    def test_create_user_with_email_succesfull(self):
        email = 'caio@mail.com'
        password = 'senha123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
