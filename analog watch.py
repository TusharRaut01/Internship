import tkinter as ui
import time
import math

window = ui.Tk()
window.geometry('500x500')

def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # seconds line
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(second_hand, center_x, center_y, seconds_x, seconds_y)

    # minutes line
    minutes_x =  minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # hours line
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    window.after(1000, update_clock)

# canvas
canvas = ui.Canvas(window, width=500, height=500, bg="white")
canvas.pack(expand=True, fill="both")

# background
bg = ui.PhotoImage(file="C:/Users/rautr/OneDrive/Pictures/analog500x500.png")
canvas.create_image(250, 250, image=bg)

# clock hands
center_x = 250
center_y = 250
seconds_hand_len = 150
minutes_hand_len = 130
hours_hand_len = 100

# clock hands
# second hands
second_hand = canvas.create_line(250, 250, 250 + seconds_hand_len, 250 + seconds_hand_len, width=3, fill="red")
# minutes hands
minutes_hand = canvas.create_line(250, 250, 250 + minutes_hand_len, 250 + seconds_hand_len, width=4, fill="#a594e2")
# hours hands
hours_hand = canvas.create_line(250, 250, 250 + hours_hand_len, 250 + seconds_hand_len, width=5, fill="#a594e2")

update_clock()
window.mainloop()