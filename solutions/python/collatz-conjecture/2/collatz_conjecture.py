"""
    Module that offers a function that determines: Can every number find its way to 1? returning the number of steps taken to reach 1
"""
def steps(number):
    """
        function that determines: Can every number find its way to 1?

        Paramters:
            number (int): the number needed to determine for.

        Returns:
            step (int): the number of steps taken to reach 1
    """   
    
    if number > 0:
        step = 0
        while number > 1:       
            if number % 2 == 0: 
                number /= 2
                step += 1
            else:
                number = number * 3 + 1
                step += 1
        return step
    raise ValueError("Only positive integers are allowed")
