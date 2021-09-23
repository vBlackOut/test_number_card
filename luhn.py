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

        #print("total", total_chiffre)

        print(total_chiffre, total_chiffre%10)

        if total_chiffre % 10:
            return False
        else:
            return True

        #return True
