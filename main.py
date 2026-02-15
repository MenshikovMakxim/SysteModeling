from core import Lab1
from views import Histogram

if __name__ == '__main__':
    # m = input("Номер лабораторної, або '0' для виходу: ")
    # while True:
    #
    a : int = int(pow(5, 13))
    c : int = int(pow(2, 31))
    quantity : int = 10000
    lab1 = Lab1(a, c, quantity)
    data = lab1.count(10)
    hist = Histogram(data, 20, lab1)
    hist.render()