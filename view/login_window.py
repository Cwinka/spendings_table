from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from .business_logic.ac_functions import try_sign_in, try_sign_in_temp, try_register
    from .business_logic.security_functions import get_password
    from .business_logic.get_functions import *
except ImportError:
    from business_logic.ac_functions import try_sign_in, try_sign_in_temp, try_register, remember_user
    from business_logic.security_functions import get_password, get_login
    from business_logic.get_functions import _put_user


def check():
    result = try_sign_in_temp()
    if result:
        return result

    def on_closing():
        exit()

    registered = None
    login = None
    password = None
    window = Tk()
    height = 195
    width = 360
    #  -------------------------Start of apositioning
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = int(screen_width / 2 - size[0] / 2 - height / 2)
    y = int(screen_height / 2 - size[1] / 2 - width / 2)
    #  ------------------------- End of a positioning
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.protocol("WM_DELETE_WINDOW", on_closing)
    left_main = Frame(window)
    main_frame = Frame(window)
    right_main = Frame(window)

    loggin_lable = Label(main_frame, text='Loggin')
    loggin_entry = Entry(main_frame, width=25)
    passp_lable = Label(main_frame, text='Password')
    passp_entry = Entry(main_frame, width=25)

    state_of_remember = IntVar()
    remember_me_label = Label(main_frame, text='Remember me')
    remember_me_checkbox = Checkbutton(main_frame, variable=state_of_remember, onvalue=1, offvalue=0)

    #  Start action after CLICK SIGN UP button ---------------
    def do():
        window_child = Toplevel()
        window_child.title('Sign up')
        window_child.geometry(f'300x300+{x+30}+{y-10}')

        left_main = Frame(window_child)
        main_frame = Frame(window_child)
        right_main = Frame(window_child)

        name_lable = Label(main_frame, text='Name of your account')
        name_entry = Entry(main_frame, width=25)
        passp_lable = Label(main_frame, text='Password')
        passp_entry = Entry(main_frame, width=25)
        left_main.pack(side='left')
        main_frame.pack()
        right_main.pack(side='right')


        def try_sign_up():
            login = name_entry.get()
            password = passp_entry.get()

            if len(password) < 5:
                mb.showerror('Error', 'Passport must be at least 5 simbols long!')
                window_child.focus_set()
                return
            registered = try_register(login, password)
            if registered:
                window_child.destroy()
                mb.showinfo('Success', f"You're successfuly registered as \"{login} with password {password}\"\n\nNow you can sign in!", parent=window)
            else:
                mb.showinfo('Failed', f"This name is unavailable \"{login}\"\n\nTry another one!", parent=window)
                window_child.focus_set()

        sign_up_lable = Button(main_frame, text='Sign up', command=try_sign_up)


        name_lable.pack(anchor='w', pady=2)
        name_entry.pack()
        passp_lable.pack(anchor='w')
        passp_entry.pack()
        sign_up_lable.pack(pady=7)
        window_child.mainloop()

    sign_up_lable = Button(right_main, text='Sign up', command=do)
    #  End action ----------------------

    #  Start action after CLICK OK button--------------------
    def pull():
        local_loging = loggin_entry.get()
        local_password = passp_entry.get()
        if not local_loging:
            loggin_entry.config()
            loggin_entry.focus_set()
            return mb.showerror("Error", "Enter loggin")
        if not local_password:
            passp_entry.config()
            passp_entry.focus_set()
            return mb.showerror("Error", "Enter password")

        is_correct = try_sign_in(local_loging, local_password)

        if is_correct:
            nonlocal login, password
            login = local_loging
            password = local_password
            window.destroy()
            return
        else:
            return mb.showerror("Incorrect logging or password",
                                "Incorrect logging or password")
    #  End action------------------------

    button_ok = Button(main_frame, width=18, text='Ok', command=pull)

    left_main.pack(side='left')
    main_frame.pack()
    right_main.pack(side='right')

    loggin_lable.pack(anchor='w')
    loggin_entry.pack()
    passp_lable.pack(anchor='w')
    passp_entry.pack()
    button_ok.pack(pady=19)
    sign_up_lable.pack(anchor='ne', padx=2, pady=2)
    remember_me_checkbox.pack(side='left')
    remember_me_label.pack()

    window.mainloop()
    remember_user(login, password, state_of_remember.get())
    return login, password
# check()
