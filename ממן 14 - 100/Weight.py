class Weight:
    """
    This class represents Weight object

    Author: Ori Nave
    Version: 20/01/2025
    """

    # Class constants
    DEFAULT_KILOS = 1
    DEFAULT_GRAMS = 0

    MIN_KILOS = 1
    MIN_GRAMS = 0
    MAX_GRAMS = 999

    GRAMS_IN_KILO = 1000

    def __init__(self, kilos = DEFAULT_KILOS, grams = DEFAULT_GRAMS):
        """
        Description - Weight constructor.

        Parameters:
        kilos - Positive integer.
        grams - Integer in range 0-999.
        """
        if type(kilos) == int and kilos >= Weight.MIN_KILOS and type(grams) == int and Weight.MIN_GRAMS <= grams <= Weight.MAX_GRAMS:
            self.__kilos = kilos
            self.__grams = grams
        else:
            self.__kilos = Weight.DEFAULT_KILOS
            self.__grams = Weight.DEFAULT_GRAMS

    def get_kilos(self):
        """
        Description - returns kilos.
        """
        return self.__kilos

    def get_grams(self):
        """
        Description - returns grams.
        """
        return self.__grams

    def __eq__(self,other):
        """
        Description - checks if two weights are equal.

        Parameters:
        other - Weight object.

        Output:
        True if the weights are equal, False otherwise.
        """
        if isinstance(other, Weight):
            return self.__kilos == other.__kilos and self.__grams == other.__grams
        else:
            return NotImplemented

    def __lt__(self, other):
        """
        Descriptions - checks if the weight is less than the other weight.

        Parameters:
        other - Weight object.

        Output:
        True if the weight is less than the other weight, False otherwise.
        """
        if isinstance(other, Weight):
            if self.__kilos < other.__kilos:
                return True
            elif self.__kilos > other.__kilos:
                return False
            else:
                if self.__grams < other.__grams:
                    return True
                else:
                    return False
        else:
            return NotImplemented

    def __gt__(self, other):
        """
        Descriptions - checks if the weight is greater than the other weight.

        Parameters:
        other - Weight object.

        Output:
        True if the weight is greater than the other weight, False otherwise.
        """
        return not self.__lt__(other)

    def __str__(self):
        """
        Description - A string representation of Weight object.
        """
        if self.__grams == Weight.MIN_GRAMS:
            return f"{self.__kilos}.0"

        str_grams = str(self.__grams)

        if len(str_grams) == 1:
            return f"{self.__kilos}.00{str_grams}"
        elif len(str_grams) == 2:
            if self.__grams%10 == 0:
                return f"{self.__kilos}.0{self.__grams//10}"
            else:
                return f"{self.__kilos}.0{self.__grams}"
        elif len(str_grams) == 3:
            if self.__grams%10 == 0:
                if self.__grams%100 == 0:
                    return f"{self.__kilos}.{self.__grams//100}"
                return f"{self.__kilos}.{self.__grams // 10}"
            else:
                return f"{self.__kilos}.{self.__grams}"

    def add(self, grams):
        """
        Description - adds grams to a Weight object.

        Parameters:
        grams - Integer
        """
        if type(grams) != int:
            return NotImplemented

        if grams > 0:
            if self.__grams + grams > Weight.MAX_GRAMS:
                self.__kilos += (self.__grams + grams) // Weight.GRAMS_IN_KILO
                self.__grams = (self.__grams + grams) % Weight.GRAMS_IN_KILO
            else:
                self.__grams += grams

        elif grams < 0:
            if self.__grams + grams < 0:
                if (Weight.GRAMS_IN_KILO*self.__kilos + self.__grams + grams)//Weight.GRAMS_IN_KILO >= Weight.DEFAULT_KILOS:
                    self.__kilos += (self.__grams + grams) // Weight.GRAMS_IN_KILO
                    self.__grams = (self.__grams + grams) % Weight.GRAMS_IN_KILO
            else:
                self.__grams += grams