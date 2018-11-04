class Snacky():

    def __init__(self, x, y, can):
        self.x = x
        self.y = y
        self.canvas = can
        # ----- Initialisation du Snacky ------------
        self.snacky = self.canvas.create_rectangle(self.x, self.y, self.x + 16, self.y + 16, fill='white')

    def update(self):
        self.canvas.coords(self.snacky, self.x, self.y, self.x + 16, self.y + 16)

    def __eq__(self, other):
        if (self.x, self.y) == (other.x, other.y):
            return True
        return False
