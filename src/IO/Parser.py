# File : Parser.py
# Berisi class Parser, yang bertugas untuk
# Melakukan parsing terhadap file input dan mengembalikan adjacency matrix yang sesuai
# File harus berada di dalam folder test yang setara kedudukannya dengan folder src

class Parser:

    # Constructor
    def __init__(self, fileName):
        self.row = -1
        self.col = -1
        self.map = [[]]
        self.fileName = fileName

    # Getter
    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col
    
    def getMap(self):
        return self.map
    
    # Check if the map symmetric or not
    def isMapSymmetric(self):
        i = 0
        isSymmetric = True

        while (i < self.row and isSymmetric):
            j = i+1
            while (j < self.col and isSymmetric):
                if (self.map[i][j] != self.map[j][i]):
                    isSymmetric = False
                else:
                    j += 1
            if (isSymmetric):
                i += 1

        return isSymmetric
    
    # Parse every line on lines and fill it to map attributes
    def parseFile(self, lines):
        self.map = [[0 for j in range(self.col)] for i in range(self.row)]

        for i in range (0, self.row):
            line = lines[i].split(" ")

            if (len(line) != self.col):
                raise Exception("Different number of columns in a row")
            
            for j in range(0, self.col):
                if (int(line[j]) < 0):
                    raise Exception("The weight of the sides of map/graph cannot be less than 0")
                self.map[i][j] = int(line[j])

    # Open the map/graph file and start the parse
    def openAndParse(self):
        with open(f"../test/{self.fileName}.txt", "r") as file:
            lines = file.readlines()
            file.close()
            
        self.row = len(lines)
        self.col = len(lines[0].split(" "))

        if (self.row != self.col):
            raise Exception("Column and row of the matrix is not the same")
        if (self.row < 8):
            raise Exception("Please input a map/graph that contain 8 nodes or more")
        
        self.parseFile(lines)

        if (not self.isMapSymmetric()):
            raise Exception("One of the sides in map/graph has two different weight")