from django.test import TestCase
from pokedex.forms import PokemonForm
class PokemonFormTest(TestCase):
    def test_valid_form(self):
        data = {'name': 'charmander', 'type': 'fire', 'level': 5}
        form = PokemonForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', 'type': 'fire', 'level': 5}
        form = PokemonForm(data=data)
        self.assertFalse(form.is_valid())
