from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    # Test URLs for the Home page are working:
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # Test URL names for Home pages are correct
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # Test Home page uses correct template name
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    # Test Home page shows correct content for the page
    def test_template_correct_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h2>Home Page</h2>")


class AboutpageTests(SimpleTestCase):
    # Test URLs for the About page are working:
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    # Test URL names for About pages are correct
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    # Test About page uses correct template name
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    # Test About page shows correct content for the page
    def test_template_correct_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h2>About Page</h2>")
