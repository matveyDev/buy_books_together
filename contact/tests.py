from django.test import TestCase
from .models import Contact
from django.utils import timezone

class TestContactModel(TestCase):

    def test_create_contact(self):
        test_contact = Contact.objects.create(
            email='matveytri777@gmail.com'
        )

        self.assertEqual(test_contact.email, 'matveytri777@gmail.com')
        self.assertLess(test_contact.created_at, timezone.now())