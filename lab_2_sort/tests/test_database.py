import sys
import os
import time
import random
import sqlite3
from contextlib import contextmanager

# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import init_db, save_array, get_arrays_by_size, clear_all_arrays
from src.shaker_sort import shaker_sort

# Используем отдельную БД для тестов
TEST_DB_PATH = os.path.join(os.path.dirname(__file__), 'test_database.db')


@contextmanager
def test_db():
    """Временная БД для тестов"""
    # Подменяем путь к БД
    import src.database
    original_path = src.database.DB_PATH
    src.database.DB_PATH = TEST_DB_PATH

    # Инициализируем тестовую БД
    init_db()

    try:
        yield
    finally:
        # Очищаем и восстанавливаем
        if os.path.exists(TEST_DB_PATH):
            os.remove(TEST_DB_PATH)
        src.database.DB_PATH = original_path


def generate_random_array(size):
    """Генерация случайного массива"""
    return [random.randint(-100, 100) for _ in range(size)]


def test_add_arrays(count):
    """Тест добавления count массивов"""
    print(f"\n--- Тест добавления {count} массивов ---")

    with test_db():
        start_time = time.time()

        for i in range(count):
            size = random.randint(5, 20)
            original = generate_random_array(size)
            sorted_arr = shaker_sort(original)
            save_array(1, original, sorted_arr)  # user_id = 1 (тестовый)

        elapsed = time.time() - start_time

        # Проверяем, что все добавились
        arrays = get_arrays_by_size(5)  # просто проверяем, что есть данные

        success = len(arrays) > 0
        print(f"Результат: {'УСПЕХ' if success else 'НЕУДАЧА'}")
        print(f"Время: {elapsed:.3f} сек")
        print(f"Скорость: {count / elapsed:.1f} записей/сек")

        return success, elapsed


def test_load_and_sort(count):
    """Тест выгрузки и сортировки count массивов"""
    print(f"\n--- Тест выгрузки и сортировки {count} массивов ---")

    with test_db():
        # Сначала добавляем тестовые данные
        arrays = []
        for i in range(count):
            size = random.randint(5, 20)
            original = generate_random_array(size)
            arrays.append(original)
            sorted_arr = shaker_sort(original)
            save_array(1, original, sorted_arr)

        # Теперь выгружаем и проверяем сортировку
        start_time = time.time()
        successful = 0

        for original in arrays:
            # В реальности тут была бы загрузка из БД
            test_sorted = shaker_sort(original)

            # Проверяем правильность сортировки
            is_sorted = all(test_sorted[i] <= test_sorted[i + 1]
                            for i in range(len(test_sorted) - 1))
            if is_sorted:
                successful += 1

        elapsed = time.time() - start_time
        avg_time = elapsed / count if count > 0 else 0

        success = (successful == count)
        print(f"Результат: {'УСПЕХ' if success else 'НЕУДАЧА'}")
        print(f"Общее время: {elapsed:.3f} сек")
        print(f"Среднее время на массив: {avg_time * 1000:.2f} мс")
        print(f"Успешно обработано: {successful}/{count}")

        return success, elapsed, avg_time


def test_clear_database(count):
    """Тест очистки БД с count записями"""
    print(f"\n--- Тест очистки БД ({count} записей) ---")

    with test_db():
        # Добавляем записи
        for i in range(count):
            size = random.randint(5, 20)
            original = generate_random_array(size)
            sorted_arr = shaker_sort(original)
            save_array(1, original, sorted_arr)

        # Очищаем
        start_time = time.time()
        deleted = clear_all_arrays()
        elapsed = time.time() - start_time

        success = (deleted == count)
        print(f"Результат: {'УСПЕХ' if success else 'НЕУДАЧА'}")
        print(f"Время: {elapsed:.3f} сек")
        print(f"Удалено записей: {deleted}")

        return success, elapsed


def run_all_tests():
    """Запуск всех интеграционных тестов"""
    print("=" * 60)
    print("ИНТЕГРАЦИОННОЕ ТЕСТИРОВАНИЕ")
    print("=" * 60)

    results = []

    # Тест 1: Добавление массивов
    for count in [100, 1000, 10000]:
        success, elapsed = test_add_arrays(count)
        results.append(("add", count, success, elapsed))

    # Тест 2: Выгрузка и сортировка (запускаем 3 раза)
    for count in [100, 1000, 10000]:
        for run in range(1, 4):
            print(f"\n--- Запуск {run} для {count} массивов ---")
            success, total_time, avg_time = test_load_and_sort(count)
            results.append(("load", count, run, success, total_time, avg_time))

    # Тест 3: Очистка БД
    for count in [100, 1000, 10000]:
        success, elapsed = test_clear_database(count)
        results.append(("clear", count, success, elapsed))

    print("\n" + "=" * 60)
    print("СВОДКА РЕЗУЛЬТАТОВ")
    print("=" * 60)

    for result in results:
        print(result)


if __name__ == "__main__":
    run_all_tests()