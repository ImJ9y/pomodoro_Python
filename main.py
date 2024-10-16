import time
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_button_click():
    window.after_cancel(timer)
    #Title label
    title_label.config(text="Timer")
    #Timer label
    canvas.itemconfig(timer_text, text= "00:00")
    #Check_marks
    complete.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button_click():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #1st/3rd/5th/7th reps
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text= "Break", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_button_click()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        complete.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg = YELLOW)

canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_image)
timer_text = canvas.create_text(103, 130, text = "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1) #grid and pack can't use together

#Labels
title_label = Label(text="Timer", bg = YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.config(padx=0, pady=5, fg = GREEN)
title_label.grid(column = 1, row=0)

complete = Label(text = "", bg = YELLOW)
complete.config(padx=0, pady=5)
complete.grid(column = 1, row=3)

#Buttons
start_button = Button(text="Start", command=start_button_click)
start_button.config(padx=0, pady=5, fg = "black", highlightthickness=0, highlightbackground = YELLOW)
start_button.grid(column = 0, row = 2)

reset_button = Button(text="Reset", command=reset_button_click)
reset_button.config(padx=0, pady=5, fg = "black", highlightthickness=0, highlightbackground = YELLOW)
reset_button.grid(column = 2, row = 2)


window.mainloop()