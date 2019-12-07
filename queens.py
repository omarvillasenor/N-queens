import copy

class Queen: 
    
    def __init__(self,queens):
        self.queens = queens
        self.MIN_VALUE = 0
        self.MAX_VALUE = queens
        self.good_list = []
        self.create_good_list()

    def create_good_list(self):
        for i in range(0,self.queens):
            self.good_list.append(i)
        
    def get_size(self):
        return self.queens
                
    def fitness(self,cromosome):
        order_list = copy.deepcopy(cromosome)
        order_list.sort()
        criterion = self.evaluate_queens(order_list)
        if criterion > 1:
            return criterion * -1000
        elif criterion == 1:
            return criterion * -100
        else:
            return self.check_crashes(cromosome)


    def evaluate_queens(self,order_list):
        numbers = 0
        for i in range(self.queens):
            if self.good_list[i] != order_list[i]:
                numbers += 1
        return numbers


    def check_crashes(self,cromosome):
        bandera = True
        q = 0 
        for i in range(len(cromosome)):
            actual = cromosome[i]
            for j in range(len(cromosome)):
                if j !=  i:
                    i_qi = i - actual
                    j_qj = j - cromosome[j]
                    i__qi = i + actual
                    j__qj = j + cromosome[j]
                    if (i_qi == j_qj) or (i__qi == j__qj):
                        bandera = False
            if bandera:
                q+=1
            else:
                bandera = True
        return q