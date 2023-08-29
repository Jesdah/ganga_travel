from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Adventure, Post


class TestViews(TestCase):
    """
    Test views.
    """

    def setUp(self):
        """ 
        Setup test 
        """
        username = "project4"
        password = "dator123"
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create Adventure
        adventure = Adventure.objects.create(
            name="Adventure1",
            date="2023-08-01",
            author=get_object_or_404(User),
            featured_image="image.jpg",
            )
        # Create Destination
        post = Post.objects.create(title="testDestination",
        created_on="2023-08-01", featured_image="image1.jpg",
        adventure_id=1)


    def test_adventure_list(self):
        """
        Test adventure list
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_get(self):
        """
        Test Destination List
        """

         # Create Adventure
        adventure = Adventure.objects.create(
            name="Adventure1",
            date="2023-08-01",
            author=get_object_or_404(User),
            featured_image="image.jpg",
            )
        # Create Destination
        post = Post.objects.create(title="testDestination",
        created_on="2023-08-01", featured_image="image1.jpg",
        adventure_id=1)

        response = self.client.get('/2/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post.html')

    def test_add_adventure(self):
        """
        Test add adventure function.
        """
        username = "jesper"
        password = "dator123"
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        response = self.client.get('/add/2/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_adventure.html')
