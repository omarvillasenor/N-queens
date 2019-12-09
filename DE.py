import numpy as np
import copy

class Vector():
    
    def __init__(self):
        self.position = np.array([])
        self.fitness = 0

    def get_position(self):
        return self.position

    def set_position(self,pos):
        self.position = pos

    def get_fitness(self):
        return self.fitness

    def set_fitness(self,f):
        self.fitness = f

    def initialize(self, dimensions, Max, Min):
        lista = np.array([])
        for i in range(0,dimensions):
            aux = np.random.randint(0,dimensions)
            while aux in lista:
                aux = np.random.randint(0,dimensions)
            lista = np.append(lista,aux)
        self.position = lista

class DE():

    def __init__(self,individuals,iterations,dimensions,problem):
        self.individuals = individuals
        self.iterations = iterations
        self.dimensions = dimensions
        self.problem = problem
        self.Individuals_Array = np.array([])
        self.best = object

    def run(self):
        self.initialize_Individuals()
        self.Initialize_Fitness()
        self.best = self.Individuals_Array[0]
        generation = 1
        cont = 0
        while generation <= self.iterations:
            u = []
            if self.best.get_fitness() == self.dimensions:
                break
            for individual in self.Individuals_Array:
                ui = self.interchange(individual.get_position(),individual.get_fitness())
                u.append(ui)
                cont+=1
            cont = 0
            for i in range(self.individuals):
                if self.problem.fitness(u[i]) > self.Individuals_Array[i].get_fitness():
                    self.Individuals_Array[i].set_position(np.copy(u[i]))
                    self.Individuals_Array[i].set_fitness(self.problem.fitness(self.Individuals_Array[i].get_position()))
                if self.Individuals_Array[i].get_fitness() > self.best.get_fitness():
                    ob = copy.deepcopy(self.Individuals_Array[i])
                    self.best = ob
            print(f'generacion: {generation} - mejor: {self.best.get_position()} - fitness: {self.best.get_fitness()}')
            generation += 1
        return (self.best.get_position(),self.best.get_fitness())

    def interchange(self,actual,fitness):
        individual = copy.deepcopy(actual)
        position1 = np.random.randint(0,self.dimensions)
        position2 = np.random.randint(0,self.dimensions)
        aux = copy.deepcopy(individual[position1])
        individual[position1] = individual[position2]
        individual[position2] = aux
        return individual

    def initialize_Individuals(self):
        for i in range(self.individuals):
            aux = Vector()
            aux.initialize(self.dimensions, self.problem.MAX_VALUE, self.problem.MIN_VALUE)
            self.Individuals_Array = np.append(self.Individuals_Array, aux)

    def Initialize_Fitness(self):
        for i in self.Individuals_Array:
            i.set_fitness(self.problem.fitness(i.get_position()))