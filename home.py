import psycopg2
import tkinter as tk
from tkinter import ttk
import config
from tkinter import *
from subprocess import call

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

def create_frame():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10], width=400, height=400)        

    try:
        sql = "SELECT name, allgame, wingame, failgame, points FROM user_info where userid = %s"
        cursor.execute(sql, (config.id, ))
        name, allgame, wingame, failgame, points = cursor.fetchone()

        username_label = tk.Label(canvas, text=name, font = font1, background="#cafcfc")
        username_label.place(x=25, y=20)

        allgameT_label = tk.Label(canvas, text="Общее количество партий:", background="#cafcfc", width=30)
        allgameT_label.place(x=25, y=60)
        allgame_label = tk.Label(canvas, text=allgame, background="#cafcfc", width=20)
        allgame_label.place(x=230, y=60)

        wingameT_label = tk.Label(canvas, text="Количество выигранных партий:", background="#cafcfc", width=30)
        wingameT_label.place(x=25, y=90)
        wingame_label = tk.Label(canvas, text=wingame, background="#cafcfc", width=20)
        wingame_label.place(x=230, y=90)

        failgameT_label = tk.Label(canvas, text="Количество проигранных пратий:", background="#cafcfc", width=30)
        failgameT_label.place(x=25, y=120)
        failgame_label = tk.Label(canvas, text=failgame, background="#cafcfc", width=20)
        failgame_label.place(x=230, y=120)

        pointsT_label = tk.Label(canvas, text="Очки:", background="#cafcfc", width=30)
        pointsT_label.place(x=25, y=150)
        points_label = tk.Label(canvas, text=points, background="#cafcfc", width=20)
        points_label.place(x=230, y=150)

    except Exception as error:
        print("Ошибка при работе с PostgreSQL", error)
    
    frame.pack()
    return frame

def start_black_game():
    window.destroy()
    update_allgame()
    execfile("start_black.pyw")

def start_white_game():
    window.destroy()
    update_allgame()
    execfile("start_white.pyw")

def go_progress():
    window.destroy()
    execfile("allprogress.py")

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

font1 = font.Font(family= "Copperplate Gothic Bold", size=14)
font2 = font.Font(family= "Copperplate Gothic Bold", size=11)

canvas = Canvas(window, width=400, height=400)
canvas.pack()

bg_image = PhotoImage(file="homewindow.png")
canvas.create_image(0, 0, image=bg_image, anchor="nw")

create_frame()

window.option_add("*tearOff", FALSE)

main_menu = Menu()
game_menu = Menu()
game_menu.add_command(label="Играть за черные", command=start_black_game)
game_menu.add_command(label="Играть за белые", command=start_white_game)

main_menu.add_cascade(label="Игра", menu=game_menu)
main_menu.add_cascade(label="Общий рейтинг", command=go_progress)

window.config(menu=main_menu)


window.mainloop()