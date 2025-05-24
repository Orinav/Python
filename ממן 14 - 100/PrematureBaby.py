from Baby import Baby

class PrematureBaby(Baby):
    """
     This class represents Baby object

    Author: Ori Nave
    Version: 20/01/2025
    """

    # Class constants
    MIN_PREMATURE_AGE = 0
    MAX_PREMATURE_AGE = 36

    def __init__(self, f_name, l_name, id_num, day, month, year, birth_weight_in_grams, birth_age):
        """
        Description - PrematureBaby constructor.

        Parameters:
        f_name - String.
        l_name - String.
        id_num - String.
        day - Integer between 1 and 31.
        month - Integer between 1 and 12.
        year - Integer between 1000 and 10000.
        birth_weight_in_grams - Positive Integer.
        birth_age - Positive Integer(represents weeks).
        """
        super().__init__(f_name, l_name, id_num, day, month, year, birth_weight_in_grams)
        self.__birth_age = birth_age

    def __str__(self):
        """
        Description - A string representation of Baby object.
        """
        return (
                super().__str__() +
                f"Birth Age: {self.__birth_age}"
        )

    def __eq__(self, other):
        """
        Description - Equality operator.
        """
        return super().__eq__(other) and self.__birth_age == other.__birth_age

    def get_birth_age(self):
        """
        Description - return the birth age.
        """
        return self.__birth_age

    def set_birth_age(self, birth_age):
        """
        Description - sets the birth age of a premature baby.
        """
        if isinstance(birth_age, int):
            if PrematureBaby.MIN_PREMATURE_AGE <= birth_age <= PrematureBaby.MAX_PREMATURE_AGE:
                self.__birth_age = birth_age
            else:
                raise ValueError(f"birth_age of a premature baby must be between {PrematureBaby.MIN_PREMATURE_AGE} and {PrematureBaby.MIN_PREMATURE_AGE} weeks")
        else:
            raise TypeError("birth_age must be an Integer")