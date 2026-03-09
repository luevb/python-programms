"""
Главный модуль консольного приложения
Демонстрирует работу шейкерной сортировки
"""

import sys
import os

# Добавляем путь для импорта модулей проекта
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from src.shaker_sort import shaker_sort_with_stats, is_sorted
from src.utils import (
    read_from_keyboard,
    generate_random_array,
    load_from_file,
    save_to_file,
    print_results
)


def display_menu():
    """Отображение главного меню"""
    print("\n" + "=" * 60)
    print("ПРОГРАММА ШЕЙКЕРНОЙ СОРТИРОВКИ")
    print("=" * 60)
    print("Выберите способ ввода данных:")
    print("  1. Ввод с клавиатуры")
    print("  2. Генерация случайных чисел")
    print("  3. Загрузка из файла")
    print("  4. Выход")
    print("-" * 60)


def main():
    """Основная функция программы"""

    while True:
        display_menu()

        choice = input("Ваш выбор (1-4): ").strip()

        # Обработка выхода
        if choice == '4':
            print("Программа завершена.")
            break

        # Получение массива согласно выбору пользователя
        array = None

        if choice == '1':
            array = read_from_keyboard()

        elif choice == '2':
            array = generate_random_array()

        elif choice == '3':
            filename = input("Введите имя файла: ").strip()
            array = load_from_file(filename)

        else:
            print("Ошибка: неверный выбор. Используйте 1, 2, 3 или 4")
            continue

        # Проверка корректности полученного массива
        if array is None:
            print("Не удалось получить массив. Попробуйте снова.")
            continue

        if len(array) == 0:
            print("Ошибка: массив пуст")
            continue

        # Вывод исходного массива
        print(f"\nИсходный массив: {array}")

        # Сортировка
        print("Выполняется сортировка...")
        sorted_array, statistics = shaker_sort_with_stats(array)

        # Проверка корректности сортировки
        if is_sorted(sorted_array):
            print("Сортировка выполнена успешно")
        else:
            print("ОШИБКА: массив не отсортирован!")

        # Вывод результатов
        print_results(array, sorted_array, statistics)

        # Предложение сохранить результаты
        save_choice = input("\nСохранить результаты в файл? (y/n): ").strip().lower()
        if save_choice in ('y', 'yes', 'да', 'д'):
            filename = input("Имя файла для сохранения: ").strip()

            # Сохраняем расширенную информацию
            try:
                file = open(filename, 'w', encoding='utf-8')

                file.write("РЕЗУЛЬТАТЫ ШЕЙКЕРНОЙ СОРТИРОВКИ\n")
                file.write("=" * 40 + "\n\n")

                file.write("ИСХОДНЫЙ МАССИВ:\n")
                file.write(' '.join(str(x) for x in array) + "\n\n")

                file.write("ОТСОРТИРОВАННЫЙ МАССИВ:\n")
                file.write(' '.join(str(x) for x in sorted_array) + "\n\n")

                file.write("СТАТИСТИКА:\n")
                file.write(f"  Количество сравнений: {statistics['comparisons']}\n")
                file.write(f"  Количество обменов: {statistics['swaps']}\n")
                file.write(f"  Количество проходов: {statistics['passes']}\n")

                file.close()
                print(f"Результаты сохранены в файл '{filename}'")

            except IOError:
                print(f"Ошибка при сохранении в файл '{filename}'")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
        sys.exit(0)
    except Exception as error:
        print(f"\nНепредвиденная ошибка: {error}")
        sys.exit(1)