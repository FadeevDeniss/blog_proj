from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog.models import Post


class BlogTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='Test title',
            body='Test body content',
            author=self.user,
        )

    def test_str_repr(self):
        post = Post(title='Sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "Test title")
        self.assertEqual(f"{self.post.body}", "Test body content")
        self.assertEqual(f"{self.post.author}", "testuser")

    def test_created_at_correct_timestamp(self):
        self.assertIsNotNone(self.post.created_at)
        self.assertIsInstance(self.post.created_at, datetime)

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test body content")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get(reverse("post_detail", args=[1]))
        no_response = self.client.get(
            reverse(
                "post_detail",
                args=[100000]
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test title")
        self.assertTemplateUsed(response, "post_detail.html")
