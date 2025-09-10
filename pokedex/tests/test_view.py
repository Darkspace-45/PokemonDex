from django.urls import reverse
from django.test import TestCase

class PokemonViewsTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('pokedex:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pokedex/index.html')

    def test_pokemon_list_view(self):
        response = self.client.get(reverse('pokedex:pokemon_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pokedex/pokemon_list.html')
