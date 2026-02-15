import matplotlib.pyplot as plt

class Histogram:

    def __init__(self, data, k, title):
        self.data = data
        self.k = k
        self.title = title
        self.fx = None

    def render(self):
        plt.bar(self.intervals(),
                self.count_ni(),
                width=self.count_h(),
                align='edge',
                edgecolor='black',
                color='lightblue'
        )
        plt.title(self.title)
        plt.xlabel('Интервалы')
        plt.ylabel('Частота')
        plt.show()


    def count_h(self) -> float | None:
        if self.data:
            return (max(self.data) - min(self.data)) / self.k
        return None


    def count_ni(self) -> list[int]:
        intervals = [0 for i in range(0, self.k)]
        m = min(self.data)
        h = self.count_h()
        for x in self.data:
            i = int((x-m) / h)
            if i >= self.k:
                i -= 1
            intervals[i] += 1
        return intervals

    def intervals(self) -> list[float]:
        h = self.count_h()
        intervals = []
        for i in range(0, self.k):
            intervals.append(i * h)
        return intervals