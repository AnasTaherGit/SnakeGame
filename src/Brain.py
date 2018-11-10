import numpy as np
from random import choice, random


def relu(x):
    return x * (x > 0)


def softmax(x):
    e_x = np.exp(x - np.max(x))

    return e_x / e_x.sum()


def pick(seq, k=2):
    picked = []
    sumx = sum([br.fitness for br in seq]) + len(seq)
    i = 0
    cpt = 0
    while (len(picked)) < k:
        if random() < (seq[i].fitness + 1) / sumx:
            picked.append(seq[i])
            i += 1
            if (i >= len(seq)):
                i = 0
        cpt += 1
        if cpt > 20:
            picked = [seq[0], seq[1]]
    return picked


def fitness(score, dist, moves):

    return (score + 1) / ((dist * moves)**2 + 1)


class Brain():
    def __init__(self, n_inputs, n_hiddens, n_outputs, mutationRate):
        self.NbInputs = n_inputs
        self.NbHiddens = n_hiddens
        self.NbOutputs = n_outputs
        self.WeightHidden = np.zeros((self.NbHiddens, self.NbInputs))
        self.WeightOutputs = np.zeros((self.NbOutputs, self.NbHiddens))
        self.mutationRate = mutationRate
        self.fitness = 0

    def predict(self, X):

        return np.argmax(softmax(self.WeightOutputs@relu(self.WeightHidden@X)))

    def randomize(self):
        self.WeightHidden = np.random.random((self.NbHiddens, self.NbInputs))
        self.WeightOutputs = np.random.random((self.NbOutputs, self.NbHiddens))

    def CrossOver(self, other):
        child = Brain(self.NbInputs, self.NbHiddens,
                      self.NbOutputs, self.mutationRate)
        for i in range(self.NbHiddens):
            for j in range(0, self.NbInputs):
                child.WeightHidden[i][j] = choice(
                    [self.WeightHidden[i][j], other.WeightHidden[i][j]])
        for i in range(self.NbOutputs):
            for j in range(0, self.NbHiddens):
                child.WeightOutputs[i][j] = choice(
                    [self.WeightOutputs[i][j], other.WeightOutputs[i][j]])

        return child

    def mutate(self):
        for i in range(self.NbHiddens):
            for j in range(self.NbInputs):
                if random() < self.mutationRate:
                    self.WeightHidden[i][j] = random()
        for i in range(self.NbOutputs):
            for j in range(self.NbHiddens):
                if random() < self.mutationRate:
                    self.WeightHidden[i][j] = random()


class Population():

    def __init__(self, n_inputs, n_hiddens, n_outputs, size, mutationRate=0.01):

        self.n_inputs = n_inputs
        self.n_hiddens = n_hiddens
        self.n_outputs = n_outputs
        self.size = size
        self.population = [0] * size
        self.mutationRate = mutationRate
        self.generation = 1
        print("Generation :", self.generation)

    def initialize(self):
        for i in range(self.size):
            self.population[i] = Brain(
                self.n_inputs, self.n_hiddens, self.n_outputs, self.mutationRate)
            self.population[i].randomize()

    def Reproduction(self):
        matingpool = list(self.population)
        for loop in range(self.size):
            picked = pick(matingpool)
            child = picked[0].CrossOver(picked[1])
            self.population.append(child)
        for loop in range(self.size):
            del self.population[loop]
        self.generation += 1
        print("Generation :", self.generation)

    def mutation(self):
        for b in self.population:
            b.mutate()
