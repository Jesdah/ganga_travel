from django.test import TestCase
from .models import Post

class ModelTestCaste(TestCase):

    def test_if_title_works(self):
        post = Post.title.create(name='testing')
        self.assertEqual(max_length=200)


# Create your tests here.
