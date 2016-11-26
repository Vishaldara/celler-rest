from django.test import TestCase
from .models import Post


# Create your tests here.
class PostTest(TestCase):
    def test_str(self):
        test_title = Post(title='My Latest Blog')
        self.assertEqual(str(test_title),
                         'My Lastest Blog')
