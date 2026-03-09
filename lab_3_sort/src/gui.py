import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
from shaker_sort import shaker_sort
from database import save_array, get_user_arrays
from auth import register_user, login_user


class ShakerSortApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Шейкерная сортировка")
        self.root.geometry("800x600")

        self.current_user = None

        # Создаем интерфейс
        self.create_login_frame()

    def create_login_frame(self):
        """Экран входа/регистрации"""
        self.clear_window()

        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)

        ttk.Label(frame, text="Вход в систему", font=("Arial", 16)).pack(pady=10)

        ttk.Label(frame, text="Логин:").pack()
        self.login_entry = ttk.Entry(frame)
        self.login_entry.pack(pady=5)

        ttk.Label(frame, text="Пароль:").pack()
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(frame, text="Войти", command=self.login).pack(pady=5)
        ttk.Button(frame, text="Регистрация", command=self.register).pack(pady=5)
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(fill=tk.X)

        # Кнопка справки (слева от кнопки выхода)
        ttk.Button(top_frame, text="Справка",
                   command=self.show_help).pack(side=tk.RIGHT, padx=2)

    def create_main_frame(self):
        """Главный экран приложения"""
        self.clear_window()

        # Верхняя панель с информацией о пользователе
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(fill=tk.X)
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(fill=tk.X)

        ttk.Label(top_frame, text=f"Пользователь: {self.current_user}").pack(side=tk.LEFT)
        ttk.Button(top_frame, text="Выйти", command=self.logout).pack(side=tk.RIGHT)

        # Основная панель
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Левая панель - ввод и сортировка
        left_frame = ttk.LabelFrame(main_frame, text="Работа с массивом", padding="10")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        ttk.Label(left_frame, text="Введите числа через пробел:").pack(anchor=tk.W)
        self.input_entry = ttk.Entry(left_frame, width=40)
        self.input_entry.pack(fill=tk.X, pady=5)

        ttk.Button(left_frame, text="Случайный массив",
                   command=self.generate_random).pack(pady=2)
        ttk.Button(left_frame, text="Сортировать",
                   command=self.sort_array).pack(pady=2)
        ttk.Button(left_frame, text="Сохранить",
                   command=self.save_array).pack(pady=2)

        ttk.Label(left_frame, text="Исходный массив:").pack(anchor=tk.W, pady=(10, 0))
        self.original_text = scrolledtext.ScrolledText(left_frame, height=5)
        self.original_text.pack(fill=tk.BOTH, expand=True, pady=5)

        ttk.Label(left_frame, text="Отсортированный массив:").pack(anchor=tk.W)
        self.sorted_text = scrolledtext.ScrolledText(left_frame, height=5)
        self.sorted_text.pack(fill=tk.BOTH, expand=True, pady=5)

        # Правая панель - история
        right_frame = ttk.LabelFrame(main_frame, text="Сохраненные массивы", padding="10")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)

        self.history_list = tk.Listbox(right_frame, height=20)
        self.history_list.pack(fill=tk.BOTH, expand=True)

        ttk.Button(right_frame, text="Обновить",
                   command=self.load_history).pack(pady=5)

        # Загружаем историю
        self.load_history()

    def show_help(self):
        """Показывает окно со справкой"""
        help_text = """
        ========== ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ ==========

        1. Вход в систему:
            Если у вас нет аккаунта - нажмите "Регистрация"
            Введите логин и пароль
            Нажмите "Войти"

        2. Работа с массивами:
            Введите числа через пробел (например: 5 2 8 1 9)
            Или нажмите "Случайный массив" для генерации
            Нажмите "Сортировать" для сортировки
            Нажмите "Сохранить" для сохранения в БД

        3. Просмотр истории:
            Справа отображаются сохраненные массивы
            Нажмите "Обновить" для обновления списка

        4. Выход:
           • Нажмите "Выйти" для возврата на экран входа

        ========== О ПРОГРАММЕ ==========
         Алгоритм: Шейкерная сортировка (Shaker sort)
         Версия: 3.0 с графическим интерфейсом и БД
        """

        # Создаем окно справки
        help_window = tk.Toplevel(self.root)
        help_window.title("Справка")
        help_window.geometry("500x400")

        # Текст с прокруткой
        text_area = scrolledtext.ScrolledText(help_window, wrap=tk.WORD, font=("Consolas", 10))
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_area.insert(tk.END, help_text)
        text_area.config(state=tk.DISABLED)  # запрещаем редактирование

        # Кнопка закрытия
        ttk.Button(help_window, text="Закрыть",
                   command=help_window.destroy).pack(pady=5)

    def generate_random(self):
        """Генерация случайного массива"""
        try:
            size = random.randint(5, 15)
            array = [random.randint(-50, 50) for _ in range(size)]
            self.original_text.delete(1.0, tk.END)
            self.original_text.insert(1.0, ' '.join(map(str, array)))
            self.sorted_text.delete(1.0, tk.END)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def sort_array(self):
        """Сортировка массива"""
        try:
            # Получаем исходный массив
            text = self.original_text.get(1.0, tk.END).strip()
            if not text:
                messagebox.showwarning("Предупреждение", "Введите массив")
                return

            array = list(map(int, text.split()))

            # Сортируем
            sorted_array = shaker_sort(array)

            # Показываем результат
            self.sorted_text.delete(1.0, tk.END)
            self.sorted_text.insert(1.0, ' '.join(map(str, sorted_array)))

        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод. Используйте целые числа через пробел")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def save_array(self):
        """Сохранить массив в БД"""
        if not self.current_user:
            messagebox.showwarning("Предупреждение", "Сначала войдите в систему")
            return

        try:
            original_text = self.original_text.get(1.0, tk.END).strip()
            sorted_text = self.sorted_text.get(1.0, tk.END).strip()

            if not original_text or not sorted_text:
                messagebox.showwarning("Предупреждение", "Сначала отсортируйте массив")
                return

            original = list(map(int, original_text.split()))
            sorted_arr = list(map(int, sorted_text.split()))

            save_array(self.current_user, original, sorted_arr)
            messagebox.showinfo("Успех", "Массив сохранен")
            self.load_history()

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def load_history(self):
        """Загрузить историю массивов пользователя"""
        if not self.current_user:
            return

        try:
            arrays = get_user_arrays(self.current_user)
            self.history_list.delete(0, tk.END)

            for arr in arrays:
                display = f"{arr['created_at'][:16]} | Размер: {arr['size']}"
                self.history_list.insert(tk.END, display)

        except Exception as e:
            print(f"Ошибка загрузки истории: {e}")

    def login(self):
        """Авторизация"""
        username = self.login_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Предупреждение", "Заполните все поля")
            return

        success, result = login_user(username, password)

        if success:
            self.current_user = result
            self.create_main_frame()
        else:
            messagebox.showerror("Ошибка", result)

    def register(self):
        """Регистрация"""
        username = self.login_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Предупреждение", "Заполните все поля")
            return

        success, message = register_user(username, password)

        if success:
            messagebox.showinfo("Успех", message)
        else:
            messagebox.showerror("Ошибка", message)

    def logout(self):
        """Выход из системы"""
        self.current_user = None
        self.create_login_frame()

    def clear_window(self):
        """Очистить окно"""
        for widget in self.root.winfo_children():
            widget.destroy()


def main():
    root = tk.Tk()
    app = ShakerSortApp(root)
    root.mainloop()


if __name__ == "__main__":
    # Инициализируем БД при запуске
    from database import init_db

    init_db()

    main()