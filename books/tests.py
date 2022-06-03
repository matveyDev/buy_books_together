from django.test import TestCase
from .models import BooksForBuy, BooksForFree, Category
from django.utils import timezone
from django.contrib.auth import get_user_model

class TestBooksModels(TestCase):

    def test_create_category(self):
        test_category = Category.objects.create(
            title='Code',
            slug='code'
        )

        self.assertEqual(test_category.title, 'Code')
        self.assertEqual(test_category.slug, 'code')
    
    def test_create_book_for_buy(self):
        test_category = Category.objects.create(
            title='Code',
            slug='code'
        )
        test_category2 = Category.objects.create(
            title='Code2',
            slug='code2'
        )

        book_test = BooksForBuy.objects.create(
            title='Django Book',
            description='Best book',
            image='../media/photos/elon.jpg',
            finish_goal=2000,
            current_goal=0,
            end=False,
            slug='django-book',
            category=test_category
        )

        self.assertEqual(book_test.title, 'Django Book')
        self.assertEqual(book_test.description, 'Best book')
        self.assertEqual(book_test.image, '../media/photos/elon.jpg')
        self.assertEqual(book_test.finish_goal, 2000)
        self.assertEqual(book_test.current_goal, 0)
        self.assertEqual(book_test.slug, 'django-book')
        self.assertEqual(book_test.category, test_category)
        self.assertLess(book_test.created_at, timezone.now())
        self.assertFalse(book_test.end)

        book_test2 = BooksForBuy.objects.create(
            title='Django API book',
            description='Best book2',
            image='../media/photos/elon.jpg',
            finish_goal=1500,
            current_goal=200,
            end=True,
            slug='django-api-book',
            category=test_category2
        )

        self.assertEqual(book_test2.title, 'Django API book')
        self.assertEqual(book_test2.description, 'Best book2')
        self.assertEqual(book_test2.image, '../media/photos/elon.jpg')
        self.assertEqual(book_test2.finish_goal, 1500)
        self.assertEqual(book_test2.current_goal, 200)
        self.assertEqual(book_test2.slug, 'django-api-book')
        self.assertEqual(book_test2.category, test_category2)
        self.assertLess(book_test2.created_at, timezone.now())
        self.assertTrue(book_test2.end)

    def test_create_book_for_free(self):
        User = get_user_model()
        test_user = User.objects.create(
            email='exple@exp.exp',
            password='Test1234',
            full_name='Тест Тестович Тестов',
            username='test1',
        )
        users = User.objects.all()

        test_category = Category.objects.create(
            title='Code',
            slug='code'
        )

        book_test = BooksForFree.objects.create(
            title='Free book',
            description='best free book',
            image='../media/photos/elon.jpg',
            user=test_user,
            slug='free-book',
            category=test_category
        )

        self.assertEqual(book_test.title, 'Free book')
        self.assertEqual(book_test.description, 'best free book')
        self.assertEqual(book_test.image, '../media/photos/elon.jpg')
        self.assertEqual(book_test.slug, 'free-book')
        self.assertEqual(book_test.category, test_category)
        self.assertEqual(book_test.views, 0)
        self.assertIn(book_test.user, users)