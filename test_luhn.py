from luhn import LuhnFormula


def test_input_is_valid():
    """
    Test string input is valid
    """

    luhn_formula = LuhnFormula("543215")
    assert luhn_formula.is_valid()

    luhn_formula_2 = LuhnFormula("972487086")
    assert luhn_formula_2.is_valid()

    print("success test 1")


def test_input_is_not_valid():
    """
    Test string input is not valid
    """

    luhn_formula_2 = LuhnFormula("927487086")
    assert not luhn_formula_2.is_valid()
    print("success test 2")

def test_input_bonus():

    luhn_formula_2 = LuhnFormula("012346")
    assert luhn_formula_2.is_bonus_valid()

    luhn_formula_2 = LuhnFormula("54321")
    assert luhn_formula_2.is_bonus_valid()

    print("success test 3")


test_input_is_valid()
test_input_is_not_valid()
test_input_bonus()
