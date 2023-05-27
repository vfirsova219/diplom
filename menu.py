import psycopg2 #необходимо для подключения к бд
import config #необходимо для импорта переменной
import tkinter as tk #необходимо для отображения интерфейса
from tkinter import *
window = Tk()
window.title("Фирсова Владислава 219")
window.geometry('1000x900')

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


def clicked(): #при нажатии на "Войти"

    username = username_entry.get() #записываем введенные пользователем данные
    password = password_entry.get()

    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='dipdb', user='postgres', password='123456789', host='localhost')
        print('Подключение к БД выполнено успешно!')
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('При попытке подключения к БД возникла ошибка!')

    # получение объекта курсора
    cursor = conn.cursor()

    sql = "SELECT id FROM users where login = %s and pass=%s"

    try:
        cursor.execute(sql, (username, password,)) #выполняем запрос к бд с переменными
        res = cursor.fetchone() #записываем результат
        config.id = res[0] #обрабатываем кортеж. забираем значение столбца id
        print(config.id)
        execfile("home.py") #открываем личный кабинет пользователя
    except Exception as error:
        print("Ошибка при работе с PostgreSQL", error)
    #finally:
        #cursor.close()
        #conn.close()
        #print("Соединение с PostgreSQL закрыто")


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