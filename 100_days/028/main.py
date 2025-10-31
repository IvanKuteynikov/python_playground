import tkinter as tk
from math import floor
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
clock_init = "00:00"
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer, reps, clock_init
    window.after_cancel(timer)
    reps = 0
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=clock_init)
    label_check_mark.config(text='')
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    works_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Relax!", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break time!", fg=PINK)
    else:
        count_down(works_sec)
        label.config(text="Work time!", fg=GREEN)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = "0"+str(count_sec)
    if count_sec == 0:
        count_sec = "00"
    if len(str(count_min)) == 1:
        count_min = "0"+str(count_min)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        mark = ''
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        label_check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100)

label = tk.Label(text="Timer", font=(FONT_NAME, 35, 'bold'), fg=GREEN)
label.config(padx=10, pady=10)
label.grid(column=3, row=0)

canvas = tk.Canvas(width=200, height=224, highlightthickness=0)
tomato_img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
#canvas.config(bg=YELLOW)
timer_text = canvas.create_text(103, 130, text=clock_init, font=(FONT_NAME, 35, 'bold'), fill="white")
canvas.grid(column=3, row=2)

button_start = tk.Button(text="Start", highlightthickness=0, command=start, bg=YELLOW)
button_start.grid(column=0, row=4)


label_check_mark = tk.Label(font=(FONT_NAME, 35, 'bold'), fg=GREEN)
label_check_mark.grid(column=3, row=4)

button_reset = tk.Button(text="Reset", highlightthickness=0, command=reset, bg=YELLOW)
button_reset.grid(column=6, row=4)


window.mainloop()