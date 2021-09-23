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

        print(self.input[::-1])
        total_chiffre = 0

        for i, value in enumerate(self.input[::-1]):

            if i % 2 == True:
                if int(value)*2 >= 10:
                    #print("somme chiffre", int(value), int(value))
                    somme_chiffre = 0
                    for i in str(int(value)*2):
                        somme_chiffre += int(i)
                    print("somme chiffre", int(value), int(value)*2, somme_chiffre)
                    total_chiffre += somme_chiffre
                else:
                    print("double normal", int(value), int(value)*2)
                    total_chiffre += int(value)*2

            else:
                total_chiffre += int(value)

        #print("total", total_chiffre)

        print(total_chiffre, total_chiffre%10)

        if total_chiffre % 10:
            print("not ten modulo")
            return False
        else:
            return True

        #return True
