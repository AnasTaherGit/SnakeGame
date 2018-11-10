from threading import Thread
from SnackGame import SnackGame
from Brain import Population
from ReproductionThread import *


n_inputs = 30 * 30
n_hidden = 300
n_outputs = 4
size = 50


class AppHandler(Thread):

    def __init__(self, App):
        Thread.__init__(self)
        self.App = App

    def run(self):
        self.App.mainloop()


p = Population(n_inputs, n_hidden, n_outputs, size)
p.initialize()
s = SnackGame(population=p)
handler = Handler(s)
#appHandler = AppHandler(s)
handler.start()
s.mainloop()
# appHandler.start()
