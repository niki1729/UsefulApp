"Press Restart at the end"
"Press s to slow done"
"Press a to accelerate"
"Press p to pause"
"At the end the mean of all runs in this session is displayed,when you close the window, you lose all progress"
"Have FUN"

from tkinter import *
from time import *
from random import *
from math import sqrt

width = 1080
height = 1980
number_balls = 400
hit = False
last = None


def collision(b1, b2):
    distance = sqrt((b1.x_p - b2.x_p) ** 2 + (b1.y_p - b2.y_p) ** 2)
    return distance <= b1.r + b2.r


def moving(liste, n):
    all_stoped = True
    if True:  # not c.pause:
        for i in range(n):
            if liste[i].vx != 0 and liste[i].vy != 0:
                all_stoped = False

    return not all_stoped


class Control:
    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(width) + "x" + str(height))
        self.pause = False
        self.canvas = Canvas(self.window, width=width, height=height)
        self.canvas.place(x=0, y=0)
        self.start_time = time()
        self.liste_times = []

        self.slowdown = False
        self.accelerate = False

    def start(self, _, button, text):
        if not button is None:
            button.destroy()
            text.destroy()
            self.canvas.delete("all")
            self.canvas.unbind('<Return>')
            self.window.unbind('<Return>')
        self.bc = BallControl()
        print(self.bc.ball_liste)

    def restart(self, _):
        endtime = time()
        delta = endtime - self.start_time
        self.liste_times.append(float(round(delta, 2)))
        delta_text = Label(self.canvas, text=str(round(delta, 2)) + "\n" + "Ø: " + str(
            round(sum(self.liste_times) / len(self.liste_times), 2)), font=("Ariel", 30))
        print(self.liste_times)
        delta_text.place(x=width / 2, y=height / 2, anchor=N)
        self.start_time = time()
        restart_b = Button(self.canvas, text="restart", bg="red", command=lambda: self.start("", restart_b, delta_text))
        restart_b.place(x=width / 2, y=height / 5, anchor=S)

        self.window.bind('<Return>', lambda event, r=restart_b, d=delta_text: self.start(event, r, d))


class Ball:
    def __init__(self, canvas, radius, color):
        self.color = color
        self.canvas = canvas
        self.r = radius
        self.x_p = randint(self.r * 2, width - self.r * 2)
        self.y_p = randint(self.r * 2, height - self.r * 2)
        self.vx = randrange(-3, 3, 2) * (10 - self.r / 3)
        self.vy = randrange(-3, 3, 2) * (10 - self.r / 3)
        self.ball = self.canvas.create_oval(self.x_p - self.r, self.y_p - self.r, self.x_p + self.r, self.y_p + self.r,
                                            fill=self.color)

    def move(self):
        self.canvas.delete(self.ball)
        if self.x_p + self.vx <= self.r or self.x_p + self.vx >= width - self.r:
            self.vx = -self.vx + randint(-1, 1)
        if self.y_p + self.vy <= self.r or self.y_p + self.vy >= height - self.r:
            self.vy = -self.vy + randint(-1, 1)
        self.x_p = self.x_p + self.vx
        self.y_p = self.y_p + self.vy
        self.ball = self.canvas.create_oval(self.x_p - self.r, self.y_p - self.r, self.x_p + self.r, self.y_p + self.r,
                                            fill=self.color)


class BallControl:
    def __init__(self):
        c.window.bind('<KeyPress>', lambda s="s": self.effects(s))
        self.ball_liste = []
        for i in range(number_balls):
            self.ball_liste.append(Ball(c.canvas, randint(2, 5), "#" + str(randint(111111, 999999))))

        self.liste_speed = []
        self.state_pause = False

        self.restart = False

        while moving(self.ball_liste, number_balls):
            for n in range(number_balls):
                for m in range(number_balls):
                    if n != m:
                        if collision(self.ball_liste[n], self.ball_liste[m]):
                            self.ball_liste[n].vx = 0
                            self.ball_liste[n].vy = 0
                            self.ball_liste[m].vx = 0
                            self.ball_liste[m].vy = 0

            sleep(0.05)
            for i in range(number_balls):
                self.ball_liste[i].move()
            c.window.update()

        if not self.restart:
            c.restart(None)

    def effects(self, event):
        if event.char == "a":
            print(event.char)

            self.accelerate()

        if event.char == "s":
            print(event.char)
            self.slowdone()

        if event.char == "r":
            self.restart = True
            for i in range(number_balls):
                self.ball_liste[i].vx, self.ball_liste[i].vy = 0, 0
            c.restart(None)

        if event.char == "p":
            self.pause()

    def accelerate(self):
        for i in range(number_balls):
            self.ball_liste[i].vx = self.ball_liste[i].vx * 1.5
            self.ball_liste[i].vy = self.ball_liste[i].vy * 1.5

    def slowdone(self):
        for i in range(number_balls):
            self.ball_liste[i].vx = self.ball_liste[i].vx / 1.5
            self.ball_liste[i].vy = self.ball_liste[i].vy / 1.5

    def pause(self):

        if not self.state_pause:
            self.state_pause = True
            self.liste_speed = []

            for i in range(number_balls):
                self.liste_speed.append([self.ball_liste[i].vx, self.ball_liste[i].vy])
                self.ball_liste[i].vx, self.ball_liste[i].vy = self.ball_liste[i].vx / 1000000, self.ball_liste[
                    i].vy / 1000000

        elif self.state_pause:
            self.state_pause = False
            for i in range(number_balls):
                self.ball_liste[i].vx, self.ball_liste[i].vy = self.liste_speed[i][0], self.liste_speed[i][1]


c = Control()
c.start(None, None, None)

mainloop()
