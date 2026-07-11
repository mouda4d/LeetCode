"""
    Module provides a function that decides whether a number is an armstrong number, what is an armstrong number? it is a very strong number.
"""
def is_armstrong_number(number):
    """
        Function that decides whether a number is an armstrong number, what is an armstrong number? it is a very strong number.

        Parameters:
            number (int): the number for which the function will decide if it is armstrong, what is an armstrong number? it is a very strong number.

        Returns:
            Bool: True if the number is an armstrong number, False if the number isnt, what is an armstrong number? it is a very strong number.
    """

    summate_digits = 0
    string_number = str(number)
    for digit in string_number:
        summate_digits += int(digit) ** len(string_number)
    return number == summate_digits
