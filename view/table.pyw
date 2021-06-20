import matplotlib.pyplot as plt
import re
import time
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
from tkinter.ttk import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from .business_logic.get_functions import get_user, get_path_to_database
    from .business_logic.ac_functions import sign_off
    from .models.expense import Spendings
    from .models.person import Person
    from .income_window import income_window
except ImportError:
    from business_logic.get_functions import get_user, get_path_to_database
    from business_logic.ac_functions import sign_off
    from models.expense import Spendings
    from models.person import Person
    from income_window import income_window

from login_window import check



while True:
    if get_user() == '':
        result = check()
        if not result:
            exit()

    s = Spendings(get_path_to_database())
    p = Person(get_user())

    class Tkin():
        per_cent = 0.6
        width = 475
        height = 650
        window = Tk()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
        x = int(screen_width / 2 - size[0] / 2 - height / 1.9)
        y = int(screen_height / 2 - size[1] / 2 - width / 1.9)

        window.geometry(f"{height}x{width}+{x}+{y}")

        # Создание меню, команды добавляются ниже
        menu = Menu(window)
        manage_account = Menu(menu, tearoff=0)
        manage_options = Menu(menu, tearoff=0)

        # Создание областей , что то в роде html разметки
        main_frame = Frame(window)
        wrap_cost_name_frames = Frame(main_frame)
        cost_frame = Frame(wrap_cost_name_frames)
        name_frame = Frame(wrap_cost_name_frames)
        wrap_button_frame = Frame(window)
        button_frame = Frame(wrap_button_frame)
        info_frame = Frame(wrap_button_frame)

        # Названия полей
        cost_label = Label(cost_frame, text='Cost:')
        name_label = Label(name_frame, text='Name:')

        # Поля
        cost_entry = Entry(cost_frame, width=23)

        # Кнопки
        add_button = Button(button_frame, width=23, text='Add element')
        delete_button = Button(button_frame, width=23,
                               text='Delete selected elment')

        # Информация
        query_label = Listbox(info_frame, width=68, height=30, bd=1)

        # Информация о доходах
        statistic_info = Frame(window)
        l = Label(statistic_info, text='Here could be your finance')
        statistic_info.pack(fill=Y, side='left', padx=7)

        salary_frame = LabelFrame(statistic_info, text='Income')
        names_of_income = Frame(salary_frame)
        income_data = Frame(salary_frame)

        salary_name1 = Label(names_of_income, text='Current salary: ')
        salary_amount1 = Label(income_data)

        available_frame = LabelFrame(statistic_info, text='Available')
        names_of_available = Frame(available_frame)
        available_data = Frame(available_frame)

        available_name1 = Label(names_of_available,
                                text='Available for shopping: ')
        available_amount1 = Label(available_data)

        budget_frame = LabelFrame(statistic_info, text='Budget')
        names_of_budget = Frame(budget_frame)
        budget_data = Frame(budget_frame)

        budget_name1 = Label(names_of_budget, text='Your total budget: ')
        budget_amount1 = Label(budget_data)

        investments_frame = LabelFrame(statistic_info, text='Investments')
        names_of_investments = Frame(investments_frame)
        investments_data = Frame(investments_frame)

        investment_name1 = Label(names_of_investments, text='Total investments: ')
        investment_amount1 = Label(investments_data)

        shares_frame = LabelFrame(statistic_info, text='Shares')
        names_of_shares = Frame(shares_frame)
        shares_data = Frame(shares_frame)

        shares_name1 = Label(names_of_shares, text='Total shares: ')
        shares_amount1 = Label(shares_data)

        bonds_frame = LabelFrame(statistic_info, text='Bonds')
        names_of_bonds = Frame(bonds_frame)
        bonds_data = Frame(bonds_frame)

        bonds_name1 = Label(names_of_bonds, text='Total Bonds: ')
        bonds_amount1 = Label(bonds_data)

        in_work_frame = LabelFrame(statistic_info, text='Brings income: ')
        names_of_in_work = Frame(in_work_frame)
        in_work_data = Frame(in_work_frame)

        in_work_name1 = Label(names_of_in_work, text='Per month: ')
        in_work_amount1 = Label(in_work_data)

        amount_frame = LabelFrame(statistic_info)
        names_of_amount = Frame(amount_frame)
        amount_data = Frame(amount_frame)

        # Подсчет расходов
        amount_name1 = Label(names_of_amount, text="You've spent: ")
        amount_amount1 = Label(amount_data)

        def __init__(self):
            self.window.title(s.table)
            self.window.bind("<Return>", self.add)
            self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
            # Поля
            self.name_entry = self.create_combox

            # Кнопки
            self.add_button.config(command=self.add)
            self.delete_button.config(command=self.delete)

            for i in s.show():
                self.query_label.insert(END, i)

            # Отображаю области
            self.pack(
                      [self.main_frame, self.wrap_cost_name_frames,
                      (self.cost_frame, {'side': 'left'}), self.name_frame,
                       self.wrap_button_frame, self.button_frame, self.info_frame,
                       self.amount_frame],
                       common_attribute={'pady': 3}
                     )

            # Отображаю элементы в областях
            self.name_entry(side='right')
            self.pack([(self.cost_entry, {'side': "right", 'padx': 5}),
                       (self.cost_label, {'padx': 5}),
                       (self.name_label, {'padx': 10}),
                       (self.add_button, {'side': 'left', 'padx': 3}),
                       (self.delete_button, {'padx': 3}),
                        self.query_label]
                      )

            # Добавляют команды кнопкам в раздел меню
            self.manage_account.add_command(label='Sing off', command=self.sign_off_from_account)

            self.manage_options.add_command(label='Change table', command=self.change_table)
            self.manage_options.add_command(label='Show graph', command=self.show_graph)
            self.manage_options.add_command(label='Create statistic',
                                  command=self.show_window_for_creation_income)
            self.manage_options.add_command(label='Drop statistic',
                                  command=self.delete_statistic_info_frame)

            if get_user() == 'b4914600112ba18af7798b6c1a1363728ae1d96f':
                self.manage_account.add_command(label='Debug', command=self.show_table)

            self.menu.add_cascade(label="Account", menu=self.manage_account)
            self.menu.add_cascade(label="Options", menu=self.manage_options)
            self.window.config(menu=self.menu)

            self.fill_statistic_info_frame()
            self.window.mainloop()

        #выход из текущего аккаунта
        def sign_off_from_account(self):
            s.path = ''
            sign_off()
            self.window.destroy()

        def show_table(self):
            print(get_user())
            print(get_path_to_database())
            print(s.table)

        def on_closing(self):
            exit()

        def change_table(self):
            from change_table import change_table_
            change_table_(s, self.window, self.x, self.y, self.update_lables)

        def create_combox(self, key=False, side=None):
            if not key:  # исполняется при запуске
                # ниже создается поле рядом с Name
                self.combo = Combobox(self.name_frame, width=23)
                self.combo['values'] = ('Shop', 'Medicine','Wrong stuff', 'Bus',
                                        'Monthly payments', 'Games',
                                        'Apps', 'Other')
                self.combo.current(0)  # установите вариант по умолчанию
                self.combo.pack(side=side)  # упаковываем по правой стороне от Name
            else:  # нужен чтобы сразу получить значение при  нажатии на add
                return self.combo.get()

        #  создание диалогового окна с информацие о доходах
        def show_window_for_creation_income(self):
            income_window(p, self.fill_statistic_info_frame, self.pack)

        def fill_statistic_info_frame(self):
            def _spesial_pack(iter_len_3):
                one, two, three = iter_len_3
                one.pack({'anchor':'w', 'fill':X})
                two.pack({'side': 'right'})
                three.pack({'anchor':'w'})

            all_funds = p.pull_all()
            if all_funds is None:
                self.l.pack()
                return
            # Фрейм с подсчетом трат за месяц и его лейблы
            self.amount_frame.pack(side='bottom', pady=5, fill=X)
            self.amount_data.pack(side='right')
            self.names_of_amount.pack(anchor='w')
            self.amount_amount1.config(text=s.addition())
            self.amount_amount1.pack()
            self.amount_name1.pack()

            #Фрем с зарпоатой и доступными средствами
            if all_funds[0] != 0:
                _spesial_pack((self.salary_frame, self.income_data,
                               self.names_of_income))
                _spesial_pack((self.available_frame, self.available_data,
                               self.names_of_available))
            #Фремы с инвестициями
            if all_funds[1] != 0:
                _spesial_pack((self.investments_frame, self.investments_data,
                               self.names_of_investments))
            #Фремы с акциями
            if all_funds[3] != 0:
                _spesial_pack((self.shares_frame, self.shares_data,
                               self.names_of_shares))
            #Фремы с облигациями
            if all_funds[5] != 0:
                _spesial_pack((self.bonds_frame, self.bonds_data,
                               self.names_of_bonds))
            #Фремы с общим бюджетом
            if all_funds[7] != 0:
                _spesial_pack((self.budget_frame, self.budget_data,
                               self.names_of_budget))
            #Фремы с приносящими доход средствами
            if all_funds[8] != 0:
                _spesial_pack((self.in_work_frame, self.in_work_data,
                               self.names_of_in_work))

            # Добавление цифр в подходящие лейблы, индексация согласно индексам в классе Person
            self.salary_amount1.config(text = f'{all_funds[0]} руб.')
            self.investment_amount1.config(text = f'{all_funds[1]} руб.')
            self.shares_amount1.config(text = f'{all_funds[3]} руб.')
            self.bonds_amount1.config(text = f'{all_funds[5]} руб.')
            self.budget_amount1.config(text = f'{all_funds[7]} руб.')
            self.in_work_amount1.config(text = f'{all_funds[8]} руб.')

            # self.per_cent это процент, та часть зарплаты, которую можно тратить
            # из этой части вычиется уже потраченная сумма s.addition()
            self.update_availab_label()


            # Упаковка лейблов на свои места
            self.pack([self.salary_amount1, self.salary_name1,
                       self.investment_amount1, self.investment_name1,
                       self.shares_amount1, self.shares_name1,
                       self.bonds_amount1, self.bonds_name1,
                       self.budget_name1, self.budget_amount1,
                       self.available_amount1, self.available_name1,
                       self.in_work_amount1, self.in_work_name1], {'pady': 3})
            # Удаление надписи о стат поле
            self.l.pack_forget()

        def delete_statistic_info_frame(self):
            # Забываю все главные фреймы стат поля
            self.salary_frame.pack_forget()
            self.investments_frame.pack_forget()
            self.shares_frame.pack_forget()
            self.bonds_frame.pack_forget()
            self.budget_frame.pack_forget()
            self.available_frame.pack_forget()
            self.in_work_frame.pack_forget()
            p.drop_info()

        def pack(self, iter, common_attribute=None):
            # Упаковщик для множества элементов tkinter, в виде атрибутов принимает словарь
            # также можно назначить уникальные атрибуты для отдельных элементов
            #  (x, {attrib})
            if common_attribute is None:
                for elem in iter:
                    try:
                        internal_elem, attrib = elem
                        internal_elem.pack(attrib)
                    except Exception as e:
                        # print(e)
                        elem.pack()
            else:
                for elem in iter:
                    try:
                        internal_elem, attrib = elem
                        attrib.update(common_attribute)
                        internal_elem.pack(attrib)
                    except:
                        elem.pack(common_attribute)

        def count(self):
            self.amount_amount1.config(text=s.addition())

        def add(self, event=None):
            # availab = p.pull_all()[0]*self.per_cent-s.addition()
            get_cost = self.cost_entry.get()
            if not get_cost.isdigit():
                self.cost_entry.focus_set()
                return mb.showerror("Error", "Cost must be digit")

            # Важное поле, которое не даёт ввести сумму большую чем availab
            # if availab - float(get_cost) < 0:
                # return mb.showerror("Wow wow", f"You can't spend more than {availab} rub.")

            # нет смысла ставить 0 в цене
            if get_cost == '0':
                return mb.showerror("Error", "It's absolutely useless")

            get_name = self.create_combox(key=True)
            len_name = len(get_name)
            #Ограничение названия в предел от 2 до 25 букв
            if len_name < 2 or len_name > 25:
                return mb.showerror("Error", "Name must contain from 2 to 25 letters")
            else:
                for i in get_name.split():
                    # проверка на буквы
                    if not i.isalpha():
                        return mb.showerror("Error", "Name must be alphabetical")
                    else:
                        pass

            #  очищаем поле с расходами
            self.cost_entry.delete(0, END)
            #  добавляем данные в таблицу
            s.add_things(get_cost, get_name)
            #  обновляем поля
            self.update_lables()

        def update_availab_label(self):
            try:
                self.available_amount1.config(text = f'{p.pull_all()[0]*self.per_cent-s.addition()} руб.')
            except TypeError:
                #  вероятно пользователь не установил зарплату
                pass

        def update_lables(self):
            self.show()
            self.count()
            self.update_availab_label()

        def show_graph(self):
            # показывает круговую диаграмму
            all_sutff = s.show() # получаю все строки из таблицы
            all_cost_and_names = s.pull_cost_name_amount(sort=True) # получаю список со стоимостю и именем

            values = list(all_cost_and_names.values())
            total = sum(values)
            def make_labes(dict_):
                ll = ['{0} {1} руб. {2:.2f}%'.format(x, int(y), (int(y)/total*100)) for x,y in dict_.items()]
                return ll

            fig2, ax1 = plt.subplots(figsize=(9, 5))
            ax1.pie(values, wedgeprops=dict(width=0.6), shadow=True)
            plt.legend(labels=make_labes(all_cost_and_names), bbox_to_anchor=[0.09, 1.])
            plt.show()

        def delete(self):
            del_lst = self.query_label.curselection()
            try:
                get_string = self.query_label.get(del_lst[0])
                answer = mb.askyesno(title='Confirm', message=f'Delete     {get_string} ?')
                if answer is True:
                    pattern = re.findall("ID:\d*", get_string)
                    s.del_things1(pattern[0][3:]) # по сути достаю цифру из листа с ["id:1"]  индексирую и нарезаю на "id:1"[3:] --> 1
                else:
                    pass
            except:
                pass

            self.update_lables()
        #
        def show(self):
            self.query_label.delete(0, END)
            for i in s.show():
                self.query_label.insert(ANCHOR, i)
            self.query_label.pack()

    t = Tkin()
