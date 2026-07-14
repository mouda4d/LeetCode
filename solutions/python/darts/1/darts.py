"""
    Module that offers a function that decides whether the coordinates specified lie inside a radius of 10 circle (darts)
"""

import math # to use sqrt function

def score(x, y):
    """
        Function that takes coordinate x and y  and calculates the hyp (like a right angled triangle) to figure out if they lie inside a 10 radius circle

        Parameters:
            x (float): coordinate X.
            y (float): coordinate Y.

        Returns:
            Score of (1, 5, 10, 0) for a darts game.
    """

    z = math.sqrt(x**2 + y**2)    
    if z <= 1:
        return 10
    if z <= 5:
        return 5
    if z <= 10:
        return 1
    return 0
