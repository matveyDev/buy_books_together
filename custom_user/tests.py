from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import datetime

class TestUserModel(TestCase):

    def test_create_user(self):
        user = get_user_model()
        user_test = user.objects.create(
            email='exple@exp.exp',
            password='Test1234',
            full_name='Тест Тестович Тестов',
            age=datetime.datetime(2002, 3, 14),
            username='test1',
        )
        new_token = Token.objects.create(user=user_test)

        self.assertEqual(user_test.email, 'exple@exp.exp')
        self.assertEqual(user_test.password, 'Test1234')
        self.assertEqual(user_test.full_name, 'Тест Тестович Тестов')
        self.assertEqual(user_test.username, 'test1')
        self.assertEqual(new_token.user_id, user_test.pk)
        self.assertEqual(user_test.rating, 0)

        self.assertLess(user_test.age, datetime.datetime.today())

        self.assertFalse(user_test.is_staff)
        self.assertFalse(user_test.is_superuser)
        self.assertFalse(user_test.subscriber)
        self.assertTrue(user_test.is_active)