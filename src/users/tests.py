from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.login_url = reverse(
            "login"
        )  # Update with the correct name of your login URL
        self.logout_url = reverse(
            "logout_success"
        )  # Update with the correct name of your logout URL

    def test_login_view(self):
        response = self.client.post(
            self.login_url, {"username": "testuser", "password": "12345"}
        )
        self.assertEqual(
            response.status_code, 302
        )  # Assuming redirect after successful login
        self.assertTrue(
            "_auth_user_id" in self.client.session
        )  # Check if the user is logged in

    def test_logout_view(self):
        # First, log the user in
        self.client.login(username="testuser", password="12345")

        # Then, log the user out
        response = self.client.get(self.logout_url)
        self.assertEqual(
            response.status_code, 200
        )  # Assuming direct rendering of success page without redirect
        self.assertFalse(
            "_auth_user_id" in self.client.session
        )  # Check if the user is logged out


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # This method is now correctly defined as a class method
        cls.user = User.objects.create(name="Jim")

    def test_user_name(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("name").max_length
        self.assertEqual(max_length, 120)
