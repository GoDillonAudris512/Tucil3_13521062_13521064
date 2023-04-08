# File : Parser.py
# Contains the class Parser, that are used for
# Parsing the input file for name of nodes, adjacency matrix, and heuristic value
"""
File Format:
a b c d e f g h             line 1: the name of nodes, from node 1, 2, etc, separated by whitelines
0 1 1 1 1 1 1 1             
1 0 1 1 1 1 1 1                                                
1 1 0 1 1 1 1 1
1 1 1 0 1 1 1 1             line 2 and the next number of node lines: 
1 1 1 1 0 1 1 1             the adjacency matrix, represent the cost from one node to another, must be symmetric
1 1 1 1 1 0 1 1             elements not in main diagonal must be >= 0, the main diagonal must be 0, the column must also equal to number of node
1 1 1 1 1 1 0 1
1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1             
1 0 1 1 1 1 1 1                                                
1 1 0 1 1 1 1 1
1 1 1 0 1 1 1 1             line 2 + number of node + 1 and the next number of node lines:
1 1 1 1 0 1 1 1             the heurisic value matrix, represent the straight line distance from one node to another, must be symmetric
1 1 1 1 1 0 1 1             elements not in main diagonal must be > 0, the main diagonal must be 0, column must also equal to number of node
1 1 1 1 1 1 0 1
1 1 1 1 1 1 1 0
"""

class Parser:

    # CONSTRUCTOR
    # Construct and initialize the object
    def __init__(self, fileName):
        self.row = -1
        self.col = -1
        self.map = [[]]
        self.heuristicMap = [[]]
        self.nodeName = []
        self.fileName = fileName

    # GETTER
    # Get the row of matrix
    def getRow(self):
        return self.row
    
    # Get the column of matrix
    def getCol(self):
        return self.col
    
    # Get the adjacency matrix
    def getMap(self):
        return self.map
    
    # Get the heuristic matrix
    def getHeuristicMap(self):
        return self.heuristicMap
    
    # Get the list of node name
    def getNodeName(self):
        return self.nodeName
    
    # HELPER METHOD
    # Check if the map and heuristic map symmetric or not
    def isMapSymmetric(self):
        i = 0
        isSymmetric = True

        while (i < self.row and isSymmetric):
            j = i+1
            while (j < self.col and isSymmetric):
                if (self.map[i][j] != self.map[j][i] or self.heuristicMap[i][j] != self.heuristicMap[j][i]):
                    isSymmetric = False
                else:
                    j += 1
            if (isSymmetric):
                i += 1

        return isSymmetric
    
    # PARSING METHOD
    # Parse the line and fill it to nodeName attribute
    def parseNodeName(self, line):
        nameList = line.split(" ")
        
        # Check if there is less than 8 nodes
        if (len(nameList) < 8):
            raise Exception("Please input a map/graph that contain 8 nodes or more")
        
        self.row = len(nameList)
        self.col = len(nameList)

        # Put all the name of node
        for name in nameList:
            self.nodeName.append(name.strip("\n"))

    # Parse every line on lines and fill it to map attribute
    def parseMap(self, lines):
        self.map = [[0 for j in range(self.col)] for i in range(self.row)]

        # Put all elements to map
        for i in range (0, self.row):
            line = lines[i].split(" ")

            # Check if the column for this line is the same as number of node
            if (len(line) != self.col):
                raise Exception("Different number of columns in a map row")
            
            for j in range(0, self.col):
                # Check if the element does not follow the format
                if (i != j and int(line[j]) < 0):
                    raise Exception("The weight of the sides of map/graph cannot be < 0")
                if (i == j and int(line[j]) != 0):
                    raise Exception("The map main diagonal elements must be 0")
                
                self.map[i][j] = int(line[j])

    # Parse every line on lines and fill it to map attribute
    def parseHeuristic(self, lines):
        self.heuristicMap = [[0 for j in range(self.col)] for i in range(self.row)]

        # Put all elements to map
        for i in range (0, self.row):
            line = lines[i].split(" ")

            # Check if the column for this line is the same as number of node
            if (len(line) != self.col):
                raise Exception("Different number of columns in a heuristic map row")
            
            for j in range(0, self.col):
                # Check if the element does not follow the format
                if (i != j and int(line[j]) <= 0):
                    raise Exception("The straight line distance of two node cannot \u2264 0")
                if (i == j and int(line[j]) != 0):
                    raise Exception("The heuristic map main diagonal elements must be 0")
                
                self.heuristicMap[i][j] = int(line[j])

    # Open the map/graph file and start the parse
    def openAndParse(self):
        # Check if the file is in txt format or not
        if (not self.fileName.endswith(".txt")):
            raise Exception("Invalid file format, must be txt")
        
        # Open and read all lines of file
        with open(f"{self.fileName}", "r") as file:
            lines = file.readlines()
            file.close()
        
        # Check if the file is empty
        if (len(lines) == 0):
            raise Exception('The file is empty')
        
        # Parse the first lines, get all of node names
        self.parseNodeName(lines[0])

        # Check if there is enough remaining lines for map
        if (len(lines)-1 < self.row):
            raise Exception("There is too few row for map")
        
        # Parse the map, get the adjacency matrix
        self.parseMap(lines[1:1+self.row])

        # Check if there is exactly enough remaining lines for heuristic map
        if (len(lines)-1-self.row != self.row):
            raise Exception("There is too few or too much row for heuristic map")
        
        # Parse the heuristic map
        self.parseHeuristic(lines[1+self.row:1+self.row+self.row])
        
        # Check if map and heuristic map symmetric or not
        if (not self.isMapSymmetric() ):
            raise Exception("One of the sides in map/graph has two different weight")