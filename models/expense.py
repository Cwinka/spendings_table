import datetime
import sqlite3
from collections import OrderedDict, defaultdict
from typing import NoReturn, Union

class Spendings:
    #  Определяет текущую дату
    curent_date = datetime.datetime.today()
    #  Выводим текущий месяц,язык US
    curent_month = curent_date.strftime('%B_%Y')
    #  Создаём название для таблицы
    curent_table = 'spendings_of_' + curent_month


    def __init__(self, path: str):
        #  Поключаемся к базе
        self.path = path
        self.conn = sqlite3.connect(self.path)
        #  Устанавливаем курсор
        self.c = self.conn.cursor()
        #  Ссылка на текущее название таблицы. Не менять!
        #  Используется в других функциях
        self.table = self.curent_table

        self.create_table_if_not_exists()

        #  получаем обновлённый список таблиц, если верх отработалработал
        with self.conn:
            sql = 'SELECT NAME FROM sqlite_master WHERE type = "table"'
            self.c.execute(sql)
            #  Переменная используется в других функциях (также в table_spd)
            self.tables_names = [x[0] for x in self.c.fetchall()
                                 if x[0] != 'sqlite_sequence']

    #  получить сисок таблиц
    def get_tables_names(self) -> str:
        return self.tables_names

    def create_table_if_not_exists(self) -> NoReturn:
        """
         проверяем наличие текущей таблицы в списке таблиц, если не нашлось,
         то создаем новую таблицу

        """

        if not self.check_selftable_on_existing():
            #  Создаём новую таблицу, после добавления
            with self.conn:
                self.c.execute(f"""CREATE TABLE IF NOT EXISTS {self.table} (
                id integer primary key autoincrement,
                time REAL,
                cost REAL PRIMIRY KEY NOT NULL,
                name VARCHAR NOT NULL)""")

    def check_selftable_on_existing(self) -> bool:
        """
         проверяем наличие текущей таблицы в списке таблиц, если не нашлось,
         то создаем новую таблицу

        """
        self.c.execute('SELECT NAME FROM sqlite_master WHERE type = "table" ')
        tables_from_database = [x[0] for x in self.c.fetchall()
                                if x[0] != 'sqlite_sequence']
        return self.table in tables_from_database

    #  Сюда приходят данные с интерактивной панели
    def add_things(self, cost: int, name: str) -> None:
        """
        Добавляет полученные данные в таблицу пользователя

        """
        #  Вывожу дату в нужном формате
        today = self.curent_date.strftime("%Y-%m-%d %H:%M")
        #  Использую контекстный оператор with чтобы авто1матицески закрыть базу
        with self.conn:
            try:
                self.c.execute(f"INSERT INTO {self.table}(time, cost, name) \
                                VALUES (?, ?, ?)", (today, cost, name))
            except:
                print('Somethings went wrong')

    #  Сюда приходят данные с интерактивной панели
    def del_things1(self, id_from_table: str) -> None:
        """
        Удаляет элемент из таблицы пользователя

        """
        with self.conn:
            #  Делаю через блок, чтобы поймать исключение,
            #  нужно чтобы править интерактивную панель
            try:
                self.c.execute(f"DELETE FROM {self.table} WHERE id = (?)",
                               (id_from_table,))
            except:
                print('Invalid ID')

        #  функцию используется для построения круговой диаграммы
        #  получаю данные из таблицы, складываю одиноковые значения и
        #  возвращаю их
    def pull_cost_name_amount(self, sort: bool = False) -> Union[OrderedDict,\
                                                                 defaultdict]:
        """
        Возвращает OrderedDict or defaultdict с информацией о всех тратах
        пользователя, совпадающие поля суммируются

         """

        #  ниже создаю словарь, чтобы данные не повторялись,
        #  суммирую повторяющиеся
        names_costs_dict = defaultdict(int)
        for (cost, name) in self.pull_all_costs_and_names():
            names_costs_dict[name] += cost

        if sort is True:
            return OrderedDict(sorted(names_costs_dict.items(),
                                      key=lambda x: x[1]))
        else:
            return names_costs_dict

    def pull_all_costs_and_names(self) -> list:
        """
        Возвращает лист со всеми тратами типа [название: цена]

        """
        self.c.execute(f'SELECT cost, name FROM {self.table}')
        return self.c.fetchall()


        #  выводит список записей в таблицу
    def show(self) -> list:
        """
        Возвращает list с информацией о каждой
        трате пользователя
        0 - id, 1 - дата, 2 - цена, 3 - название

        """
        self.c.execute(f"SELECT * FROM {self.table}")
        record = [f"{row[2]} {row[3]}   ID:{row[0]}   {row[1]}"
                  for row in self.c.fetchall()]
        return record

        #  складывает все cost
    def addition(self) -> Union[int, float]:
        """
        Возвращает сумму поля cost, int

        """
        self.c.execute(f"SELECT cost FROM {self.table}")
        value = sum([x[0] for x in self.c.fetchall()])
        return value

# from business_logic.get_functions import get_path_xp
# s = Spendings(get_path_xp() + '256039816cda6ece251b47bddf3b1e1251d57b91.db')
# s.add_things('бла', 123)
# s.del_things1(1)
