"""
Fibanacci implementation using recursive method.
"""


class BruteForceFibonacci(object):
    """
    In this RecursiveFibonacci class, we realized recursive implementation.
    """

    def __init__(self):
        """
        __init__ method can be called as constructor on other languages. Interpretator called when you create an
        instance.
        """
        self.cache = {}

    def get_number(self, n):
        """
        Returns n-th number of fibonacci numbers.

        :param n: n-th number of fibonacci numbers
        :rtype: int
        :return: fibonacci number

        Recursion means calling functions directly from itself.
        """

        if n < 0:
            raise TypeError('please enter positive numbers')

        if n in self.cache:
            ans = self.cache[n]
        elif n <= 2:
            ans = 1
            self.cache[n] = ans
        else:
            ans = self.get_number(n - 2) + self.get_number(n - 1)
            self.cache[n] = ans

        return ans