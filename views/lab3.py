from matplotlib import pyplot as plt
import numpy as np
from core import Lab3

class Lab3Approximation:
    def __init__(self, X, Y, n_order, b):
        self.X = X
        self.Y = Y
        self.n_order = n_order
        self.b = b

    def _calculate_smooth_curve(self):
        """Розраховує гладку криву апроксимації"""
        X_smooth = np.linspace(min(self.X), max(self.X), 100)
        lt_smooth = Lab3(X_smooth, None, self.n_order)
        X_smooth_mat = lt_smooth.make_matrix()
        Y_smooth = X_smooth_mat @ self.b
        return X_smooth, Y_smooth

    def plot(self):
        """Малює графік експериментальних даних, апроксимацію та текст поруч"""
        # 1. Робимо вікно ширшим (наприклад, 12 на 6 дюймів замість стандартного квадрата)
        plt.figure(figsize=(12, 6))

        # Малюємо реальні дані як червоні крапки
        plt.scatter(self.X, self.Y, color='red', label='Експериментальні дані', zorder=5)

        # Отримуємо розраховані значення
        X_smooth, Y_smooth = self._calculate_smooth_curve()

        # Малюємо ідеальну синю лінію
        plt.plot(X_smooth, Y_smooth, color='blue', linewidth=2, label=f'Апроксимація (порядок {self.n_order})')

        # Наводимо красу: сітка, підписи, легенда
        plt.title('Ідентифікація об\'єкта за експериментальними даними')
        plt.xlabel('X (вхідні дані)')
        plt.ylabel('Y (відгук)')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()

        # Виводимо графік на екран
        plt.savefig('lab3.png')
        plt.show()
#
# lb3c = Lab3(
#     x=np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5]),
#     y=np.array([14, 18.222, 18, 17.216, 16.444, 15.778, 15.219, 14.749,
#                 14.352, 14.014, 13.722, 13.469, 13.248, 13.052,
#                 12.879, 12.724])
# )
# b = lb3c.count_b(1)
#
# lb3 = Lab3Approximation(
#     X=lb3c.x,
#     Y=lb3c.y,
#     n_order=2,
#     b=b
# )
#
# lb3.plot()