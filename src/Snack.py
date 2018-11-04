from Snacky import Snacky


class Snack():

    def __init__(self, can):
        self.canvas = can
        self.d = 'r'
        self.snack = [Snacky(4, 4, self.canvas)]
        # if player==human:
        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.direction)

    def direction(self, event):
        touche = event.keysym
        if self.d == 'r':
            if touche == 'Up':
                self.d = 'u'
            elif touche == 'Down':
                self.d = 'd'
        elif self.d == 'l':
            if touche == 'Up':
                self.d = 'u'
            elif touche == 'Down':
                self.d = 'd'
        elif self.d == 'u':
            if touche == 'Right':
                self.d = 'r'
            elif touche == 'Left':
                self.d = 'l'
        elif self.d == 'd':
            if touche == 'Right':
                self.d = 'r'
            elif touche == 'Left':
                self.d = 'l'

    def update(self):
        # print(self.d)
        if len(self.snack) > 1:
            past_x = self.snack[0].x
            past_y = self.snack[0].y
            if self.d == 'r':
                self.snack[0].x += 20
                self.snack[0].update()
            if self.d == 'l':
                self.snack[0].x -= 20
                self.snack[0].update()
            if self.d == 'u':
                self.snack[0].y -= 20
                self.snack[0].update()
            if self.d == 'd':
                self.snack[0].y += 20
                self.snack[0].update()
            for i in range(1, len(self.snack)):
                self.snack[i].x, past_x = past_x, self.snack[i].x
                self.snack[i].y, past_y = past_y, self.snack[i].y
                self.snack[i].update()

        else:
            if self.d == 'r':
                self.snack[0].x += 20
                self.snack[0].update()
            if self.d == 'l':
                self.snack[0].x -= 20
                self.snack[0].update()
            if self.d == 'u':
                self.snack[0].y -= 20
                self.snack[0].update()
            if self.d == 'd':
                self.snack[0].y += 20
                self.snack[0].update()

    def is_eating(self, t):
        if (self.snack[0].x, self.snack[0].y) == (t.x, t.y):
            return True
        return False

    def Cross(self):
        for i in range(len(self.snack)):
            for j in range(i + 1, len(self.snack)):
                if self.snack[i] == self.snack[j]:
                    return True
        return False
