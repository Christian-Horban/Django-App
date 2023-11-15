from django.test import TestCase
from .models import User


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
