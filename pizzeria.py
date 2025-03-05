class CartePizzeriaException(Exception):
    """Exception levée lorsqu'une erreur liée à la carte des pizzas survient."""
    pass

class Pizza:
    def __init__(self, nom, ingredients, prix):
        """
        Initialise une pizza avec un nom, une liste d'ingrédients et un prix.

        :param nom: Nom de la pizza (str)
        :param ingredients: Liste des ingrédients (list[str])
        :param prix: Prix de la pizza (float)
        """
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix

    def __str__(self):
        """Retourne une représentation textuelle de la pizza."""
        return f"{self.nom} - {', '.join(self.ingredients)} : {self.prix}€"


class CartePizzeria:
    def __init__(self):
        """
        Initialise une carte de pizzeria vide.
        """
        self.pizzas = []

    def is_empty(self):
        """
        Vérifie si la carte est vide.

        :return: True si la carte ne contient aucune pizza, False sinon.
        """
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        """
        Retourne le nombre de pizzas disponibles dans la carte.

        :return: Nombre d'éléments dans la carte (int).
        """
        return len(self.pizzas)

    def add_pizza(self, pizza):
        """
        Ajoute une pizza à la carte.

        :param pizza: Une instance de Pizza à ajouter.
        """
        if not isinstance(pizza, Pizza):
            raise TypeError("L'objet ajouté doit être une instance de Pizza.")
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        """
        Retire une pizza de la carte par son nom.

        :param name: Nom de la pizza à retirer (str).
        :raises CartePizzeriaException: Si la pizza n'existe pas dans la carte.
        """
        for pizza in self.pizzas:
            if pizza.nom == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException(f"Pizza '{name}' non trouvée.")

    def __str__(self):
        """
        Retourne une représentation de la carte avec toutes les pizzas listées.

        :return: Description des pizzas sous forme de chaîne de caractères.
        """
        if self.is_empty():
            return "La carte de la pizzeria est vide."
        return "\n".join(str(pizza) for pizza in self.pizzas)
