import matplotlib.pyplot as plt

class Histogram:

    def __init__(self, data, k, title):
        self.data = data
        self.k = k
        self.title = title
        self.fx = None

    @staticmethod
    def sub_histogram(histograms):
        count = len(histograms)
        fig, axes = plt.subplots(nrows=count, ncols=1, figsize=(10, 3 * count))

        # Якщо графік всього один, axes буде не списком, а об'єктом. Виправляємо це:
        if count == 1: axes = [axes]

        # 3. Проходимо циклом і малюємо кожен на своєму місці
        for i, hist_obj in enumerate(histograms):
            hist_obj.render(ax=axes[i])  # Передаємо конкретну область (ax)

        # Додаємо відступи, щоб заголовки не налізали один на одного
        plt.tight_layout()
        plt.show()


    def render_with_info(self, info_text):
        # 1. Створюємо "сітку": 1 рядок, 2 колонки.
        # width_ratios=[3, 1] -> Графік займає 3 частини ширини, текст - 1 частину.
        fig, (ax_plot, ax_text) = plt.subplots(1, 2, figsize=(12, 6),
                                               gridspec_kw={'width_ratios': [3, 1]})

        # --- ЛІВА ЧАСТИНА: ГРАФІК (ax_plot) ---

        # Використовуємо твої методи для даних
        x_coords = self.intervals()  # Ліві межі
        heights = self.count_ni()  # Висоти
        w = self.count_h()  # Ширина

        # Малюємо стовпчики
        ax_plot.bar(x_coords, heights, width=w, align='edge',
                    color='skyblue', edgecolor='black', label='Емпіричні')

        # Малюємо лінію ідеалу
        expected = len(self.data) / self.k
        ax_plot.axhline(y=expected, color='red', linestyle='--', linewidth=2,
                        label=f'Ідеал (~{int(expected)})')

        # Налаштування осей
        ax_plot.set_title(self.title)
        ax_plot.set_xlabel('Інтервали')
        ax_plot.set_ylabel('Частота')
        ax_plot.legend()
        ax_plot.grid(axis='y', linestyle='--', alpha=0.5)

        # --- ПРАВА ЧАСТИНА: ТЕКСТ (ax_text) ---

        # Прибираємо осі (рамку), щоб був просто чистий лист для тексту
        ax_text.axis('off')

        # Виводимо текст
        ax_text.text(
            x=0, y=1,  # Координати (0, 1) - це лівий верхній кут текстового поля
            s=info_text,  # Твій рядок з інфою
            fontsize=12,
            fontfamily='monospace',  # Моноширинний шрифт виглядає як код/термінал (рівненько)
            verticalalignment='top',  # Вирівнювання по верхньому краю
            bbox=dict(boxstyle='round', facecolor='whitesmoke', edgecolor='lightgray')  # Легка рамочка
        )

        plt.tight_layout()  # Щоб нічого не обрізалось
        plt.show()



    def render(self, ax=None):
        show_now = False
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
            show_now = True

        # 1. Малюємо ідеальну лінію
        expected_height = len(self.data) / self.k
        ax.axhline(y=expected_height, color='red', linestyle='--', linewidth=2,
                   label=f'Ідеал (~{int(expected_height)})')

        # 2. Малюємо стовпчики
        ax.bar(self.intervals(),
               self.count_ni(),
               width=self.count_h(),
               align='edge',
               edgecolor='black',
               color='lightblue',
               label='Емпіричні'
               )

        ax.set_title(self.title)
        ax.set_xlabel('Інтервали')
        ax.set_ylabel('Частота')

        # Якщо створювали вікно самі — показуємо його
        if show_now:
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