from Matrix import Matrix
import numpy as np 

class Operation:
    
    def __init__(self, iterationNumber, arg):
        self.iterationNumber = iterationNumber
        self.arg = arg
        self.iteration = []
        
    def powerMethod(self):
        self.iteration = []
        self.result = None
        matrix = Matrix(self.arg)
        value=self.checkStochastic(matrix)
       
        if value == True:
            for x in range(self.iterationNumber):
                self.result=np.dot(matrix.getMatrix(),matrix.getCanonicalVector())
                matrix.setCanonicalVector(self.result)
                self.iteration.append(np.transpose(self.result))
            return True
        else:
            return False
    
    def getIteration(self):
        return self.iteration
    
    def checkStochastic(self,matrix):
        listOfValues = np.sum(matrix.getMatrix(),axis=0)
        for x in listOfValues:
            if round(x,4) != 1:
                return False
        return True
