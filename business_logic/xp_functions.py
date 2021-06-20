try:
    from .get_functions import get_path_xp
except ImportError:
    from get_functions import get_path_xp

import sqlite3

def create_database(loggin: str):
    """
    Создаёт базу данных для новозарегистрированного пользователя

    """
    conn = sqlite3.connect(get_path_xp() + loggin + '.db')
