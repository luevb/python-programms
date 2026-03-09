import sqlite3
import hashlib
import os
from database import get_db


def hash_password(password):
    """Хеширование пароля (никогда не храните пароли в открытом виде!)"""
    salt = "lab3_salt"  # в реальном проекте нужна случайная соль
    return hashlib.sha256((password + salt).encode()).hexdigest()


def register_user(username, password):
    """Регистрация нового пользователя"""
    with get_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO users (username, password)
                VALUES (?, ?)
            ''', (username, hash_password(password)))
            conn.commit()
            return True, "Регистрация успешна"
        except sqlite3.IntegrityError:
            return False, "Пользователь уже существует"


def login_user(username, password):
    """Авторизация пользователя"""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM users 
            WHERE username = ? AND password = ?
        ''', (username, hash_password(password)))
        user = cursor.fetchone()

        if user:
            return True, user['id']
        else:
            return False, "Неверный логин или пароль"