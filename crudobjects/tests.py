from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Crudobject, Comment


class CrudobjectTests(TestCase):


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )

        self.crudobject = Crudobject.objects.create(
            title = 'Harry Potter',
            author = 'JK Rowling',
            price = '25.00',
        )

        self.review = Comment.objects.create(
            crudobject = self.crudobject,
            author = self.user,
            text = 'An excellent review',
        )

    def test_crudobject_listing(self):
        self.assertEqual(f'{self.crudobject.title}', 'Harry Potter')
        self.assertEqual(f'{self.crudobject.author}', 'JK Rowling')
        self.assertEqual(f'{self.crudobject.price}', '25.00')

    def test_crudobject_list_view(self):
        response = self.client.get(reverse('crudobject_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'crudobjects/crudobject_list.html')

    def test_crudobject_detail_view(self):
        response = self.client.get(self.crudobject.get_absolute_url())
        no_response = self.client.get('/crudobject/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'An excellent review')
        self.assertTemplateUsed(response, 'crudobjects/crudobject_detail.html')

    def test_crudobject_create_view(self):
        response = self.client.get(self.crudobject.get_absolute_url())
        no_response = self.client.get('/crudobject/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)




# Create your tests here.
