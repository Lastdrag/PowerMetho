import numpy as np
import csv
from Util import Util

class Matrix:
    
    def __init__(self, *args):
        
        # A new matrix is created by giving the args[0] parameter
        # if args[0] is an integer then it will create a square
        # matrix with this parameter.
        if isinstance(args[0],int):
            self.size = args[0]
            self.matrix = np.transpose(np.random.dirichlet(np.ones(args[0]),size=args[0]))
            self.rows, self.columns = self.matrix.shape
        
        # if args[0] is a string (the path of csv file) then it will load the
        # csv file in a new matrix
        elif isinstance(args[0],str):
            util = Util
            self.file = args[0]
            file = open(self.file)
            rows = len(file.readlines())
            file.close()
            self.rows = rows
            with open(self.file, 'r') as nFile:
                line = nFile.readline()
            self.columns = line.count(',') + 1 
            self.matrix=np.empty((self.rows,self.columns))

            #fill the matrix 
            with open(args[0]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                f = 0
                for row in csv_reader:
                    for c in range(self.columns):
                        self.matrix[f,c] = util.stringToFloat(row[c])
                    f += 1
        # creates a canonical vector
        self.canonicalVector=np.empty((self.rows,1))
        for f in range(self.rows):
            if (f == 0):
                self.canonicalVector[f,0]= 1
            else:
                self.canonicalVector[f,0]= 0   
    
    def getNumberOfRows(self):
        return self.rows

    def getNumberOfColumns(self):
        return self.columns

    def getMatrix(self):
        return self.matrix
    
    def getCanonicalVector(self):
        return self.canonicalVector;
    
    def setCanonicalVector(self,canonicalVector):
        self.canonicalVector = canonicalVector
    
