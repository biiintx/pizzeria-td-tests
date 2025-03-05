import unittest
from unittest.mock import MagicMock
from pizzeria import Pizza, Boisson, Dessert, CartePizzeria, CartePizzeriaException


class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        """Initialisation des données pour les tests."""
        self.carte = CartePizzeria()
        self.pizza1 = Pizza("Margherita", 8.5, "Classique italienne", ["Tomate", "Mozzarella"], "tomate")
        self.pizza2 = Pizza("Pepperoni", 10.0, "Pizza épicée", ["Tomate", "Mozzarella", "Pepperoni"], "tomate")
        self.boisson1 = Boisson("Coca-Cola", 3.0, False)
        self.boisson2 = Boisson("Vin rouge", 12.0, True)
        self.dessert1 = Dessert("Tiramisu", 6.0, ["Mascarpone", "Café"], True)
        self.dessert2 = Dessert("Glace", 4.0, ["Lait", "Sucre"], False)

    def test_carte_vide(self):
        """Test si la carte est vide au départ."""
        self.assertTrue(self.carte.is_empty())

    def test_ajout_pizza(self):
        """Test de l'ajout d'une pizza."""
        self.carte.add(self.pizza1)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_ajout_boisson(self):
        """Test de l'ajout d'une boisson."""
        self.carte.add(self.boisson1)
        self.assertEqual(self.carte.nb_drinks(), 1)

    def test_ajout_dessert(self):
        """Test de l'ajout d'un dessert."""
        self.carte.add(self.dessert1)
        self.assertEqual(self.carte.nb_desserts(), 1)

    def test_suppression_element(self):
        """Test de la suppression d'un élément existant."""
        self.carte.add(self.pizza1)
        self.carte.remove("Margherita")
        self.assertTrue(self.carte.is_empty())

    def test_exception_ajout_pizza_existe_deja(self):
        """Test de l'ajout d'une pizza déjà existante (doit lever une exception)."""
        self.carte.add(self.pizza1)
        with self.assertRaises(CartePizzeriaException):
            self.carte.add(self.pizza1)

    def test_exception_suppression_element_inexistant(self):
        """Test de la suppression d'un élément qui n'existe pas (doit lever une exception)."""
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove("Inconnu")


class TestCartePizzeriaAvecMock(unittest.TestCase):
    def setUp(self):
        """Initialisation d'une carte de pizzeria avec un mock."""
        self.carte = CartePizzeria()
        self.pizza_mock = MagicMock(spec=Pizza)
        self.pizza_mock.nom = "MockPizza"
        self.pizza_mock.ingredients = ["Fromage", "Tomate"]
        self.pizza_mock.prix = 9.99

        self.boisson_mock = MagicMock(spec=Boisson)
        self.boisson_mock.nom = "MockDrink"
        self.boisson_mock.prix = 5.0
        self.boisson_mock.alcool = False

        self.dessert_mock = MagicMock(spec=Dessert)
        self.dessert_mock.nom = "MockDessert"
        self.dessert_mock.prix = 7.5
        self.dessert_mock.ingredients = ["Chocolat"]
        self.dessert_mock.fait_maison = True

    def test_ajout_pizza_mock(self):
        """Test l'ajout d'une pizza mockée dans la carte."""
        self.carte.add(self.pizza_mock)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_ajout_boisson_mock(self):
        """Test l'ajout d'une boisson mockée."""
        self.carte.add(self.boisson_mock)
        self.assertEqual(self.carte.nb_drinks(), 1)

    def test_ajout_dessert_mock(self):
        """Test l'ajout d'un dessert mocké."""
        self.carte.add(self.dessert_mock)
        self.assertEqual(self.carte.nb_desserts(), 1)

    def test_suppression_pizza_mock(self):
        """Test la suppression d'une pizza mockée."""
        self.carte.add(self.pizza_mock)
        self.carte.remove("MockPizza")
        self.assertTrue(self.carte.is_empty())

    def test_suppression_boisson_mock(self):
        """Test la suppression d'une boisson mockée."""
        self.carte.add(self.boisson_mock)
        self.carte.remove("MockDrink")
        self.assertTrue(self.carte.is_empty())

    def test_suppression_dessert_mock(self):
        """Test la suppression d'un dessert mocké."""
        self.carte.add(self.dessert_mock)
        self.carte.remove("MockDessert")
        self.assertTrue(self.carte.is_empty())

    def test_suppression_pizza_mock_inexistante(self):
        """Test la suppression d'une pizza qui n'existe pas (mock)."""
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove("PizzaFantôme")


if __name__ == "__main__":
    unittest.main()
