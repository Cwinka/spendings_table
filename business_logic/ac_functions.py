import sys
import os
import sqlite3
import os
from typing import Union
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from .get_functions import *
    from .get_functions import _put_user, _del_user
    from .security_functions import get_password, get_login
    from .xp_functions import create_database
except ImportError:
    from get_functions import *
    from get_functions import _put_user, _del_user
    from security_functions import get_password, get_login
    from xp_functions import create_database


conn = sqlite3.connect(get_path_ac())
conn_temp = sqlite3.connect(get_path_temp())
c = conn.cursor()
c_temp = conn_temp.cursor()

def check_login_on_existing(login: str) -> bool:
    """
    Проверка существования логина в базе логинов
    Принимает сырой логин

    """
    login = get_login(login)
    c.execute("""SELECT name FROM {0} WHERE name="{1}" """.format(get_tb_ac(),
                                                                  login))
    if c.fetchall():
        return True
    else:
        return False

    #  сюда напихать проверок имени и пароля
def try_register(login: str, password: str) -> bool:
    """
     Попытка регистрации, возвращает True если подошли поля,
     False в другом случае
     Принимает сырые логин и пароль

    """

    if check_login_on_existing(login):
        return False
    else:
        password = get_password(login, password)
        with conn:
            sql = 'INSERT INTO {0} VALUES ("{1}", "{2}", "{1}.db", "{3}")'
            c.execute(sql.format(get_tb_ac(),
                                 login,
                                 password,
                                 "\", \"".join(["0"]*9)))
            create_database(login)
        return True

def try_sign_in(login: str, password: str, prep_password: bool = False) -> bool:
    """
     Попытка входа в аккаунт возвращает True если подошли поля,
     False в другом случае
     Принимает сырые логин и пароль, если не указан prep_password, иначе
     подготовленные (полученные с security_functions)

    """

    if not prep_password:
        password = get_password(login, password)
        login = get_login(login)
    c.execute('SELECT * FROM {0} WHERE password="{1}"'.format(get_tb_ac(),
                                                              password))

    if c.fetchone():
        _put_user(login)
        return True
    return False

def try_sign_in_temp() -> bool:
    """
     Попытка входа в аккаунт с TEMP базы, возвращает True если подошли поля,
     False в другом случае

    """
    try:
        c_temp.execute(""" SELECT * FROM  temp """)
        login, password, _ = c_temp.fetchone()
    except TypeError:
        return False
    return try_sign_in(login, password, True)

def remember_user(login: str, password: str, flag: bool):
    """
    Запоминает пользователя, записывая его в TEMP базу

    """
    if flag:
        login = get_login(login)
        password = get_password(login, password)
        with conn_temp:
            c_temp.execute(""" INSERT INTO temp(name, password) VALUES ("{0}", "{1}") """.format(login, password))

def sign_off():
    """
     Выход из аккаунта пользователя

    """
    _del_user()
    with conn_temp:
        c_temp.execute(""" DELETE FROM temp """)

def _delete_account(login: str):
    """
    Удаление акканта

    """
    login = get_login(login)
    with conn:
        c.execute('DELETE FROM {0} WHERE name="{1}"'.format(get_tb_ac(), login))
    try:
        os.remove(get_path_xp() + login + '.db')
    except Exception:
        pass

# print(try_register('Nikita', '12123123'))
# print(try_sign_in('Nikita', '12123123'))
# print(get_login('Nikita'))
# print(get_password('Nikita', '12123123'))
# remember_user('Nikita', '12123123', True)
# print(try_sign_in_temp())
# delete_account('Nikita0')
# sign_off()
