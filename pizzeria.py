class CartePizzeriaException(Exception):
    """Exception levée lorsqu'une erreur liée à la carte des pizzas survient."""
    pass


class Pizza:
    """Représente une pizza avec nom, prix, description, ingrédients et base (tomate ou crème)."""
    def __init__(self, nom, prix, description, ingredients, base):
        """
        Initialise une pizza.

        :param nom: Nom de la pizza (str)
        :param prix: Prix de la pizza (float)
        :param description: Brève description de la pizza (str)
        :param ingredients: Liste des ingrédients (list[str])
        :param base: Base de la pizza (str) ("tomate" ou "crème")
        """
        self.nom = nom
        self.prix = prix
        self.description = description
        self.ingredients = tuple(ingredients)  # Tuple pour éviter les modifications accidentelles
        self.base = base.lower()  # Convertir en minuscule pour uniformiser

    def __eq__(self, other):
        """Deux pizzas sont considérées identiques si elles ont les mêmes ingrédients et la même base."""
        return isinstance(other, Pizza) and self.ingredients == other.ingredients and self.base == other.base

    def __hash__(self):
        """Permet d'utiliser les pizzas dans un ensemble (évite les doublons)."""
        return hash((self.ingredients, self.base))

    def __str__(self):
        return f"{self.nom} ({self.base}) - {self.description} - {', '.join(self.ingredients)} : {self.prix}€"


class Boisson:
    """Représente une boisson avec nom, prix et présence d'alcool."""
    def __init__(self, nom, prix, alcool):
        """
        Initialise une boisson.

        :param nom: Nom de la boisson (str)
        :param prix: Prix de la boisson (float)
        :param alcool: Indique si la boisson contient de l'alcool (bool)
        """
        self.nom = nom
        self.prix = prix
        self.alcool = alcool  # Booléen (True = contient de l’alcool)

    def __eq__(self, other):
        """Deux boissons sont identiques si elles ont le même nom (insensible à la casse)."""
        return isinstance(other, Boisson) and self.nom.lower() == other.nom.lower()

    def __str__(self):
        return f"{self.nom} - {'Avec Alcool' if self.alcool else 'Sans Alcool'} : {self.prix}€"


class Dessert:
    """Représente un dessert avec nom, prix, ingrédients et indication 'fait maison'."""
    def __init__(self, nom, prix, ingredients, fait_maison):
        """
        Initialise un dessert.

        :param nom: Nom du dessert (str)
        :param prix: Prix du dessert (float)
        :param ingredients: Liste des ingrédients (list[str])
        :param fait_maison: Indique si le dessert est fait maison (bool)
        """
        self.nom = nom
        self.prix = prix
        self.ingredients = tuple(ingredients)
        self.fait_maison = fait_maison  # Booléen (True = fait maison)

    def __eq__(self, other):
        """Deux desserts sont identiques s'ils ont le même nom (insensible à la casse)."""
        return isinstance(other, Dessert) and self.nom.lower() == other.nom.lower()

    def __str__(self):
        return f"{self.nom} - {'Fait Maison' if self.fait_maison else 'Industriel'} : {self.prix}€"


class CartePizzeria:
    """Gère une carte de pizzeria contenant des pizzas, boissons et desserts."""
    def __init__(self):
        self.pizzas = set()  # Ensemble pour éviter les doublons
        self.boissons = set()
        self.desserts = set()

    def is_empty(self):
        """Retourne True si la carte est vide."""
        return not (self.pizzas or self.boissons or self.desserts)

    def nb_pizzas(self):
        """Retourne le nombre de pizzas dans la carte."""
        return len(self.pizzas)

    def nb_drinks(self):
        """Retourne le nombre de boissons dans la carte."""
        return len(self.boissons)

    def nb_desserts(self):
        """Retourne le nombre de desserts dans la carte."""
        return len(self.desserts)

    def add(self, element):
        """
        Ajoute un élément (pizza, boisson ou dessert) à la carte.

        :param element: Instance de Pizza, Boisson ou Dessert
        :raises CartePizzeriaException: Si l'élément existe déjà
        """
        if isinstance(element, Pizza):
            if element in self.pizzas:
                raise CartePizzeriaException(f"La pizza '{element.nom}' existe déjà avec ces ingrédients.")
            self.pizzas.add(element)

        elif isinstance(element, Boisson):
            if element in self.boissons:
                raise CartePizzeriaException(f"La boisson '{element.nom}' est déjà présente.")
            self.boissons.add(element)

        elif isinstance(element, Dessert):
            if element in self.desserts:
                raise CartePizzeriaException(f"Le dessert '{element.nom}' est déjà présent.")
            self.desserts.add(element)

        else:
            raise CartePizzeriaException("Type d'élément inconnu.")

    def remove(self, name):
        """
        Retire un élément de la carte par son nom.

        :param name: Nom de l'élément à retirer (str)
        :raises CartePizzeriaException: Si l'élément n'existe pas
        """
        for category in [self.pizzas, self.boissons, self.desserts]:
            for item in category:
                if item.nom.lower() == name.lower():
                    category.remove(item)
                    return
        raise CartePizzeriaException(f"L'élément '{name}' n'existe pas dans la carte.")

    def __str__(self):
        """Retourne une description de la carte avec tous les éléments listés."""
        items = []
        if self.pizzas:
            items.append("\n🍕 Pizzas :")
            items.extend(str(pizza) for pizza in self.pizzas)

        if self.boissons:
            items.append("\n🥤 Boissons :")
            items.extend(str(boisson) for boisson in self.boissons)

        if self.desserts:
            items.append("\n🍰 Desserts :")
            items.extend(str(dessert) for dessert in self.desserts)

        return "\n".join(items) if items else "La carte est vide."
