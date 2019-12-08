import copy

class Queen: 
    
    def __init__(self,queens):
        self.queens = queens
        self.MIN_VALUE = 0
        self.MAX_VALUE = queens
        self.good_list = []
        
    def get_size(self):
        return self.queens
                
    def fitness(self,cromosome):
        order_list = copy.deepcopy(cromosome)
        order_list.sort()
        return self.check_crashes(cromosome)

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