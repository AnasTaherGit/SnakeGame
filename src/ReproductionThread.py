from threading import Thread


class Handler(Thread):

    def __init__(self, App):
        Thread.__init__(self)
        self.App = App

    def run(self):
        while True:
            expr = self.App.Reproduction
            if (expr == True):
                self.App.Reproduction = False
                self.App.Waiting = False
                self.App.population.Reproduction()
                print("Reproduction done")
                self.App.population.mutation()
                print("Mutation done")
                self.App.event_generate('<<reprod>>')
                print("GOOD")
