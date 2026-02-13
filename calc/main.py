import tkinter as tk
from tkinter import ttk

current_expression = ''


history_label = None  # Будем переиспользовать одну метку


def update_history():
    """Обновляет существующую метку вместо создания новой"""
    global history_label

    if history_label is None:
        history_label = ttk.Label(root, text="", font=("Consolas", 14, "bold"))
        history_label.place(relx=0.5, rely=0.7, anchor="center")

    history_label.config(text=current_expression)


def add_buttons(symbol):
    area_input.insert(tk.END, symbol)


def clear():
    global current_expression
    area_input.delete(0, "end")
    area_output.delete(0, "end")
    current_expression = ''
    update_history()

def add_operator(operator):
    global current_expression
    num = area_input.get()
    if num:
        current_expression = current_expression + num + operator
        area_input.delete(0, tk.END)
        update_history()


def equal():
    global current_expression
    try:
        area_output.delete(0, tk.END)
        # Добавляем последнее число
        last_num = area_input.get()
        if last_num:
            full_expr = current_expression + last_num
        else:
            full_expr = current_expression[:-1]  # Убираем последний оператор

        result = eval(full_expr)

        # Показываем выражение в истории
        current_expression = full_expr + '='
        update_history()

        # Показываем результат
        area_input.delete(0, tk.END)
        area_output.insert(0, str(result))
        current_expression = ''
        update_history()
    except ZeroDivisionError:
        area_input.delete(0, tk.END)
        area_output.insert(0, "Деление на 0")
        current_expression = ''
        update_history()
    except SyntaxError:
        area_input.delete(0, tk.END)
        area_output.insert(0, "Ошибка")
        current_expression = ''
        update_history()

root = tk.Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)
root.iconbitmap("Calculator.ico")
root.title("Калькулятор")
style = ttk.Style()
style.configure("TButton",font=("Consolas", 12, "bold"))
hello_text = ttk.Label(root, text="Введите число", font=("Consolas", 14, "bold"))
area_input = ttk.Entry(font=("Consolas", 20, "bold"))
area_output = ttk.Entry(font=("Consolas", 20, "bold"))
area_output_text = ttk.Label(root, text='Ответ', font=("Consolas", 14, "bold"))
area_output_text.place(relx=0.5, rely=0.84, anchor="center")
area_output.place(relx=0.5, rely=0.9, anchor="center")
hello_text.place(relx=0.5, rely=0.03, anchor="center")
area_input.place(relx=0.5, rely=0.09, anchor="center")

button_1 = ttk.Button(root, text='1', cursor='hand2', command=lambda: add_buttons('1'))
button_2 = ttk.Button(root, text='2', cursor='hand2', command=lambda: add_buttons('2'))
button_3 = ttk.Button(root, text='3', cursor='hand2', command=lambda: add_buttons('3'))
button_4 = ttk.Button(root, text='4', cursor='hand2', command=lambda: add_buttons('4'))
button_5 = ttk.Button(root, text='5', cursor='hand2', command=lambda: add_buttons('5'))
button_6 = ttk.Button(root, text='6', cursor='hand2', command=lambda: add_buttons('6'))
button_7 = ttk.Button(root, text='7', cursor='hand2', command=lambda: add_buttons('7'))
button_8 = ttk.Button(root, text='8', cursor='hand2', command=lambda: add_buttons('8'))
button_9 = ttk.Button(root, text='9', cursor='hand2', command=lambda: add_buttons('9'))
button_0 = ttk.Button(root, text='0', cursor='hand2', command=lambda: add_buttons('0'))
button_1.place(relx=0.3129, rely=0.44, anchor="center", width=60, height=60)
button_2.place(relx=0.4329, rely=0.44, anchor="center", width=60, height=60)
button_3.place(relx=0.5529, rely=0.44, anchor="center", width=60, height=60)
button_4.place(relx=0.3129, rely=0.32, anchor="center", width=60, height=60)
button_5.place(relx=0.4329, rely=0.32, anchor="center", width=60, height=60)
button_6.place(relx=0.5529, rely=0.32, anchor="center", width=60, height=60)
button_7.place(relx=0.3129, rely=0.2, anchor="center", width=60, height=60)
button_8.place(relx=0.4329, rely=0.2, anchor="center", width=60, height=60)
button_9.place(relx=0.5529, rely=0.2, anchor="center", width=60, height=60)
button_0.place(relx=0.4329, rely=0.56, anchor="center", width=60, height=60)

button_add = ttk.Button(root, text="+", cursor='hand2', command=lambda: add_operator('+'))
button_sub = ttk.Button(text="-", cursor='hand2', command=lambda: add_operator('-'))
button_divide = ttk.Button(text="/", cursor='hand2', command=lambda: add_operator('/'))
button_multiply = ttk.Button(text="*", cursor='hand2', command=lambda: add_operator('*'))
button_equal = ttk.Button(text="=", cursor='hand2', command=equal)
button_clear = ttk.Button(text="Clear", cursor='hand2', command=clear)
button_add.place(relx=0.6729, rely=0.2, anchor="center", width=60, height=60)
button_sub.place(relx=0.6729, rely=0.32, anchor="center", width=60, height=60)
button_divide.place(relx=0.6729, rely=0.44, anchor="center", width=60, height=60)
button_multiply.place(relx=0.6729, rely=0.56, anchor="center", width=60, height=60)
button_equal.place(relx=0.5529, rely=0.56, anchor="center", width=60, height=60)
button_clear.place(relx=0.3129, rely=0.56, anchor="center", width=60, height=60)
root.mainloop()
