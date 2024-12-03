class Recipe():
    """
    A class used to represent a Recipe

    Attributes
    ----------
    name : str
        the name of the Recipe
    ingredients : list
        the list of Ingredients that make up the Recipe
    quantity : float
        the current quantity of this Recipe in unit
    desired_quantity : float
        the desired quantity of this Recipe to have in stock in unit
    unit : str
        the unit of storage used for this Recipe

    Methods
    -------
    remove_ingredient(ingredients)
        removes Ingredient from ingredients list
    add_ingredient(ingredients)
        adds Ingredient to the ingredients list
    remove(quantity)
        removes n from quantity
    add(quantity)
        add n to quantity
    edit_desired(desired_quantity)
        changes desired quantity to n
    need_to_make(quantity, desired_quantity)
        returns wether the recipe needs to be made to meet the desired quantity
    """

    def __init__(self, name=None, ingredients=[], quantity=0, desired_quantity=0, unit=None):
        """
        Parameters
        ----------
        name : str
            the name of the Recipe
        ingredients : list
            the list of Ingredients that make up the Recipe
        quantity : float
            the current quantity of this Recipe in unit
        desired_quantity : float
            the desired quantity of this Recipe to have in stock in unit
        unit : str
            the unit of storage used for this Recipe
        """

        self.name = name
        self.ingredients.append(ingredients)
        self.quantity = quantity
        self.desired_quantity = desired_quantity
        self.unit = unit

    @property
    def ingredients(self):
        return self._ingredients
    
    @ingredients.setter
    def ingredients(self, ingredients)
        self._ingredients = ingredients

    @property
    def desired_quantity(self):
        return self._desired_quantity
    
    @desired_quantity.setter
    def desired_quantity(self, desired_quantity):
        self._desired_quantity = desired_quantity

class Ingredient():
    """
    A class used to represent an Ingredient

    Attributes
    ----------
    name : str
        the name of the Ingredient
    quantity : float
        the current quantity of this Ingredient in unit
    unit : str
        the unit of storage used for this Ingredient 

    Methods
    -------
    remove(quantity)
        removes n from quantity
    add(quantity)
        add n to quantity
    """
    
    def __init__(self, name=None, quantity=0, unit=None):
        """Ingredient Initialisation Function

        Parameters
        ----------
        name : str
            the name of the Ingredient, by default None
        quantity : float
            the quantity of the Ingredient, by default 0
        unit : str
            the unit of the Ingredient, by default None
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit


    def remove(self, amount):
        """Remove amount from this Ingredient

        Parameters
        ----------
        amount : float
            a positive float to remove from this Ingredient's quantity

        Raises
        ------
        ValueError
            if trying to remove more Ingredients than exist
        ValueError
            if trying to remove a negative amount
        """
        if (self.quantity - amount) < 0:
            raise ValueError(f'Not enough {self.name} to remove {amount}')
        elif amount < 0:
                raise ValueError('Amount to remove can not be negative')
        else:
            self.quantity -= amount 


    def add(self, amount):
        """Add amount to this Ingredient's quantity

        Parameters
        ----------
        amount : float
            a positive float to add to this Ingredient's quantity

        Raises
        ------
        ValueError
            if amount is a negative number
        """
        if amount < 0:
            raise ValueError('Amount to add can not be negative')
        else:
            self.quantity += amount  