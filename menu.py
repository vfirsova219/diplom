import psycopg2 #необходимо для подключения к бд
import config #необходимо для импорта переменной
import tkinter as tk #необходимо для отображения интерфейса
from tkinter import *
from tkinter import font
from tkinter.messagebox import showwarning

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
        window.destroy()
        cursor.execute(sql, (username, password,)) #выполняем запрос к бд с переменными
        res = cursor.fetchone() #записываем результат
        config.id = res[0] #обрабатываем кортеж. забираем значение столбца id
        print(config.id)
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")
        execfile("home.py") #открываем личный кабинет пользователя
    except Exception as error:
        open_warning()
        print("Ошибка при работе с PostgreSQL", error)
        

window = Tk()
window.title("Фирсова Владислава 219")
window.geometry('400x400')

# Создаем canvas с фоновым изображением
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

bg_image = tk.PhotoImage(file="mainwindow.png")
canvas.create_image(0, 0, image=bg_image, anchor="nw")

font1 = font.Font(family= "Copperplate Gothic Bold", size=16)
font2 = font.Font(family= "Copperplate Gothic Bold", size=11)

main_label = tk.Label(canvas, text='Authorization', font=font1, background="#cafcfc")
main_label.place(x=25, y=30)

username_label = tk.Label(canvas, text='Username', font=font2, background="#dbfeff")
username_label.place(x=20, y=85)

username_entry = tk.Entry(canvas, bg='#fff', fg='#444', width=30)
username_entry.place(x=20, y=110)

password_label = tk.Label(canvas, text='Password', font=font2, background="#dbfeff")
password_label.place(x=20, y=150)

password_entry = tk.Entry(canvas, bg='#fff', fg='#444', width=30)
password_entry.place(x=20, y=175)

send_btn = tk.Button(canvas, text='Sign in', command=clicked, font=font2)
send_btn.place(x=130, y=220)

def open_warning():
    showwarning(title="Предупреждение", message="Данные пользователя введены неверно или пользователь не зарегистрирован")
window.mainloop()