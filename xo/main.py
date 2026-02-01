print("Добро пожаловать в игру Крестики-Нолики.")
print("Примечание: Строчка - по горизонтали. Столбец по вертикали.")
print()
table = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
def winner():
    # Проверка строк для X
    if table[0][0] == 'X' and table[0][1] == 'X' and table[0][2] == 'X':
        return 'X'
    if table[1][0] == 'X' and table[1][1] == 'X' and table[1][2] == 'X':
        return 'X'
    if table[2][0] == 'X' and table[2][1] == 'X' and table[2][2] == 'X':
        return 'X'

    # Проверка столбцов для X
    if table[0][0] == 'X' and table[1][0] == 'X' and table[2][0] == 'X':
        return 'X'
    if table[0][1] == 'X' and table[1][1] == 'X' and table[2][1] == 'X':
        return 'X'
    if table[0][2] == 'X' and table[1][2] == 'X' and table[2][2] == 'X':
        return 'X'

    # Проверка диагоналей для X
    if table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X':
        return 'X'
    if table[0][2] == 'X' and table[1][1] == 'X' and table[2][0] == 'X':
        return 'X'

    # Проверка строк для 0
    if table[0][0] == '0' and table[0][1] == '0' and table[0][2] == '0':
        return '0'
    if table[1][0] == '0' and table[1][1] == '0' and table[1][2] == '0':
        return '0'
    if table[2][0] == '0' and table[2][1] == '0' and table[2][2] == '0':
        return '0'

    # Проверка столбцов для 0
    if table[0][0] == '0' and table[1][0] == '0' and table[2][0] == '0':
        return '0'
    if table[0][1] == '0' and table[1][1] == '0' and table[2][1] == '0':
        return '0'
    if table[0][2] == '0' and table[1][2] == '0' and table[2][2] == '0':
        return '0'

    # Проверка диагоналей для 0
    if table[0][0] == '0' and table[1][1] == '0' and table[2][2] == '0':
        return '0'
    if table[0][2] == '0' and table[1][1] == '0' and table[2][0] == '0':
        return '0'
    return '*'
def draw_table():
    for i in table:
        print(*i)
    print()


def write_X0(value):
    # Ввод строчки.
    while True:
        try:
            line = int(input("Выберите строчку (1, 2, 3): ")) - 1
            if 0 <= line <= 2:
                break
            else:
                print("Ошибка! Выберите число (1, 2, 3)")
        except ValueError:
            print("Вы ввели неверное число!")

    # Ввод столбца.
    while True:
        try:
            column = int(input("Выберите столбец (1, 2, 3): ")) - 1
            if 0 <= column <= 2:
                break
            else:
                print("Ошибка! Выберите число (1, 2, 3)")
        except ValueError:
            print("Вы ввели неверное число!")
    if table[line][column] == '*':
        table[line][column] = value
    else:
        print("Вы выбрали занятую ячейку, вы пропускаете ход!")
    return line, column

for i in range(1, 10):
    if i % 2 != 0:
        draw_table()
        print("Выберите ячейку для Х")
        write_X0(value = 'X')
    else:
        draw_table()
        print("Выберите ячейку для 0")
        write_X0(value = '0')
    win = winner()
    if win == 'X':
        print("Крестики выиграли")
        draw_table()
        break
    elif win == '0':
        print("Нолики выиграли")
        draw_table()
        break
win = winner()
if win == '*':
    print("Ничья!!!")
    draw_table()
