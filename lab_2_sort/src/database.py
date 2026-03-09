import sqlite3
import os
from contextlib import contextmanager

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'database.db')


@contextmanager
def get_db():
    """Контекстный менеджер для работы с БД"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # чтобы получать доступ по именам колонок
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    """Создание таблиц при первом запуске"""
    with get_db() as conn:
        cursor = conn.cursor()

        # Таблица пользователей
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Таблица массивов
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS arrays (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                original_array TEXT NOT NULL,
                sorted_array TEXT NOT NULL,
                size INTEGER NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

        # Индексы
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_arrays_user_id ON arrays(user_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_arrays_size ON arrays(size)')

        conn.commit()


def save_array(user_id, original_array, sorted_array):
    """Сохранить массив в БД"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO arrays (user_id, original_array, sorted_array, size)
            VALUES (?, ?, ?, ?)
        ''', (
            user_id,
            ' '.join(map(str, original_array)),
            ' '.join(map(str, sorted_array)),
            len(original_array)
        ))
        conn.commit()
        return cursor.lastrowid


def get_user_arrays(user_id):
    """Получить все массивы пользователя"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM arrays 
            WHERE user_id = ? 
            ORDER BY created_at DESC
        ''', (user_id,))
        return cursor.fetchall()


def get_arrays_by_size(size):
    """Получить массивы определенного размера (для тестов)"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM arrays WHERE size = ?', (size,))
        return cursor.fetchall()


def clear_all_arrays():
    """Очистить все массивы (для тестов)"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM arrays')
        conn.commit()
        return cursor.rowcount