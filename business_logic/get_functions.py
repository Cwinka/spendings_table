import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from .config import config
except ImportError:
    from config import config


user = ''
def get_base_dir() -> str:
    """ Возвращает root дирректорию проекта """
    return config.BASE_DIR

def get_path_ac() -> str: #
    """ Возвращает путь до базы данных с аккаунтами """
    return config.PATH_TO_ACCOUNTS + config.DB_FOR_ACCOUNTS

def _get_path_ac2() -> str: #
    """ Возвращает путь до папки с аккаунтами """
    return config.PATH_TO_ACCOUNTS

# def get_db_ac(): # Совмещено с путём
#     """ Возвращает название базы данных с аккаунтами """
#     return DB_FOR_ACCOUNTS

def get_tb_ac() -> str:
    """ Возвращает название таблицы с аккаунтами """
    return config.TABLE_FOR_ACCOUNTS

def get_path_xp() -> str:
    """ Возвращает путь до базы даннах с расходами """
    return config.PATH_TO_EXPENS

def get_path_temp() -> str:
    """ Возвращает путь до временной базы данных """
    return config.PATH_TO_TEMP +config.DB_FOR_TEMP

def _get_path_temp2() -> str:
    """ Возвращает путь до TEMP папки"""
    return config.PATH_TO_TEMP

def _put_user(login: str) -> str:
    """ Определяет текущего пользователя, нужна для get_user """
    global user
    user = login
    return user

def _del_user() -> str:
    """ Удаляет текущего пользователя """
    global user
    user = ''
    return user

def get_user() -> str:
    """ Получает текущего пользователя """
    return user

def get_path_to_database() -> str:
    if user == 'b4914600112ba18af7798b6c1a1363728ae1d96f':
        return get_path_xp() + 'spendings2.db'
    """ Путь до базы данных конкретного пользователя """
    return get_path_xp() + user + '.db'
# print(get_database())
