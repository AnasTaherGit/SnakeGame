from SnackGame import SnackGame
from Brain import *

n_inputs = 30 * 30
n_hidden = 300
n_outputs = 4
size = 20


p = Population(n_inputs, n_hidden, n_outputs, size)
p.initialize()
s = SnackGame(population=p)
s.mainloop()
