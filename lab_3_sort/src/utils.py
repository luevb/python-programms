"""
Вспомогательные функции для ввода/вывода данных
"""

import random
import os


def read_from_keyboard():
    """
    Чтение чисел с клавиатуры
    Возвращает:
        список введенных чисел или None при ошибке
    """
    while True:
        user_input = input("Введите числа через пробел: ").strip()

        if not user_input:
            print("Ошибка: строка пуста")
            continue

        # Разбиваем строку на элементы
        elements = user_input.split()
        numbers = []
        error_occurred = False

        for element in elements:
            try:
                number = int(element)
                numbers.append(number)
            except ValueError:
                print(f"Ошибка: '{element}' не является целым числом")
                error_occurred = True
                break

        if not error_occurred:
            return numbers


def generate_random_array():
    """
    Генерация массива случайных чисел
    """
    while True:
        try:
            size = int(input("Введите размер массива: "))
            if size <= 0:
                print("Размер должен быть положительным числом")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число")

    # Генерируем числа от -100 до 100
    random_numbers = []
    for _ in range(size):
        random_numbers.append(random.randint(-100, 100))

    return random_numbers


def load_from_file(filename):
    """
    Загрузка чисел из файла
    """
    if not os.path.exists(filename):
        print(f"Ошибка: файл '{filename}' не найден")
        return None

    numbers = []
    line_number = 0

    try:
        file = open(filename, 'r', encoding='utf-8')

        for line in file:
            line_number += 1
            line = line.strip()

            # Пропускаем пустые строки
            if not line:
                continue

            # Разбираем числа в строке
            for item in line.split():
                try:
                    num = int(item)
                    numbers.append(num)
                except ValueError:
                    print(f"Ошибка в файле (строка {line_number}): '{item}' - не число")
                    file.close()
                    return None

        file.close()

        if not numbers:
            print("Ошибка: файл не содержит чисел")
            return None

        return numbers

    except IOError:
        print(f"Ошибка при чтении файла '{filename}'")
        return None


def save_to_file(array, filename):
    """
    Сохранение массива в файл
    """
    try:
        file = open(filename, 'w', encoding='utf-8')

        # Преобразуем числа в строку
        line = ' '.join(str(x) for x in array)
        file.write(line)

        file.close()
        print(f"Массив сохранен в файл '{filename}'")
        return True

    except IOError:
        print(f"Ошибка при сохранении в файл '{filename}'")
        return False


def print_results(original, sorted_array, statistics):
    """
    Вывод результатов сортировки на экран
    Параметры:
        original: исходный массив
        sorted_array: отсортированный массив
        statistics: словарь со статистикой
    """
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ СОРТИРОВКИ")
    print("=" * 60)

    print(f"\nИсходный массив (длина: {len(original)}):")
    print(original)

    print(f"\nОтсортированный массив:")
    print(sorted_array)

    print(f"\nСтатистика выполнения:")
    print(f"Сравнений: {statistics['comparisons']}")
    print(f"Обменов: {statistics['swaps']}")
    print(f"Проходов: {statistics['passes']}")
    print("=" * 60)