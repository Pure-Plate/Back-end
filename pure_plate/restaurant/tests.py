from django.test import TestCase, Client
from django.urls import reverse
from .models import Restaurant

class RestaurantSearchTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Creating restaurant data for testing
        Restaurant.objects.create(
            name='Vegan Bliss', address='123 Green Way', vegan=True, halal=False,
            gluten_free=True, lacto_free=False, latitude=10.0, longitude=20.0,
            time='09:00-21:00', photo='vegan_bliss.jpg', phone='111-222-3333',
            review_count=100, avg_rating=4.8
        )
        Restaurant.objects.create(
            name='Halal Heaven', address='456 Crescent Moon', vegan=False, halal=True,
            gluten_free=False, lacto_free=True, latitude=30.0, longitude=40.0,
            time='10:00-22:00', photo='halal_heaven.jpg', phone='444-555-6666',
            review_count=80, avg_rating=4.6
        )

    def test_search_for_vegan_restaurants(self):
        # Test if the corresponding restaurant is returned when selecting the vegan option.
        response = self.client.get(reverse('restaurants-in-categories'), {'categories': 'vegan'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Vegan Bliss', response.content.decode())

    def test_search_for_halal_restaurants(self):
        # Test if the corresponding restaurant is returned when selecting the halal option.
        response = self.client.get(reverse('restaurants-in-categories'), {'categories': 'halal'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Halal Heaven', response.content.decode())

    def test_search_for_gluten_free_and_lacto_free_restaurants(self):
        # Test if there are no corresponding restaurants when selecting both gluten-free and lactose-free options.
        response = self.client.get(reverse('restaurants-in-categories'), {'categories': 'glutenfree,lactofree'})
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        # This part may need modification depending on the actual returned content.
        self.assertTrue('No restaurants found' in content or '[]' in content)
