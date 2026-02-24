from math import sqrt, pow

class MathStat:

    @staticmethod
    def average(data_list : list[float]) -> float:
        return sum(data_list) / len(data_list)

    @staticmethod
    def dispersion(data_list : list[float]) -> float:
        avg = MathStat.average(data_list)
        return sum([pow((x - avg), 2) for x in data_list]) / len(data_list) ## add -1 for sample dispersion

    @staticmethod
    def standard_deviation(xi : list[float]) -> float:
        return sqrt(MathStat.dispersion(xi))

    @staticmethod
    def statistic(data_list : list[float]) -> dict[str, float]:
        return {
            'average': MathStat.average(data_list),
            'dispersion': MathStat.dispersion(data_list),
        }

    @staticmethod
    def uniform_distribution(data, k) -> float:
        '''критичне значення для рівномірного розподілу: 30.144'''
        return len(data) / k


    @staticmethod
    def count_x2(observation : list, expectation : list | float) -> float:
        x2 = 0
        if isinstance(expectation, float):
            for i in range(len(observation)):
                x2 += pow((observation[i] - expectation), 2) / expectation
        else:
            for i in range(len(observation)):
                x2 += pow((observation[i] - expectation[i]), 2) / expectation[i]
        return x2

    @staticmethod
    def check_crit(value : float, dist : str) -> bool:
        table_x2 = {
            'uniform': 30.144
        }

        if table_x2[dist] > value:
            return True
        else:
            return False

    @staticmethod
    def multiply_matrices(a : list[list[float]], b : list[list[float]]) -> list[list[float]]:
        result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result

    @staticmethod
    def transpose(m : list[list[float]] | list[float]) -> list[list[float]]:
        transposed = []
        for i in range(len(m[0])):
            row = []
            for j in range(len(m)):
                row.append(m[j][i])
            transposed.append(row)
        return transposed

    @staticmethod
    def invert_matrix(m: list[list[float]]) -> list[list[float]]:
        n = len(m)
        # Скептична перевірка: чи матриця квадратна? (X^T * X завжди квадратна, але про всяк випадок)
        if n != len(m[0]):
            raise ValueError("Обертати можна лише квадратні матриці!")

        # Створюємо розширену матрицю [M | E], де E - одинична матриця
        am = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(m)]

        # Прямий і зворотний хід Гауса-Жордана
        for fd in range(n):
            if am[fd][fd] == 0:
                raise ValueError("Матриця вироджена (детермінант = 0), оберненої не існує. Твої дані зламані!")

            fd_scaler = 1.0 / am[fd][fd]
            for j in range(2 * n):
                am[fd][j] *= fd_scaler

            for i in range(n):
                if i != fd:
                    cr_scaler = am[i][fd]
                    for j in range(2 * n):
                        am[i][j] -= cr_scaler * am[fd][j]

        # Відрізаємо і повертаємо праву частину (там тепер наша обернена матриця)
        return [row[n:] for row in am]