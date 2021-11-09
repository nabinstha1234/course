from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve


# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, "Homepage")

    def test_homepagae_does_not_contains_incorrect_html(self):
        respose = self.client.get('/')
        self.assertNotContains(
            respose,"fuck you"
        )
