from django.test import TestCase

from pokedex.models import Pokemon

class PokemonModelTest(TestCase):
    def setUp(self):
        self.pokemon = Pokemon.objects.create(
            name="pikachu",
            type="electric",
            level=5
        )

    def test_pokemon_creation(self):
        self.assertEqual(self.pokemon.name, "pikachu")
        self.assertEqual(self.pokemon.level, 5)
