import unittest
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

if __name__ == "__main__":
    unittest.main()
