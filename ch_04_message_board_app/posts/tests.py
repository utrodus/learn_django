from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostTest(TestCase):
    # setUpTestData method is used to create objects that will be used by all test methods in the class.
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            text="This is a test post.", description="This is a test description."
        )

    # test_model_content method is used to test the content of the model.
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test post.")
        self.assertEqual(self.post.description, "This is a test description.")

    # test_url_exists_at_correct_location method is used to test the URL for '/' (Homepage) and should return 200 HTTP status code
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # test_url_available_by_name method is used to test the URL name for the home page
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # test_template_name_correct method is used to test the template name for the home page
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    # test_template_correct_content method is used to test the content of the home page should contain the test post and description created in the setUpTestData method.
    def test_template_correct_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test post.")
        self.assertContains(response, "This is a test description.")

    # refactored test methods
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test post.")
        self.assertContains(response, "This is a test description.")
