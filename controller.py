from core import Lab1, MathStat
from views import Histogram
from random import randint

class CLab1:

    def __init__(self, a : int, c : int, quantity : int, seed : int) -> None:
        self.seed = seed
        self.lab = Lab1(a, c, quantity)


    def make_histogram(self, k : int = 20) -> None:
        data = self.lab.count(self.seed)
        hist = Histogram(data, k, self.lab)
        hist.render_with_info(CLab1.info(hist))


    def get_info(self) -> dict[str, float]:
        return self.lab.get_stats()


    def make_count(self) -> list[float]:
        return self.lab.count(self.seed)


    @staticmethod
    def generate_random_data(quantity, seed) -> tuple[list[float], str]:
        """Випадкові дані для тестування"""
        rand_c = randint(1000, pow(2, 31))
        rand_a = randint(1, rand_c - 1)
        info = f"Random data (a={rand_a}, c={rand_c})"
        rdata = CLab1(rand_a, rand_c, quantity, seed)
        return rdata.make_count(), info


    @staticmethod
    def make_3random_histograms(quantity, seed, k=20):
        histograms = []

        for i in range(3):
            data, info = CLab1.generate_random_data(quantity, seed)
            hist = Histogram(data, k, f"Histogram: {i+1}, {info}")
            histograms.append(hist)
            print("\n" + "-"*20 + f"Histogram: {i+1}, {info}" + "-"*20 + "\n")
            print(CLab1.info(hist))


        Histogram.sub_histogram(histograms)

    @staticmethod
    def info(hist : Histogram):
        dist = MathStat.uniform_distribution(hist.data, hist.k)
        x2 = MathStat.count_x2(hist.count_ni(), dist)
        data_info = MathStat.statistic(hist.data)
        x2_valid = MathStat.check_crit(x2, 'uniform')
        validity : str
        if x2_valid:
            validity = "відповідає рівномірному розподілу"
        else:
            validity = "не відповідає рівномірному розподілу"

        stats_text = (
            f"Кількість (N): {len(hist.data)}\n"
            f"Середнє (μ): {data_info['average']:.4f}\n"  # Очікується ~0.5
            f"Дисперсія (σ²): {data_info['dispersion']:.4f}\n"  # Очікується ~0.0833
            f"Інтервалів (K): {hist.k}\n"
            f"Критерій згоди (Xi²): {x2}\n"
            f"Результат перевірки: {validity}\n"
            f"Критичне значення для рівномірного розподілу: 30.144"
        )

        return stats_text