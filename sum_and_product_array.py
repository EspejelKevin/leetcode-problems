"""

WAF to calculate sum & product of all numbers in an array.

Example 1:
input: [1, 2, 3, 4, 5]
output: sum = 15, product = 120

"""

import math

def sum_and_product(arr):
    return sum(arr), math.prod(arr)
