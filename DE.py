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
                ui = copy.deepcopy(individual.get_position())
                individual.set_position( self.interchange( individual.get_position(), individual.get_fitness() ) )
                individual.set_fitness(self.problem.fitness(individual.get_position()))
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
        f = self.problem.fitness(individual)
        if f > fitness:
            return individual
        else:
            return actual

    def initialize_Individuals(self):
        for i in range(self.individuals):
            aux = Vector()
            aux.initialize(self.dimensions, self.problem.MAX_VALUE, self.problem.MIN_VALUE)
            self.Individuals_Array = np.append(self.Individuals_Array, aux)

    def Initialize_Fitness(self):
        for i in self.Individuals_Array:
            i.set_fitness(self.problem.fitness(i.get_position()))


#variante 0: Xr1 + F(Xr2 -Xr3)
#aux = Xr1.get_position()[i] + self.F*(Xr2.get_position()[i] - Xr3.get_position()[i])
#variante 1: best + F(XR1 - XR2  + XR3 - XR4)
#aux = self.best.get_position()[i] + self.F*( (Xr1.get_position()[i] - Xr2.get_position()[i]) + (Xr3.get_position()[i] - Xr4.get_position()[i]) )
#variante 2: XR0 + F(XR1 - XR2  + XR3 - XR4)
#aux = Xr0.get_position()[i] + self.F*( (Xr1.get_position()[i] - Xr2.get_position()[i]) + (Xr3.get_position()[i] - Xr4.get_position()[i]) )
#variante 3: Xi + F(Xb - Xi)
#aux = Xi.get_position()[i] + self.F*(self.best.get_position()[i] - Xi.get_position()[i])
#variante 4: Xr1 + F(Xb - Xr3)
#aux = Xr1.get_position()[i] + self.F*(self.best.get_position()[i] - Xr3.get_position()[i])
#variante 5: Xb + F(Xr2 - Xr3 + Xb - Xr4)
#aux = self.best.get_position()[i] + self.F*( (Xr2.get_position()[i] - Xr3.get_position()[i]) + (self.best.get_position()[i] - Xr4.get_position()[i]) )
#variante 6: Xi + F(Xb - Xi + Xr2 - Xr3)
#aux = Xi.get_position()[i] + self.F*( (self.best.get_position()[i] - Xi.get_position()[i]) + (Xr2.get_position()[i] - Xr3.get_position()[i]) )

#       def run(self):
#         self.initialize_Individuals()
#         self.Initialize_Fitness()
#         self.best = self.Individuals_Array[0]
#         generation = 1
#         cont = 0
#         while generation <= self.iterations:
#             u = []
#             if self.best.get_fitness() == self.dimensions:
#                 break
#             for individual in self.Individuals_Array:
#                 self.is_not_muted(individual)
#                 ui = self.is_muted(cont, individual)
#                 aux = Vector()
#                 aux.set_position(ui)
#                 aux.set_fitness(self.problem.fitness(ui))
#                 if aux.get_fitness() < individual.get_fitness() and aux.get_fitness() > 1:
#                     self.is_not_muted(aux)
#                 u.append(aux.get_position())
#                 cont+=1
#             cont = 0
#             for i in range(self.individuals):
#                 if self.problem.fitness(u[i]) > self.Individuals_Array[i].get_fitness():
#                     self.Individuals_Array[i].set_position(np.copy(u[i]))
#                     self.Individuals_Array[i].set_fitness(self.problem.fitness(self.Individuals_Array[i].get_position()))
#                 if self.Individuals_Array[i].get_fitness() > self.best.get_fitness():
#                     ob = copy.deepcopy(self.Individuals_Array[i])
#                     self.best = ob
#             print(f'generacion: {generation} - mejor: {self.best.get_position()} - fitness: {self.best.get_fitness()}')
#             generation += 1
#         return (self.best.get_position(),self.best.get_fitness())

#     def is_not_muted(self,actual):
#         individual = copy.deepcopy(actual)
#         for i in range(actual.get_fitness(),self.dimensions):
#             position1 = np.random.randint(0,self.dimensions)
#             position2 = np.random.randint(0,self.dimensions)
#             aux = copy.deepcopy(individual.get_position()[position1])
#             individual.get_position()[position1] = individual.get_position()[position2]
#             individual.get_position()[position2] = aux
#         individual.set_fitness(self.problem.fitness(individual.get_position()))
#         if individual.get_fitness() > actual.get_fitness():
#             actual.set_fitness(individual.get_fitness())
#             actual.set_position(individual.get_position())

#     def is_muted(self,cont, individual):
#         ui = []
#         self.F = np.random.random()
#         Pf = np.random.random()
#         a = np.random.random()
#         method = np.random.randint(0,6)
#         if a < Pf:
#             vi = self.get_mutant(cont,method)
#         else:
#             K = (self.F + 1) / 2
#             vi = self.get_mutant(cont,method,K)
#         L = np.random.randint(0,self.dimensions)
#         s = np.random.randint(0,self.dimensions)
#         J = set()
#         J = self.fill_J(s,L)
#         for j in range(self.dimensions):
#             if j in J:
#                 y = np.copy(vi)
#                 ui.append(y[j])
#             else:
#                 x = np.copy(individual.get_position())
#                 ui.append(x[j])
#         return ui

#     def fill_J(self,s,L):
#         sV = set()
#         for Svalues in range(s, min(self.dimensions,s + L -1) ):
#             sV.add(Svalues)
#         oV = set()
#         for operationValues in range(1, (s + L - self.dimensions - 1) ):
#             oV.add(operationValues)
#         sV.union(oV)
#         return sV

#     def get_mutant(self, j, method,K=0):
#         r0 = np.random.randint(0,self.individuals)
#         while r0 == j:
#             r0 = np.random.randint(0,self.individuals)
#         r1 = np.random.randint(0,self.individuals)
#         while r1 == j or r1 == r0:
#             r1 = np.random.randint(0,self.individuals)
#         r2 = np.random.randint(0,self.individuals)
#         while r2 == j or r2 == r1 or r2 == r0:
#             r2 = np.random.randint(0,self.individuals)
#         r3 = np.random.randint(0,self.individuals)
#         while r3 == r2 or r3 == j or r3 == r1 or r3 == r0:
#             r3 = np.random.randint(0,self.individuals)
#         r4 = np.random.randint(0,self.individuals)
#         while r4 == r3 or r4 == j or r4 == r2 or r4 == r1 or r4 == r0:
#             r4 = np.random.randint(0,self.individuals)
        
#         #Individuos
#         Xr0 = copy.deepcopy(self.Individuals_Array[r0])
#         Xr1 = copy.deepcopy(self.Individuals_Array[r1])
#         Xr2 = copy.deepcopy(self.Individuals_Array[r2])
#         Xr3 = copy.deepcopy(self.Individuals_Array[r3])
#         Xr4 = copy.deepcopy(self.Individuals_Array[r4])
#         Xi = copy.deepcopy(self.Individuals_Array[j])
#         vi = np.array([])
#         for i in range(self.dimensions):

#             #variantes originales
#             if K is not 0:
#                 if method is 0:
#                     #variante 0: Xr1 + F(Xr2 -Xr3)
#                     aux = Xr1.get_position()[i] + self.F*(Xr2.get_position()[i] - Xr3.get_position()[i])
#                 if method is 1:
#                     #variante 1: best + F(XR1 - XR2  + XR3 - XR4)
#                     aux = self.best.get_position()[i] + self.F*( (Xr1.get_position()[i] - Xr2.get_position()[i]) + (Xr3.get_position()[i] - Xr4.get_position()[i]) )
#                 if method is 2:
#                     #variante 2: XR0 + F(XR1 - XR2  + XR3 - XR4)
#                     aux = Xr0.get_position()[i] + self.F*( (Xr1.get_position()[i] - Xr2.get_position()[i]) + (Xr3.get_position()[i] - Xr4.get_position()[i]) )
#                 if method is 3:
#                     #variante 3: Xi + F(Xb - Xi)
#                     aux = Xi.get_position()[i] + self.F*(self.best.get_position()[i] - Xi.get_position()[i])
#                 if method is 4:
#                     #variante 4: Xr1 + F(Xb - Xr3)
#                     aux = Xr1.get_position()[i] + self.F*(self.best.get_position()[i] - Xr3.get_position()[i])
#                 if method is 5:
#                     #variante 5: Xb + F(Xr2 - Xr3 + Xb - Xr4)
#                     aux = self.best.get_position()[i] + self.F*( (Xr2.get_position()[i] - Xr3.get_position()[i]) + (self.best.get_position()[i] - Xr4.get_position()[i]) )
#                 if method is 6:
#                     #variante 6: Xi + F(Xb - Xi + Xr2 - Xr3)
#                     aux = Xi.get_position()[i] + self.F*( (self.best.get_position()[i] - Xi.get_position()[i]) + (Xr2.get_position()[i] - Xr3.get_position()[i]) )
                
#             #variantes con K    
#             else:
#                 if method is 0:
#                     #variante 0: Xr1 + F(Xr2 -Xr3)
#                     aux = Xr1.get_position()[i] + K*(Xr2.get_position()[i] - Xr3.get_position()[i])
#                 if method is 1:
#                     #variante 1: best + F(XR1 - XR2  + XR3 - XR4)
#                     aux = self.best.get_position()[i] + K*( (Xr1.get_position()[i] - Xr2.get_position()[i]) + (Xr3.get_position()[i] - Xr4.get_position()[i]) )
#                 if method is 2:
#                     #variante 2: XR0 + F(XR1 - XR2  + XR3 - XR4)
#                     aux = Xr0.get_position()[i] + K*( (Xr1.get_position()[i] - Xr2.get_position()[i]) + (Xr3.get_position()[i] - Xr4.get_position()[i]) )
#                 if method is 3:
#                     #variante 3: Xi + F(Xb - Xi)
#                     aux = Xi.get_position()[i] + K*(self.best.get_position()[i] - Xi.get_position()[i])
#                 if method is 4:
#                     #variante 4: Xr1 + F(Xb - Xr3)
#                     aux = Xr1.get_position()[i] + K*(self.best.get_position()[i] - Xr3.get_position()[i])
#                 if method is 5:
#                     #variante 5: Xb + F(Xr2 - Xr3 + Xb - Xr4)
#                     aux = self.best.get_position()[i] + K*( (Xr2.get_position()[i] - Xr3.get_position()[i]) + (self.best.get_position()[i] - Xr4.get_position()[i]) )
#                 if method is 6:
#                     #variante 6: Xi + F(Xb - Xi + Xr2 - Xr3)
#                     aux = Xi.get_position()[i] + K*( (self.best.get_position()[i] - Xi.get_position()[i]) + (Xr2.get_position()[i] - Xr3.get_position()[i]) )            
            
#             if aux > self.problem.MAX_VALUE or aux < self.problem.MIN_VALUE:
#                 aux = aux % self.problem.MAX_VALUE
#             aux = round(aux)
#             vi = np.append(vi, aux)
#         return vi
