import unittest
from unittest.mock import MagicMock
from pizzeria import Pizza, CartePizzeria, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        """Initialisation des données pour les tests."""
        self.carte = CartePizzeria()
        self.pizza1 = Pizza("Margherita", ["Tomate", "Mozzarella"], 8.5)
        self.pizza2 = Pizza("Pepperoni", ["Tomate", "Mozzarella", "Pepperoni"], 10.0)

    def test_carte_vide(self):
        """Test si la carte est vide au départ."""
        self.assertTrue(self.carte.is_empty())

    def test_ajout_pizza(self):
        """Test de l'ajout d'une pizza."""
        self.carte.add_pizza(self.pizza1)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_suppression_pizza(self):
        """Test de la suppression d'une pizza existante."""
        self.carte.add_pizza(self.pizza1)
        self.carte.remove_pizza("Margherita")
        self.assertTrue(self.carte.is_empty())

    def test_suppression_pizza_inexistante(self):
        """Test de la suppression d'une pizza qui n'existe pas (doit lever une exception)."""
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("Hawaïenne")


class TestCartePizzeriaAvecMock(unittest.TestCase):
    def setUp(self):
        """Initialisation d'une carte de pizzeria avec un mock."""
        self.carte = CartePizzeria()
        self.pizza_mock = MagicMock(spec=Pizza)
        self.pizza_mock.nom = "MockPizza"
        self.pizza_mock.ingredients = ["Fromage", "Tomate"]
        self.pizza_mock.prix = 9.99

    def test_ajout_pizza_mock(self):
        """Test l'ajout d'une pizza mockée dans la carte."""
        self.carte.add_pizza(self.pizza_mock)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_suppression_pizza_mock(self):
        """Test la suppression d'une pizza mockée."""
        self.carte.add_pizza(self.pizza_mock)
        self.carte.remove_pizza("MockPizza")
        self.assertTrue(self.carte.is_empty())

    def test_suppression_pizza_mock_inexistante(self):
        """Test la suppression d'une pizza qui n'existe pas (mock)."""
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("PizzaFantôme")


if __name__ == "__main__":
    unittest.main()
