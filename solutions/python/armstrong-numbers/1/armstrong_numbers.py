def is_armstrong_number(number):
    summate_digits = 0
    string_number = str(number)
    for digit in string_number:
        summate_digits += int(digit) ** len(string_number)
    return number == summate_digits