import psycopg2
import tkinter as tk
from tkinter import ttk
import menu
import config
from tkinter import *
from tkinter.messagebox import askyesno
from subprocess import call
window = Tk()
window.title("Фирсова Владислава 219")
window.geometry('1000x900')
window.option_add("*tearOff", FALSE)

print(config.id)

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='dipdb', user='postgres', password='123456789', host='localhost')
    print('Подключение к БД выполнено успешно!')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('При попытке подключения к БД возникла ошибка!')

# получение объекта курсора
cursor = conn.cursor()

sql = "SELECT name, allgame, wingame, failgame, points FROM user_info where userid = %s"

try:
    cursor.execute(sql, (config.id, )) #выполняем запрос к бд с переменными
    name, allgame, wingame, failgame, points = cursor.fetchone() #записываем результат
    username_label = Label(window, text=name, font=label_font , **base_padding)
    username_label.pack()

    # определяем данные для отображения
    info = [(allgame, wingame, failgame, points)]
 
    # определяем столбцы
    columns = ("allgame", "wingame", "failgame", "points")
 
    tree = ttk.Treeview(columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=1)
 
    # определяем заголовки
    tree.heading("allgame", text="Общее количество партий")
    tree.heading("wingame", text="Количество выигранных партий")
    tree.heading("failgame", text="Количество проигранных пратий")
    tree.heading("points", text="Очки")
 
    # добавляем данные
    for person in info:
        tree.insert("", END, values=person)
except Exception as error:
    print("Ошибка при работе с PostgreSQL", error)


def exit_click():
    result = askyesno(title="Подтвержение операции", message="Вы уверены, что хотите выйти?")
    if result:
        quit()

def start_game():
    call(["python","main.py"])

main_menu = Menu()
game_menu = Menu()

main_menu.add_cascade(label="Игра", command=start_game)
main_menu.add_cascade(label="Общий рейтинг")
main_menu.add_cascade(label="Выход", command=exit_click)

window.config(menu=main_menu)

window.mainloop()