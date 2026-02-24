from core import CLab3
import numpy as np



if __name__ == '__main__':

    x = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5])
    y = np.array([14, 18.222, 18, 17.216, 16.444, 15.778, 15.219, 14.749, 14.352, 14.014, 13.722, 13.469, 13.248, 13.052, 12.879, 12.724])
    lab3 = CLab3(x, y, 3)
    lab3.Approximation()
    print(lab3)
    lab3.lab3.test()



