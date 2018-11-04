from random import randint


class Target():

    def __init__(self, canv):
        self.x = randint(1, 28) * 20 + 4
        self.y = randint(1, 29) * 20 + 4
        self.canvas = canv
        self.target = self.canvas.create_rectangle(self.x, self.y, self.x + 16, self.y + 16, fill='red')

    def update(self):
        self.x = randint(1, 28) * 20 + 4
        self.y = randint(1, 29) * 20 + 4
        self.canvas.coords(self.target, self.x, self.y, self.x + 16, self.y + 16)
