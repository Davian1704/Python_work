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
reps=0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps=0
    window.after_cancel(timer)
    tick.config(text="")
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    reps+=1
    if reps%2!=0:
        countdown(work)
        timer_label.config(text="Work",fg=GREEN)
    elif reps %8==0:
        countdown(short_break)
        timer_label.config(text="Break", fg=RED)
    else:
        countdown(long_break)
        timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    count_minutes=math.floor(count/60)
    count_seconds = int(count%60)
    if count_seconds<10:
        count_seconds=f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if int(count)>0:
        global timer
        timer=window.after(1000, countdown, count-1)
    else:
        start_timer()
        if reps%2==0:
            tick.config(text=f"{tick['text']}🗸")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=223,bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=image)
timer_text = canvas.create_text(100,130, text="00:00",font=(FONT_NAME,35,"bold"), fill = "white")

start=Button(text="Start",command=start_timer)
start.pack(anchor="s", side="left")

reset = Button(text="Reset",command=reset_timer)
reset.pack(anchor="s", side="right")

timer_label=Label(fg=GREEN,bg=YELLOW,text="Timer",font=(FONT_NAME,50,"bold"))
timer_label.pack(side=TOP)

tick = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"))
tick.pack(side=BOTTOM)
canvas.pack()


window.mainloop()
