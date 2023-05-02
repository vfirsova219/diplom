import tkinter as tk
from tkinter import *
window = Tk()
window.title("Фирсова Владислава 219")
window.geometry('1000x900')

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

def clicked():

    username = username_entry.get()
    password = password_entry.get()


main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
main_label.pack()

username_label = Label(window, text='Имя пользователя', font=label_font , **base_padding)
username_label.pack()

username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

password_label = Label(window, text='Пароль', font=label_font , **base_padding)
password_label.pack()

password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()

send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)

window.mainloop()