class LuhnFormula():
    """
    Luhn formula implementation
    """

    def __init__(self, input: str) -> None:
        """
        Constructor
        """
        self.input = input

    def is_valid(self) -> bool:
        """
        Check if the input string is valid
        """
        total_chiffre = 0

        for i, value in enumerate(self.input[::-1]):

            if i % 2 == True:
                if int(value)*2 >= 10:
                    somme_chiffre = 0
                    for i in str(int(value)*2):
                        somme_chiffre += int(i)
                    total_chiffre += somme_chiffre
                else:
                    total_chiffre += int(value)*2

            else:
                total_chiffre += int(value)

        if (total_chiffre % 10):
            return False
        else:
            return True


    def is_bonus_valid(self) -> bool:

        total_chiffre = 0

        for i, value in enumerate(self.input[::-1]):

            if i % 2 == True:
                if int(value)*2 >= 10:
                    somme_chiffre = 0
                    for i in str(int(value)*2):
                        somme_chiffre += int(i)
                    total_chiffre += somme_chiffre
                else:
                    total_chiffre += int(value)*2

            else:
                total_chiffre += int(value)

        if total_chiffre%10 != 0:

            # calculate the best number for the last number missing
            self.input = self.input + str((total_chiffre%10)+1)

            for i, value in enumerate(self.input[::-1]):

                if i % 2 == True:
                    if int(value)*2 >= 10:
                        somme_chiffre = 0
                        for i in str(int(value)*2):
                            somme_chiffre += int(i)
                        total_chiffre += somme_chiffre
                    else:
                        total_chiffre += int(value)*2

                else:
                    total_chiffre += int(value)

        # best check if number divise by ten
        if (total_chiffre % 10) % 2:
            return False
        else:
            return True
