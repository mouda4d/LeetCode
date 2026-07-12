def steps(number):
    if number > 0:
        step = 0
        # we want to divide by two whenever its even and multiply by three then add one whenever it is odd.
        # so for example the number 50 is even, 50 25 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
        # okay so the loop will be going over mutating the number asking is it odd or even then continuing the loop and breaking at one
        while number > 1:       
            if number % 2 == 0: 
                number /= 2
                step += 1
            else:
                number = number * 3 + 1
                step += 1
        return step
    raise ValueError("Only positive integers are allowed")