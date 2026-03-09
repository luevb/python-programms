"""
Модуль реализации шейкерной сортировки (Shaker sort)
Алгоритм: двунаправленная пузырьковая сортировка
"""


def shaker_sort(array):
    # Создаем копию, чтобы не изменять оригинал
    result = array.copy()

    # Пустой список или из одного элемента сразу возвращаем
    if len(result) <= 1:
        return result

    # Границы неотсортированной части
    left_boundary = 0
    right_boundary = len(result) - 1

    # Пока есть неотсортированная область
    while left_boundary < right_boundary:
        # Проход слева направо - "всплывают" максимальные элементы
        current_index = left_boundary
        while current_index < right_boundary:
            # Если текущий элемент больше следующего - меняем
            if result[current_index] > result[current_index + 1]:
                # Обмен значений через временную переменную
                temp = result[current_index]
                result[current_index] = result[current_index + 1]
                result[current_index + 1] = temp
            current_index += 1

        # После прохода наибольший элемент на своем месте справа
        right_boundary -= 1

        # Проход справа налево - "тонут" минимальные элементы
        current_index = right_boundary
        while current_index > left_boundary:
            # Если предыдущий элемент больше текущего - меняем
            if result[current_index - 1] > result[current_index]:
                temp = result[current_index - 1]
                result[current_index - 1] = result[current_index]
                result[current_index] = temp
            current_index -= 1

        # После прохода наименьший элемент на своем месте слева
        left_boundary += 1

    return result


def shaker_sort_with_stats(array):
    # Сортирует список и собирает статистику выполнения
    result = array.copy()

    if len(result) <= 1:
        return result, {'comparisons': 0, 'swaps': 0, 'passes': 0}

    left = 0
    right = len(result) - 1

    # Статистика
    comparisons = 0  # количество сравнений элементов
    swaps = 0  # количество обменов
    passes = 0  # количество проходов по массиву

    while left < right:
        # Проход слева направо
        passes += 1
        i = left
        while i < right:
            comparisons += 1
            if result[i] > result[i + 1]:
                # Меняем местами
                result[i], result[i + 1] = result[i + 1], result[i]
                swaps += 1
            i += 1
        right -= 1

        # Проверка, не закончилась ли сортировка
        if left >= right:
            break

        # Проход справа налево
        passes += 1
        i = right
        while i > left:
            comparisons += 1
            if result[i - 1] > result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]
                swaps += 1
            i -= 1
        left += 1

    # Формируем статистику
    statistics = {
        'comparisons': comparisons,
        'swaps': swaps,
        'passes': passes
    }

    return result, statistics


def is_sorted(array):
    """
    Проверяет, отсортирован ли список по возрастанию
    """
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True