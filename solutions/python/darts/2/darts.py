"""
    Module that offers a function that decides whether the coordinates specified lie inside a radius of 10 circle (darts)
"""

import math # to use sqrt function

def score(coord_x, coord_y):
    """
        Function that takes coordinate x and y  and calculates the hyp (like a right angled triangle) to figure out if they lie inside a 10 radius circle

        Parameters:
            coord_x (float): coordinate X.
            coord_y (float): coordinate Y.

        Returns:
            Score of (1, 5, 10, 0) for a darts game.
    """

    coord_z = math.sqrt(coord_x**2 + coord_y**2)    
    if coord_z <= 1:
        return 10
    if coord_z <= 5:
        return 5
    if coord_z <= 10:
        return 1
    return 0
