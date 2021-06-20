try:
    from .get_functions import *
    from .get_functions import _get_path_ac2, _get_path_temp2
except ImportError:
    from get_functions import *
    from get_functions import _get_path_ac2, _get_path_temp2
import sqlite3
import os


def create_paths():
    """
    Создаёт пути до [
        папки с аккаунтами,
        TEMP папки,
        папки с расходами
    ]

    """
    if not os.path.exists(_get_path_ac2()):
        os.makedirs(_get_path_ac2())
    if not os.path.exists(_get_path_temp2()):
        os.makedirs(_get_path_temp2())
    if not os.path.exists(get_path_xp()):
        os.makedirs(get_path_xp())

def create_table_ac():
    """
    Создаёт таблицу в базе данных с аккаунтами

    """
    conn = sqlite3.connect(get_path_ac())
    c = conn.cursor()
    with conn:
        c.execute(f"""CREATE TABLE IF NOT EXISTS {get_tb_ac()} (
        name TEXT PRIMARY KEY NOT NULL,
        password TEXT NOT NULL,
        database TEXT NOT NULL,
        salary REAL,
        investment REAL,
        invest_per REAL,
        shares REAL,
        shares_per REAL,
        bonds REAL,
        bonds_per REAL,
        total_money REAL,
        in_work REAL)""")

def create_temp():
    """
    Создаёт временную базу и таблицу в ней

    """
    conn = sqlite3.connect(get_path_temp())
    c = conn.cursor()
    with conn:
        c.execute(f"""CREATE TABLE IF NOT EXISTS temp (
        name TEXT PRIMARY KEY NOT NULL,
        password TEXT NOT NULL,
        admin VARCHAR(10))""")
create_paths()
create_temp()
create_table_ac()
