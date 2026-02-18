from controller import CLab1
import os

if __name__ == '__main__':

    # Початкові значення (дефолтні)
    a: int = int(pow(5, 13))
    c: int = int(pow(2, 31))
    quantity: int = 10000
    seed = 1

    while True:
        print("╔═════════════════════════════════════════════════════╗")
        print("║              ЛАБОРАТОРНА РОБОТА №1                  ║")
        print("╠═════════════════════════════════════════════════════╣")
        print("║ 1. Запустити з дефолтними параметрами (a=5^13...)   ║")
        print("║ 2. Згенерувати 3 випадкові графіки                  ║")
        print("║ 3. Ввести свої параметри (a, c, N)                  ║")
        print("║ 0. Вихід                                            ║")
        print("╚═════════════════════════════════════════════════════╝")

        choice = input("\n👉 Оберіть пункт меню: ").strip()

        match choice:
            case '1':
                print(f"\n[INFO] Запуск генерації...")
                print(f"Параметри: a={a}, c={c}, N={quantity}")

                lab = CLab1(a, c, quantity, seed)
                lab.make_histogram()

                input("\n✅ Готово! Натисніть Enter, щоб повернутися в меню...")

            case '2':
                print("\n[INFO] Генерація 3-х графіків для порівняння...")

                CLab1.make_3random_histograms(quantity, seed)

                input("\n✅ Готово! Натисніть Enter, щоб повернутися в меню...")

            case '3':
                print("\n[SETTINGS] Введіть нові параметри:")
                try:
                    # Використовуємо тимчасові змінні, щоб не зламати програму, якщо введуть літери
                    new_a = int(input("  -> Введіть a: "))
                    new_c = int(input("  -> Введіть c: "))
                    new_quantity = int(input("  -> Введіть кількість (N): "))
                    new_seed = int(input("  -> Введіть seed: "))

                    lab = CLab1(new_a, new_c, new_quantity, new_seed)
                    lab.make_histogram()

                except ValueError:
                    print("\n❌ Помилка: Потрібно вводити цілі числа!")

                input("\n✅ Готово! Натисніть Enter, щоб повернутися в меню...")

            case '0':
                print("\n👋 До побачення!")
                break

            case _:
                print("\n⚠️ Невірний вибір.")
                input("Натисніть Enter і спробуйте ще раз...")