from math import sqrt, pow
from scipy.stats import f, t


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
    def get_f_critical(n: int, m: int, alpha: float = 0.05) -> float:
        k1 = m
        k2 = n - m - 1
        f_crit = f.ppf(1 - alpha, k1, k2)
        return f_crit

    @staticmethod
    def get_t_critical(n: int, m: int, alpha: float = 0.05) -> float:
        df = n - m - 1
        t_crit = t.ppf(1 - alpha, df)
        return t_crit
