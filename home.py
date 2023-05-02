import tkinter as tk
from tkinter import *
from tkinter.messagebox import askyesno
from subprocess import call
window = Tk()
window.title("Фирсова Владислава 219")
window.geometry('1000x900')
window.option_add("*tearOff", FALSE)

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