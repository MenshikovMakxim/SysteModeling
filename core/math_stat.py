from math import sqrt, pow

class MathStat:

    @staticmethod
    def average(data_list : list[float]) -> float:
        return sum(data_list) / len(data_list)

    @staticmethod
    def dispersion(data_list : list[float]) -> float:
        avg = MathStat.average(data_list)
        return sum([pow((x - avg), 2) for x in data_list]) / len(data_list)

    @staticmethod
    def standard_deviation(xi : list[float]) -> float:
        return sqrt(MathStat.dispersion(xi))

    @staticmethod
    def statistic(data_list : list[float]) -> dict[str, float]:
        return {
            'average': MathStat.average(data_list),
            'dispersion': MathStat.dispersion(data_list),
            'standard_deviation': MathStat.standard_deviation(data_list)
        }