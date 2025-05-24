from Date import Date
from Weight import Weight

class Baby:
    """
    This class represents Baby object

    Author: Ori Nave
    Version: 20/01/2025
    """

    # Class constants
    ID_LENGTH = 9


    def __init__(self, f_name, l_name, id_num, day, month, year, birth_weight_in_grams):
        """
        Description - Baby constructor.

        Parameters:
        f_name - String.
        l_name - String.
        id_num - String.
        day - Integer between 1 and 31.
        month - Integer between 1 and 12.
        year - Integer between 1000 and 10000.
        birth_weight_in_grams - Positive Integer.
        """
        self.__first_name = f_name
        self.__last_name = l_name
        if len(id_num) != Baby.ID_LENGTH or not id_num.isdigit():
            self.__id_num = Baby.ID_LENGTH*"0"
        else:
            self.__id_num = id_num
        self.__date_of_birth = Date(day, month, year)
        self.__birth_weight = Weight(birth_weight_in_grams // Weight.GRAMS_IN_KILO, birth_weight_in_grams % Weight.GRAMS_IN_KILO)
        self.__current_weight = Weight(birth_weight_in_grams // Weight.GRAMS_IN_KILO, birth_weight_in_grams % Weight.GRAMS_IN_KILO)

    def get_first_name(self):
        """
        Description - returns first name.
        """
        return self.__first_name

    def get_last_name(self):
        """
        Description - returns last name.
        """
        return self.__last_name

    def get_id(self):
        """
        Description - returns id number.
        """
        return self.__id_num

    def get_date_of_birth(self):
        """
        Description - returns date of birth.
        """
        return self.__date_of_birth

    def get_birth_weight(self):
        """
        Description - returns birth weight.
        """
        return self.__birth_weight

    def get_current_weight(self):
        """
        Description - returns current weight.
        """
        return self.__current_weight

    def set_current_weight(self, weight_to_set):
        """
        Description - sets current weight to a new weight.

        Parameters:
        weight_to_set - Weight object.
        """
        if isinstance(weight_to_set, Weight):
            self.__current_weight = Weight(weight_to_set.get_kilos(), weight_to_set.get_grams())
        else:
            raise TypeError("weight_to_set parameter should be an instance of Weight class.")

    def __str__(self):
        """
        Description - A string representation of Baby object.
        """
        return (
        f"Name: {self.__first_name} {self.__last_name}\n"
        f"Id: {self.__id_num}\n"
        f"Date of Birth: {self.__date_of_birth}\n"
        f"Birth Weight: {self.__birth_weight}\n"
        f"Current Weight: {self.__current_weight}\n"
        )

    def __eq__(self, other):
        """
        Description - checks if two babies are the same.

        Parameters:
        other - Baby object.

        Output:
        True if the babies are the same, False otherwise.
        """
        return (self.__first_name == other.__first_name and self.__last_name == other.__last_name and
        self.__date_of_birth == other.__date_of_birth and self.__id_num == other.__id_num)

    def are_twins(self, other):
        """
        Description - checks if two babies are twins.

        Parameters:
        other - Baby object.

        Output:
        True if the babies are twins, False otherwise.
        """
        return (self.__first_name != other.__first_name and self.__last_name == other.__last_name and
            self.__id_num != other.__id_num and self.__date_of_birth.difference(other.__date_of_birth) <= 1)

    def __gt__(self, other):
        """
        Description - checks if the baby current weight is greater than the other baby current weight.

        Parameters:
        other - Baby object.

        Output:
        True if the baby current weight is greater than the other baby current weight, False otherwise.
        """
        if isinstance(other, Baby):
            return self.__current_weight.__gt__(other.__current_weight)
        else:
            return NotImplemented

    def update_current_weight(self, grams):
        """
        Description - updates the current weight of a baby.

        Parameters:
        grams - Integer.

        Output:
        The updated current weight of a baby.
        """
        return self.__current_weight.add(grams)

    def older(self, other):
        """
        Description - checks if the baby is older than the other baby.

        Parameters:
        other - Baby object.

        Output:
        True if the baby is older than the other baby, False otherwise.
        """
        if isinstance(other, Baby):
            return self.__date_of_birth.__lt__(other.__date_of_birth)
        else:
            return NotImplemented