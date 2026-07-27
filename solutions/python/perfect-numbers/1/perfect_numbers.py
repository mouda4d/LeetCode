def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    pass
    # if the given is a number like 6: every number is divisible by 1 so we wont even check for it, lets check by iterates of 1: 6%2 = 0, 6%3=0, 6%4!=0, hmm so the divised
    # can't be greater than half of the divisor.
    # let us try 37: we try 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,,, 19*2 = 38 so we stop at 18
    # whoever succeeds is added to a sum and we check if the sum is equal to the number or less or equal.
    # can we lower the iterations?
    #1. if it is an odd number ignore all even attempts.
    #perabundef = ['perfect', 'abundant', 'deficient']
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')
    sum = 1
    if number == sum:
        return 'deficient'
    if number % 2 != 0: # odd number
        for i in range(3, number, 2): # 3, 5 ,7 ,9,
            if i < number / 2 : # i should be less than half of number
                if number % i == 0:
                    sum += i
    else:
        for i in range(2, number): # 2, 3, 4 ,5, 6 ,7, 8,
            if i <= number / 2 : # i should be less than or equal to half of number
                if number % i == 0:
                    sum += i

    if sum < number:
        return 'deficient'
    if sum == number:
        return 'perfect'
    if sum > number:
        return 'abundant'

    