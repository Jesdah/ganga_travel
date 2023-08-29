from django.test import TestCase
from .models import Adventure, Post, Comment
from django.urls import reverse


class TestViews(TestCase):

    def test_adventure_list(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get(self):
        adventure_id = 1
        author_id = 1
        response = self.client.get(reverse('adventure_detail', args=[adventure_id, author_id]))
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'post.html')

    def test_add_adventure(self):
        response = self.client.post('add',
        {'name': 'Test Added Item',
        'date': '2023-10-11', 'featured_image': 'image.jpg'})
        # self.assertRedirects(response, '')

    def test_delete_adventure(self):
        auth_user = 2
        adventure = Adventure.objects.create(name='Going on an Adventure',
         date='2023-10-11', featured_image='image.jpg', id=1, author_id=2 )
        response = self.client.get(f'/delete/{adventure.id}')
        self.assertRedirects(response, '/')
        existing_adventure = Adventure.objects.filter(id=adventure.id)
        self.assertEqual(len(existing_adventure), 0)

    # def test_edit_adventure(self):
    #     adventure = Adventure.objects.create(name='Going on an Adventure',
    #      date='2023-10-11', featured_image='image.jpg')
    #     response = self.client.post(f'/edit/{adventure.id}',
    #      {'name': 'Going on an Updated Adventure'},
    #      {'date': '2023-10-12'},
    #      {'featured_image': 'image2.jpg'})
    #     self.assertRedirects(response, '/')
    #     updated_adventure = Adventure.objects.get(id=adventure.id)
    #     self.assertEqual(updated_adventure.name, 'Going on an Updated Adventure')
    #     self.assertEqual(updated_adventure.date, '2023-10-12')
    #     self.assertEqual(updated_adventure.featured_image, 'image2.jpg')

    # def test_add_post(self):
    #     response = self.client.post('<int:adventure_id>/<author_id>/',
    #     {'title': 'Test Add Destination'},
    #     {'content': 'Test Add Destination'},
    #     {'featured_image': 'image.jpg'})
    #     self.assertRedirects(response, '<int:adventure_id>/<author_id>/')


    # def test_delete_post(self):
    #     post = Post.objects.create(title='New Destination',
    #     Content='When we get to this point we drink coffee!',
    #     featured_image='image.jpg')
    #     response = self.client.get(f'/delete/{post.id}')
    #     self.assertRedirects(response, '<int:adventure_id>/<author_id>/')
    #     existing_post = Post.objects.filter(id=post.id)
    #     self.assertEqual(len(existing_post), 0)

    # def test_edit_post(self):
    #     post = Post.objects.create(title='New Destination',
    #     content='When we get to this point we drink coffee!',
    #     featured_image='image.jpg')
    #     response = self.client.post(f'/edit/{post.id}',
    #      {'title': 'Updated Destination'},
    #      {'content': 'When we get to this point we drink Tea!'},
    #      {'featured_image': 'image2.jpg'})
    #     self.assertRedirects(response, '<int:adventure_id>/<author_id>/')
    #     updated_post = Post.objects.get(id=post.id)
    #     self.assertEqual(updated_post.title, 'Updated Destination')
    #     self.assertEqual(updated_post.content, 'When we get to this point we drink Tea!')
    #     self.assertEqual(updated_post.featured_image, 'image2.jpg')

    # def test_add_comment(self):
    #     response = self.client.post('<int:adventure_id>/<author_id>/',
    #     {'body': 'Test Add Comment'})
    #     self.assertRedirects(response, '<int:adventure_id>/<author_id>/')

    # def test_delete_comment(self):
    #     comment = Comment.objects.create(body='New Comment')
    #     response = self.client.get(f'/delete/{comment.id}')
    #     self.assertRedirects(response, '<int:adventure_id>/<author_id>/')
    #     existing_comment = Comment.objects.filter(id=comment.id)
    #     self.assertEqual(len(existing_comment), 0)
