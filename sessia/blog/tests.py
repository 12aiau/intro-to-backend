from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Post

class PostAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.client = APIClient()
        self.client.login(username='testuser', password='pass123')

    def test_create_post(self):
        response = self.client.post('/api/posts/', {
            'title': 'Новый пост',
            'content': 'Контент поста'
        })
        self.assertEqual(response.status_code, 201)
