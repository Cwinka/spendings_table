import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from .models.person import Person
except ImportError:
    from models.person import Person
from typing import Callable
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import *

def income_window(person: Person, fill_func: Callable, packer: Callable) -> None:
    def get(iter):
        result = [elem.get() for elem in iter]
        return result
    #  выравнивание и запись в базу

    def pull_all_entries_income_window() -> list:
        data_about_money = get([salary_entry, investment_entry,
                                     investment_entry2, shares_entry,
                                     shares_entry2, bonds_entry,
                                     bonds_entry2, total_entry,
                                     brings_income_entry])
        return data_about_money

    def create_dict_with_income_data(data_about_money: list) -> dict:
        my_list2 = ['salary', 'investment', 'invest_per', 'shares',
                    'shares_per', 'bonds', 'bonds_per',
                    'total_money', 'in_work']
        my_dict = {}
        for i in range(len(data_about_money)):
            if data_about_money[i] != '':
                g = float(data_about_money[i])
                if g > 0:
                    my_dict[my_list2[i]] = g

        return my_dict

    def click() -> None:
        data_about_money = pull_all_entries_income_window()
        my_dict = create_dict_with_income_data(data_about_money)

        if len(my_dict) == 0:
            return mb.showerror("Error", 'Fill in at least one entry')

        person.add_statistic_info(my_dict)
        statictic_window.destroy()
        fill_func()

    statictic_window = Toplevel()
    statictic_window.geometry('600x400+500+200')
    # часы
    # def tick():
    #     label.after(5000, tick)
    #     label['text'] = time.strftime('%H:%M:%S')
    #
    # label = Label(statictic_window, font='sans 20')
    # label.pack()
    # label.after_idle(tick)

    main_frame = Frame(statictic_window)

    title_frame =  Frame(main_frame)
    salary_frame = Frame(main_frame)
    investment_frame = Frame(main_frame)
    shares_frame = Frame(main_frame)
    bonds_frame = Frame(main_frame)
    total_money_frame = Frame(main_frame)
    brings_income = Frame(main_frame)

    main_frame.pack(fill=X, anchor='w', padx=10, pady=5)

    title_frame.pack(fill=X, anchor='w')
    packer([salary_frame, investment_frame, shares_frame,
               bonds_frame, total_money_frame,
               brings_income])

    title_label_per_cent = Label(title_frame, text="Persentage\nof income")

    title_label_value = Label(title_frame, text="Value")

    salary_label = Label(salary_frame, text='Current salary:')

    investment_label = Label(investment_frame, text='Investments:')

    shares_label = Label(shares_frame,
                         text='Amount of shares (their income):')

    bonds_label = Label(bonds_frame,
                        text='Amount of bonds (their income):')

    total_label = Label(total_money_frame,
                        text='Total of your funds (include shares,bonds, investments):')

    brings_income_label = Label(brings_income,
                                text='Amount of income per month (exclude salary):')

    salary_entry = Entry(salary_frame, )
    investment_entry = Entry(investment_frame, )
    investment_entry2 = Entry(investment_frame, )
    shares_entry = Entry(shares_frame, )
    shares_entry2 = Entry(shares_frame, )
    bonds_entry = Entry(bonds_frame, )
    bonds_entry2 = Entry(bonds_frame, )
    total_entry = Entry(total_money_frame, )
    brings_income_entry = Entry(brings_income, )

    title_label_per_cent.pack(side='right')
    title_label_value.pack(side='right', padx=35)

    packer([salary_label, investment_label, shares_label, bonds_label,
               total_label, brings_income_label])

    packer([investment_entry2, shares_entry2, bonds_entry2])

    packer([salary_entry, total_entry, brings_income_entry])

    packer([investment_entry, shares_entry, bonds_entry])


    okButton = Button(statictic_window, text="OK", width=10, command=click)
    okButton.pack()

    statictic_window.mainloop()
