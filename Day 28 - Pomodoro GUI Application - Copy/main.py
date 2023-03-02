from tkinter import *
import math
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

def reset_button():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text=" ")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_button():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# After 1s = 1000ms calls the Function count_down and passes the count argument to the count
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Dynamic Typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_button()
        mark = " "
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
            check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


timer_label = Label(text="Timer", bg=YELLOW, foreground=GREEN,font=("Times New Roman", 34, "bold"))
timer_label.grid(column=2, row=0)
timer_label.config(padx=10, pady=10)


left_button = Button(text="START", highlightthickness=0, command= start_button)
left_button.grid(column=1, row=5,padx=10, pady=10)
left_button.config(padx=10, pady=10)


right_button = Button(text="RESET", highlightthickness=0, command= reset_button)
right_button.grid(column=3, row=5,padx=10, pady=10)
right_button.config(padx=10, pady=10)


check_marks = Label(fg=GREEN, bg=YELLOW, font=35)
check_marks.grid(column=2, row=6)


window.mainloop()