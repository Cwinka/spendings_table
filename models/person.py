# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sqlite3
from typing import Dict, Union, NoReturn
import business_logic.get_functions
import business_logic.security_functions

class Person:
    #  Поключаемся к базе
    conn = sqlite3.connect(business_logic.get_functions.get_path_ac())
    c = conn.cursor()  # Устанавливаем курсор
    table_name = business_logic.get_functions.get_tb_ac()

    def __init__(self, user: str):
        """
        Устанавливаем текущего пользователя

        """
        self.user = user

    def drop_info(self) -> None:
        """
        Удаляем информацию о доходах

        """
        entries = ['salary', 'investment', 'invest_per', 'shares','shares_per',
                   'bonds', 'bonds_per', 'total_money', 'in_work']
        with self.conn:
            for item in entries:
                self.c.execute("UPDATE {0} SET {1} = 0 \
                                WHERE name='{2}'".format(self.table_name,
                                                         item, self.user))


    #  добавляем информацию о доходах (итеративно)
    def add_statistic_info(self, info_income_dict: Dict[str, Union[int, float]]) -> None:
        """
        Добавляет информацию о доходах

        """
        with self.conn:
            for item in info_income_dict.items():
                title = item[0]
                value = item[1]
                self.c.execute("UPDATE {0} SET {1} = {2} \
                                WHERE name='{3}'".format(self.table_name,
                                                         title, value, self.user))

    def _show(self) -> None:
        """
        Показывает всю информацию о пользователе из базы данных с
        аккаунтами

        """
        sql = f"SELECT * FROM {self.table_name} WHERE name='{self.user}'"
        self.c.execute(sql)
        print(self.c.fetchall())

    def _f(self) -> None:
        self.c.execute(f'PRAGMA table_info({self.table_name})')
        print(self.c.fetchall())


    def pull_all(self) -> Union[list, None]:
        """
        Возвращает информацию о доходах, если не установлено ни одного
        поля то None иначе list

        """
        self.c.execute('SELECT * FROM {0} WHERE name="{1}"'.format(self.table_name, self.user))
        try:
            response = self.c.fetchall()[0][3:]
        except IndexError:
            return None
            
        if sum(response) > 0:
            return response
        else:
            return None

# p = Person('Nikita2')
# p.show()
# p.add_statistic_info({'salary': 1232, 'bonds': 214314}, 'Nikita3')
# p.show()
# p.drop_info('Nikita3')
# p.show()
# print(p.pull_all())
