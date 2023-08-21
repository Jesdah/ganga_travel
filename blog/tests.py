from django.test import TestCase
from .models import Adventure, Post



class TestViews(TestCase):

    def test_adventure_list(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'template/index.html')

    def test_get(self):
        response = self.client.get('<int:adventure_id>/<author_id>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'template/post.html')
    
    def test_add_post(self):
        response = self.client.post('<int:adventure_id>/<author_id>/', {'title': 'Test Add Destination'},
        {'content': 'Test Add Destination'},{'featured_image': 'image.jpg'})
        self.assertRedirects(response, '<int:adventure_id>/<author_id>/')