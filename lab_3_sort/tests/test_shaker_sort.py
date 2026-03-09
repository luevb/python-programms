import sys
import os

# Добавляем путь к тестируемым модулям
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from src.shaker_sort import shaker_sort, is_sorted


def run_test(test_name, test_function):
    """Вспомогательная функция для запуска тестов"""
    print(f"Тест {test_name}: ", end='')
    try:
        test_function()
        print("ПРОЙДЕН")
    except AssertionError as error:
        print(f"НЕ ПРОЙДЕН - {error}")
    except Exception as error:
        print(f"ОШИБКА - {error}")


def test_empty_array():
    """Тест сортировки пустого массива"""
    input_data = []
    expected = []
    result = shaker_sort(input_data)
    assert result == expected, f"Получено {result}, ожидалось {expected}"
    assert is_sorted(result), "Результат не отсортирован"


def test_single_element():
    """Тест сортировки массива из одного элемента"""
    input_data = [42]
    expected = [42]
    result = shaker_sort(input_data)
    assert result == expected, f"Получено {result}, ожидалось {expected}"
    assert is_sorted(result), "Результат не отсортирован"


def test_sorted_array():
    """Тест сортировки уже отсортированного массива"""
    input_data = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    result = shaker_sort(input_data)
    assert result == expected, f"Получено {result}, ожидалось {expected}"
    assert is_sorted(result), "Результат не отсортирован"


def test_reverse_sorted():
    """Тест сортировки массива в обратном порядке"""
    input_data = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    result = shaker_sort(input_data)
    assert result == expected, f"Получено {result}, ожидалось {expected}"
    assert is_sorted(result), "Результат не отсортирован"


def test_random_array():
    """Тест сортировки случайного массива"""
    input_data = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    result = shaker_sort(input_data)
    assert result == expected, f"Получено {result}, ожидалось {expected}"
    assert is_sorted(result), "Результат не отсортирован"


def test_duplicates():
    """Тест сортировки массива с дубликатами"""
    input_data = [3, 1, 4, 1, 5, 9, 2, 5]
    result = shaker_sort(input_data)
    assert is_sorted(result), "Результат не отсортирован"
    # Проверяем, что все элементы сохранились
    assert sorted(input_data) == result, "Потеряны элементы"


def test_negative_numbers():
    """Тест сортировки массива с отрицательными числами"""
    input_data = [-5, 12, -3, 0, -8, 7]
    expected = [-8, -5, -3, 0, 7, 12]
    result = shaker_sort(input_data)
    assert result == expected, f"Получено {result}, ожидалось {expected}"
    assert is_sorted(result), "Результат не отсортирован"


def test_preserve_original():
    """Тест сохранения исходного массива"""
    original = [3, 1, 4, 1, 5]
    original_copy = original.copy()

    result = shaker_sort(original)

    assert original == original_copy, "Исходный массив был изменен"
    assert result != original_copy or is_sorted(original_copy), \
        "Результат должен отличаться от неотсортированного оригинала"


def run_all_tests():
    """Запуск всех тестов"""
    print("=" * 70)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА ШЕЙКЕРНОЙ СОРТИРОВКИ")
    print("=" * 70)
    print()

    tests = [
        ("Пустой массив", test_empty_array),
        ("Один элемент", test_single_element),
        ("Уже отсортирован", test_sorted_array),
        ("Обратный порядок", test_reverse_sorted),
        ("Случайный набор", test_random_array),
        ("Дубликаты", test_duplicates),
        ("Отрицательные числа", test_negative_numbers),
        ("Сохранение оригинала", test_preserve_original)
    ]

    for test_name, test_func in tests:
        run_test(test_name, test_func)

    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()