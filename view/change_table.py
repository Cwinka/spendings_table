from tkinter import *

def change_table_(s, window, x, y, update_lables):
    def choose(event=None):
        # смотрим на выбранный элемент
        chosen_table = query_label.curselection()
        get_string = query_label.get(chosen_table[0])  # выбираем его
        s.table = get_string  # изменяем переменную класса
        window.title(s.table)  # обновляем title таблицы
        update_lables()

    t = Toplevel()
    t.geometry(f'200x200+{x-210}+{y}')
    t.wm_title("Tables")
    query_label = Listbox(t, width=60, height=11)  # список
    query_label.bind('<Double-Button-1>', choose)  # Двойной щелчок мыши
    # заполняем список именами таблиц из экземпляра класса
    for i in reversed(s.get_tables_names()):
        query_label.insert(END, i)
    # кнопка выбора
    button_choose = Button(t, text='Choose table')
    button_choose.pack(side="bottom")  # отображение кнопки

    query_label.pack()
    t.mainloop()
