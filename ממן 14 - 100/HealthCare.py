from Weight import Weight
from Baby import Baby

class HealthCare:
    """
    This class represents HealthCare object

    Author: Ori Nave
    Version: 20/01/2025
    """

    def __init__(self, branch_name):
        self.__name = branch_name
        self.__babies = []

    def get_name(self):
        """
        Description - returns the name of the branch.
        """
        return self.__name

    def num_of_babies(self):
        """
        Description - returns the number of babies in the branch.
        """
        return len(self.__babies)

    def add_baby(self, baby):
        """
        Description - adds a baby to the branch in correlation to its birth date(sorted in ascending order).

        Parameters:
        baby - Baby object.
        """
        for i in range(len(self.__babies)):
            if baby.older(self.__babies[i]):
                self.__babies.insert(i, baby)
                return
        self.__babies.append(baby)

    def how_many_above_weight(self, weight):
        """
        Description - returns the number of babies that above a certain weight.

        Parameters:
        weight - Weight object.

        Output:
        The number of babies that above weight.
        """
        count = 0
        for baby in self.__babies:
            if baby.get_current_weight().__gt__(weight):
                count += 1
        return count

    def average_weight(self):
        """
        Description - returns the average weight of all the babies in the branch.
        """
        if self.num_of_babies() == 0:
            return None

        sum = 0
        for baby in self.__babies:
            sum += baby.get_current_weight().get_kilos()*Weight.GRAMS_IN_KILO + baby.get_current_weight().get_grams()

        result = sum / self.num_of_babies()
        return Weight(int(result//Weight.GRAMS_IN_KILO), int(result%Weight.GRAMS_IN_KILO))

    def most_heaviest_baby(self):
        """
        Description - returns the heaviest baby in the branch.
        """
        if self.num_of_babies() == 0:
            return None

        heaviest_index = 0
        max = self.__babies[0].get_current_weight().get_kilos()*Weight.GRAMS_IN_KILO + self.__babies[0].get_current_weight().get_grams()

        for i in range(len(self.__babies)):
            if max < self.__babies[i].get_current_weight().get_kilos()*Weight.GRAMS_IN_KILO + self.__babies[i].get_current_weight().get_grams():
                max = self.__babies[i].get_current_weight().get_kilos()*Weight.GRAMS_IN_KILO + self.__babies[i].get_current_weight().get_grams()
                heaviest_index = i

        return Baby(self.__babies[heaviest_index].get_first_name(), self.__babies[heaviest_index].get_last_name(), self.__babies[heaviest_index].get_id(),
                    self.__babies[heaviest_index].get_date_of_birth().get_day(),  self.__babies[heaviest_index].get_date_of_birth().get_month(), self.__babies[heaviest_index].get_date_of_birth().get_year(),
                    self.__babies[heaviest_index].get_current_weight().get_kilos()*Weight.GRAMS_IN_KILO + self.__babies[heaviest_index].get_current_weight().get_grams())

    def babies_above_weight(self, weight):
        """
        Description - returns a list with all the babies that their current weight is greater than a certain weight.

        Parameters:
        weight - Weight object.

        Output:
        A list with all the babies that their current weight is greater than a certain weight.
        """
        if isinstance(weight, Weight):
            above_list = []
            for i in range(len(self.__babies)):
                if self.__babies[i].get_current_weight().__gt__(weight):
                    above_list.append(Baby(self.__babies[i].get_first_name(), self.__babies[i].get_last_name(), self.__babies[i].get_id(),
                    self.__babies[i].get_date_of_birth().get_day(),  self.__babies[i].get_date_of_birth().get_month(), self.__babies[i].get_date_of_birth().get_year(),
                    self.__babies[i].get_current_weight().get_kilos()*Weight.GRAMS_IN_KILO + self.__babies[i].get_current_weight().get_grams()))

        return above_list

    def __str__(self):
        """
        Description - returns the string representation of HealthCare object.
        """
        if self.num_of_babies() == 0:
            return "There are no babies in this Health Care branch."

        result = f"Branch {self.__name} has {self.num_of_babies()} babies: \n"

        for baby in self.__babies:
            result += (
                f"Name: {baby.get_first_name()} {baby.get_last_name()} \n"
                f"Id: {baby.get_id()} \n"
                f"Date Of Birth: {baby.get_date_of_birth()} \n"
                f"Birth Weight: {baby.get_birth_weight()} \n"
                f"Current Weight: {baby.get_current_weight()} \n"
                f"\n"
        )

        return result