#!/usr/bin/python3
"""script to calculate minimum operation
"""


def minOperations(n):
    """ this method can calculates the fewest number of ops """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
