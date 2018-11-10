from tkinter import*
import numpy as np
from Snack import Snack
from Snacky import Snacky
from Target import Target
from Brain import fitness


class SnackGame(Tk):

    def __init__(self, player="IA", population=None):
        # ----- Initialisation de la fenêtre ---------
        Tk.__init__(self)
        self.geometry('600x635+400+20')
        self.title('Snack Game')
        self.h = 100
        self.score = 0
        self.info = Canvas(self, width=600, height=31, bg='black')
        self.info.grid(row=2)
        self.info_score = self.info.create_text(
            548, 18, text='Score : ' + str(self.score), font='Arial 15 bold', fill='white')
        # ----- Initialisation du canvas ------------
        self.field = Canvas(self, width=600, height=600, background='black')
        self.field.grid(row=1)
        self.p = Snack(self.field)
        self.q = Target(self.field)
        # ------- Initialisation IA ------------------
        self.i = 0
        self.Reproduction = False
        self.MinDist = 10**5
        self.moves = 1
        self.Waiting = False
        self.player = "IA"
        self.event_add('<<reprod>>', '<KeyRelease-F9>')
        self.bind('<<reprod>>', self.restart)
        if player == "IA":
            self.population = population
            self.brain = self.population.population[self.i]
        self.start()

    def start(self):
        if self.p.is_eating(self.q):
            self.p.snack.append(Snacky(self.q.x, self.q.y, self.field))
            self.q.update()
            self.score += 1
            self.info.itemconfigure(
                self.info_score, text='Score : ' + str(self.score))
            # self.h -= 5

        if self.player == "IA":
            X = np.zeros((900,))
            for loop in range(len(self.p.snack)):
                pos = (self.p.snack[loop].y +
                       self.p.snack[loop].x - 8) // 20 - 1
                X[pos] = 1
            X[(self.q.x + self.q.y - 8) // 20 - 1] = 2
            y = self.brain.predict(X)
            if (y == 0 and self.p.d != 'l'):
                self.p.d = 'r'
            elif (y == 1 and self.p.d != 'r'):
                self.p.d = 'l'
            elif (y == 2 and self.p.d != 'd'):
                self.p.d = 'u'
            elif(y == 3 and self.p.d != 'u'):
                self.p.d = 'd'

        self.p.update()
        self.getMinDistance(self.ComputeDist())
        self.moves += 1
        if self.Game_Over():
            self.field.create_text(300, 300, text='Game Over', font='Arial 30 bold', fill='purple')
            if self.player == "IA":
                self.brain.fitness = fitness(self.score, self.MinDist, self.moves)
                # print(self.brain.fitness)
                self.i = self.i + 1
                print(self.i)
                if self.i >= self.population.size:
                    self.i = 0
                    self.Reproduction = True
                    self.Waiting = True

                else:
                    self.brain = self.population.population[self.i]
                if self.Waiting == False:
                    self.after(100, self.AutomaticRestart)
            else:
                self.bind('<Key>', self.restart)
        else:
            self.after(self.h, self.start)

    def restart(self, event):
        touche = event.keysym
        if touche == 'Return':
            # print("Enter")
            # self.unbind('<Key>')
            self.field.destroy()
            # self.h = 50
            self.score = 0
            self.MinDist = 10**5
            self.moves = 1
            self.field = Canvas(self, width=600, height=600, background='black')
            self.field.grid(row=1)
            self.p = Snack(self.field)
            self.q = Target(self.field)

            self.start()

        print("Here Good")
        self.field.destroy()
        # self.h = 50
        self.score = 0
        self.MinDist = 10**5
        self.moves = 1
        self.field = Canvas(self, width=600, height=600, background='black')
        self.field.grid(row=1)
        self.p = Snack(self.field)
        self.q = Target(self.field)
        self.start()

    def AutomaticRestart(self):
        # print("Restart")
        # self.h = 100
        self.score = 0
        self.MinDist = 10**5
        self.moves = 1
        self.field = Canvas(self, width=600, height=600, background='black')
        self.field.grid(row=1)
        self.p = Snack(self.field)
        self.q = Target(self.field)
        self.start()

    def ComputeDist(self):
        x = abs(self.p.snack[0].x - self.q.y)
        y = abs(self.p.snack[0].y - self.q.y)

        return x + y

    def getMinDistance(self, n):

        if (n < self.MinDist):
            self.MinDist = n

    def Game_Over(self):
        if self.p.snack[0].x < 0:
            return True
        elif self.p.snack[0].x > 600:
            return True
        elif self.p.snack[0].y < 0:
            return True
        elif self.p.snack[0].y > 600:
            return True
        elif self.p.Cross():
            return True
        return False
