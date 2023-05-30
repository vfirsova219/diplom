import psycopg2
import tkinter as tk
from tkinter import ttk
import config
from tkinter import *

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='dipdb', user='postgres', password='123456789', host='localhost')
    print('Подключение к БД выполнено успешно!')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('При попытке подключения к БД возникла ошибка!')

# получение объекта курсора
cursor = conn.cursor()

def create_frame():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

    try:
        cursor.execute("SELECT userid, name FROM user_info ORDER BY points DESC")
        people = cursor.fetchall()

        # определяем столбцы
        columns = ("userid", "name")
 
        tree = ttk.Treeview(columns=columns, show="headings")
        #tree.pack()
        tree.grid(row=0, column=0, sticky="nsew")
 
        # определяем заголовки
        tree.heading("userid", text="Ид пользователя", anchor=W)
        tree.heading("name", text="Имя", anchor=W)
 
        tree.column("#1", stretch=NO, width=100)
        tree.column("#2", stretch=NO, width=280)
 
        # добавляем данные
        for person in people:
            tree.insert("", END, values=person)
 
        # добавляем вертикальную прокрутку
        scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

    except Exception as error:
        print("Ошибка при работе с PostgreSQL", error)

    # возвращаем фрейм из функции
    return frame

def start_black_game():
    window.destroy()
    update_allgame()
    execfile("start_black.pyw")

def start_white_game():
    window.destroy()
    update_allgame()
    execfile("start_white.pyw")

def update_allgame(): #обавляем к общему кол-ву партий +1
    sql = "SELECT allgame FROM user_info where userid = %s"
    cursor.execute(sql, (config.id, )) #выполняем запрос к бд с переменными
    allgame = cursor.fetchone() #записываем результат
    allgameBefore = allgame[0]
    print(allgameBefore)
    allgameAfter = allgameBefore + 1
    print(allgameAfter)
    cursor.execute("UPDATE user_info SET allgame =%s WHERE userid =%s", (allgameAfter, config.id))
    conn.commit()

window = Tk()
window.title("Фирсова Владислава 219")
window.geometry('400x400')

create_frame()

window.option_add("*tearOff", FALSE)

main_menu = Menu()
game_menu = Menu()
game_menu.add_command(label="Играть за черные", command=start_black_game)
game_menu.add_command(label="Играть за белые", command=start_white_game)

main_menu.add_cascade(label="Игра", menu=game_menu)
main_menu.add_cascade(label="Общий рейтинг")

window.config(menu=main_menu)

window.mainloop()