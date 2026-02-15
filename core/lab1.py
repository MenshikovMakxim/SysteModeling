import math
from .math_stat import MathStat

class Lab1:

    def __init__(self, a: int, c: int, quantity: int) -> None:
        self.quantity = quantity
        self.a = a
        self.c = c
        self.xi = []


    def count(self, q : int) -> list[float]:
        self._rand(q)
        return self.xi


    def _rand(self, rn : int = 1) -> None:
        z0 = rn
        for i in range(0, self.quantity):
            z = (self.a * z0) % self.c
            z0 = z
            self.xi.append(z / self.c)


    def __str__(self) -> str:
        return "Lab1(a={}, c={}, quantity={})".format(self.a, self.c, self.quantity)


    def clear(self) -> None:
        self.xi = []


    def get_data(self) -> list[float]:
        return self.xi






