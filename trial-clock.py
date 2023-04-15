import tkinter as tk
import math
import time

class AnalogClock:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()
        self.draw_clock()
        self.update_clock()

    def draw_clock(self):
        self.canvas.create_oval(50, 50, 250, 250, width=2)
        for i in range(12):
            x1 = 150 + math.cos(math.radians(i * 30)) * 100
            y1 = 150 - math.sin(math.radians(i * 30)) * 100
            x2 = 150 + math.cos(math.radians(i * 30)) * 90
            y2 = 150 - math.sin(math.radians(i * 30)) * 90
            self.canvas.create_line(x1, y1, x2, y2, width=2)

        self.hour_hand = self.canvas.create_line(150, 150, 150, 100, width=4, fill='red')
        self.minute_hand = self.canvas.create_line(150, 150, 150, 50, width=3, fill='blue')
        self.second_hand = self.canvas.create_line(150, 150, 150, 25, width=1, fill='green')

    def update_clock(self):
        now = time.localtime()
        hour = now.tm_hour % 12
        minute = now.tm_min
        second = now.tm_sec

        hour_angle = (hour * 30) + (minute * 0.5)
        minute_angle = minute * 6
        second_angle = second * 6

        self.canvas.coords(self.hour_hand, 150, 150, 150 + math.cos(math.radians(hour_angle)) * 60, 150 - math.sin(math.radians(hour_angle)) * 60)
        self.canvas.coords(self.minute_hand, 150, 150, 150 + math.cos(math.radians(minute_angle)) * 80, 150 - math.sin(math.radians(minute_angle)) * 80)
        self.canvas.coords(self.second_hand, 150, 150, 150 + math.cos(math.radians(second_angle)) * 90, 150 - math.sin(math.radians(second_angle)) * 90)

        self.master.after(1000, self.update_clock)

root = tk.Tk()
clock = AnalogClock(root)
root.mainloop()
