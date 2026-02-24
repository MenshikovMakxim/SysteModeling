import numpy as np
from math import sqrt

class Lab3:
    def __init__(self, x : np.ndarray, y : np.ndarray = None, n : int = 1) -> None:
        self.n = n
        self.x : np.ndarray = x #x.flatten()
        self.y : np.ndarray = y.flatten() if y is not None else None

    def make_matrix(self) -> np.ndarray:
        """
        Генерує матрицю X для функції y = b0 + b1(1/x) + b2(1/x^2) + ... + bn(1/x^n)
        """
        # 1. Стовпець одиниць
        ones_col = np.ones((len(self.x), 1))

        # Складаємо всі стовпці у список, починаючи з одиниць
        columns = [ones_col]

        # 2. У циклі генеруємо 1/x^1, 1/x^2 ... 1/x^n
        for i in range(1, self.n + 1):
            # Ділимо 1 на x у відповідному степені і робимо з цього вертикальний стовпець
            col = (1 / (self.x ** i)).reshape(-1, 1)
            columns.append(col)

        # 3. Склеюємо всі згенеровані стовпці зліва направо
        matrix = np.hstack(columns)
        return matrix

    def calculate_criterion(self) -> float:
        X = self.make_matrix()
        b = self.count_b()
        Y_pred = X @ b
        F_b = np.sum((Y_pred - self.y) ** 2)
        return F_b

    def Y_reg(self):
        X = self.make_matrix()
        b = self.count_b()
        Y_pred = X @ b
        return Y_pred

    def Y_reg_sub_Y(self):
        Y_pred = self.Y_reg()
        return abs(Y_pred - self.y)

    def Y_reg_sub_Y_squared(self):
        return (self.Y_reg_sub_Y() ** 2)


    def make_vector(self) -> np.ndarray:
        return self.y


    def chek(self):
        print(len(self.x), len(self.y))

    def count_b(self) -> np.ndarray:
        X = self.make_matrix()
        Y = self.make_vector()
        result = np.linalg.inv(X.T @ X)
        b = result @ X.T @ Y
        return b

    def __str__(self):
        info_text = (
            "\n" + "-"*30 + "Information" + "-"*30 + "\n"
            f"X: {self.x}\n"
            f"Y: {self.y}\n"
            f"Matrix X:\n{self.make_matrix()}\n"
            f"Vector Y:{self.make_vector()}\n"
            f"Coefficients b:{self.count_b().round(3)}\n"
            f"Predicted Y (Y_reg): {self.Y_reg().round(1)}\n"
            f"Difference (Y_reg - Y): {self.Y_reg_sub_Y().round(1)}\n"
            f"Squared Difference ((Y_reg - Y)^2): {self.Y_reg_sub_Y_squared().round(2)}\n"
            f"Criterion F(b): {round(self.calculate_criterion(), 2)}\n"
            f"Correlation coefficient R: {self.corel_reg_anlysis()}\n"
        )

        return info_text

    def corel_reg_anlysis(self):
        _Y_reg = (np.sum(self.y)/len(self.y)).round(1)
        fact = np.sum((self.Y_reg() - _Y_reg) ** 2)/(len(self.y)-1)
        total = np.sum((self.y - _Y_reg) ** 2)/(len(self.y)-1)
        R = sqrt(fact/total)
        info = {
            "_Y_reg": round(float(_Y_reg), 1),
            "fact": round(float(fact),1),
            "total": round(float(total),1),
            "R": round(R, 3)
        }
        return info

    def function(self):
        bs = self.count_b()
        res = f"y = {bs[0].round(3)}"
        for i in range(1, self.n+1):
            res = res + " + " + str(bs[i].round(3)) + " * (1/(x^" + str(i) + "))"
        return res

    def test(self):
        print("Оцінка критерію F(b) для різних порядків апроксимації:")
        print("-" * 50)

        best_n = 1
        min_error = float('inf')

        # Перевіряємо порядки від 1 до 4
        for n in range(1, 5):
            self.n = n
            error = self.calculate_criterion()

            print(f"Порядок n={n} | Значення F(b) = {error:.4f}")
            print(self)

            # Шукаємо мінімум
            if error < min_error:
                min_error = error
                best_n = n

        print("-" * 50)
        print(f"Висновок: Найкраще підходить порядок n={best_n}, бо його похибка найменша!")


