from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Reviews, Rating
from books.models import BooksForFree
from django.utils import timezone

class TestFeedbackModels(TestCase):
    def test_create_comments(self):
        User = get_user_model()

        test_user = User.objects.create(
            email='exple@exp.exp',
            password='Test1234',
            full_name='Тест Тестович Тестов',
            username='test1',
        )

        test_book = BooksForFree.objects.create(
            title='Free book',
            description='best free book',
            image='../media/photos/elon.jpg',
            user=test_user,
            slug='free-book',
        )

        test_comment = Reviews.objects.create(
            text='Best book!',
            author=test_user,
            book=test_book,
        )

        self.assertEqual(test_comment.text, 'Best book!')
        self.assertEqual(test_comment.author, test_user)
        self.assertEqual(test_comment.book, test_book)
        self.assertEqual(test_comment.likes, 0)
        self.assertLess(test_comment.created_at, timezone.now())

        test_comment_with_parent = Reviews.objects.create(
            text='Best book!',
            author=test_user,
            book=test_book,
            parent=test_comment,
        )

        self.assertEqual(test_comment_with_parent.text, 'Best book!')
        self.assertEqual(test_comment_with_parent.author, test_user)
        self.assertEqual(test_comment_with_parent.book, test_book)
        self.assertEqual(test_comment_with_parent.likes, 0)
        self.assertEqual(test_comment_with_parent.parent, test_comment)
        

    def test_create_rating(self):
        User = get_user_model()
        test_user = User.objects.create(
            email='exple@exp.exp',
            password='Test1234',
            full_name='Тест Тестович Тестов',
            username='test1',
        )

        test_book = BooksForFree.objects.create(
            title='Free book',
            description='best free book',
            image='../media/photos/elon.jpg',
            user=test_user,
            slug='free-book',
        )

        test_rating = Rating.objects.create(
            book=test_book,
            author=test_user,
            rating=5,
        )
        
        self.assertEqual(test_rating.book, test_book)
        self.assertEqual(test_rating.author, test_user)
        self.assertEqual(test_rating.rating, 5)