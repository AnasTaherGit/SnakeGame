from tkinter import*
from Snack import Snack
from Snacky import Snacky
from Target import Target


class SnackGame(Tk):

    def __init__(self):
        # ----- Initialisation de la fenêtre ---------
        Tk.__init__(self)
        self.geometry('600x635+400+20')
        self.title('Snack Game')
        self.h = 150
        self.score = 0
        self.info = Canvas(self, width=600, height=31, bg='black')
        self.info.grid(row=2)
        self.info_score = self.info.create_text(548, 18, text='Score : ' + str(self.score), font='Arial 15 bold', fill='white')
        # ----- Initialisation du canvas ------------
        self.field = Canvas(self, width=600, height=600, background='black')
        self.field.grid(row=1)
        self.p = Snack(self.field)
        self.q = Target(self.field)
        self.start()

    def start(self):
        if self.p.is_eating(self.q):
            self.p.snack.append(Snacky(self.q.x, self.q.y, self.field))
            self.q.update()
            self.score += 1
            self.info.itemconfigure(self.info_score, text='Score : ' + str(self.score))
            self.h -= 5
        # if player==AI:
            # AI.make_decision(self.p)
        self.p.update()
        if self.Game_Over():
            self.field.create_text(300, 300, text='Game Over', font='Arial 30 bold', fill='purple')
            self.bind('<Key>', self.restart)
            # self.after(1500, self.restart)
        else:
            self.after(self.h, self.start)

    def restart(self, event):
        touche = event.keysym
        if touche == 'Return':
            # print("Enter")
            self.unbind('<Key>')
            self.field.destroy()
            self.h = 150
            self.score = 0
            self.field = Canvas(self, width=600, height=600, background='black')
            self.field.grid(row=1)
            self.p = Snack(self.field)
            self.q = Target(self.field)

            self.start()

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
