# -*- coding: utf-8 -*-
"""
Updated Mar 14, 2025
Fixed bugs in classifyTriangle function

@author: James
"""

def classifyTriangle(a, b, c):
    """
    Classifies a triangle based on the given side lengths.

    Returns:
        'Equilateral'  -> if all three sides are equal
        'Isosceles'    -> if exactly two sides are equal
        'Scalene'      -> if no sides are equal
        'Right'        -> if it satisfies the Pythagorean theorem
        'NotATriangle' -> if it does not satisfy the triangle inequality
        'InvalidInput' -> if inputs are not valid positive integers within range 0-200
    """

    # Step 1: Validate input
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    
    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Step 2: Check if it's a valid triangle (Triangle Inequality Theorem)
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'

    # Step 3: Check for Equilateral Triangle
    if a == b == c:
        return 'Equilateral'

    # Step 4: Check for Right Triangle (Pythagorean Theorem)
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 'Right'

    # Step 5: Check for Isosceles Triangle
    if a == b or b == c or a == c:
        return 'Isosceles'

    # Step 6: If none of the above, it's a Scalene Triangle
    return 'Scalene'
