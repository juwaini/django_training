from django.test import TestCase

from .models import Book

class TestBookModel(TestCase):

    def test_str(self):
        b = Book.objects.create(title='test', author='test')
        self.assertEqual(b.title, 'test')

