from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.


class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/pages")
        self.assertEqual(response.status_code, 301)


class PostModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="testbot",
            email="jojoboy12@gmail.com",
            password="jojoboy@1992",
        )

        self.post = Post.objects.create(
            title="Hello", body="This is my Post", User=self.user, image = None

        )

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_text = f"{post.title}"
        self.assertEqual(expected_text, "Hello")

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', "Hello")  
        self.assertEqual(f'{self.post.User}', "testbot") 
        self.assertEqual(f'{self.post.body}', "This is my Post")  

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is my Post")
        self.assertTemplateUsed(response, "index.html")

   


