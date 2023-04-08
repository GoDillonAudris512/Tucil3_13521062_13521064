# File : AStar.py
# Contains the class AStar, that are used for
# Finding the shortest path on a graph using the A* algorithm

from queue import PriorityQueue

class AStar:

    # CONSTRUCTOR
    # Construct and initialize the object
    def __init__(self, nodeName, map, heuristicMap):
        self.nodeName = nodeName                      # list of name of node, used for showing the true path 
        self.map = map                                # adjacency matrix used to represent the graph
        self.heuristicMap = heuristicMap              # matrix of heuristic value, store the straight line distance of node of row i to node of column j
        self.queue = PriorityQueue()                  # queue used to process and pick the node to expand
        self.visited = set()                          # set to store all nodes that are already visited
        self.found = False                            # boolean flag to know is the result path is valid or not
        self.resultPath = []                          # list of the node that create the shortest path from start node to goal node
        self.distance = 0                             # the optimum distance from start node to goal node

    # GETTER
    # Get the result path
    def getResultPath(self):                           
        return self.resultPath
    
    # Get the distance
    def getDistance(self):
        return self.distance
    
    # Get the validity of the result path
    def getFound(self):
        return self.found
    
    # HELPER METHOD
    # Return string that contains all of node name from the result path
    def getPathName(self):
        pathName = ""

        for i in range(0, len(self.resultPath)-1):
            pathName += self.nodeName[self.resultPath[i]] + " - "
        
        pathName += self.nodeName[self.resultPath[len(self.resultPath)-1]]

        return pathName

    # A* ALGORITHM
    # Awaken the node adjacent to the expand node and put it to the queue
    def awakenNode(self, tempCost, tempNode, tempPath, goalNode):
        # Put the expand node to visited set
        self.visited.add(tempNode)

        # Put all node adjacent to expand node and not visited to the queue
        for i in range(0, len(self.map)):
            if (i not in self.visited and self.map[tempNode][i] != 0):
                self.queue.put((tempCost + self.map[tempNode][i] + self.heuristicMap[i][goalNode], i, tempPath + [tempNode]))

    # Start the A* algorithm until the result path from start node to goal node is found   
    def findPath(self, startNode, goalNode):
        # Awaken the start node
        self.queue.put((0 + self.heuristicMap[startNode][goalNode], startNode, []))

        # Looping until the goalNode is found
        while (not self.found and not self.queue.empty()):
            tempCost, tempNode, tempPath = self.queue.get()

            tempCost -= self.heuristicMap[tempNode][goalNode]

            if (tempNode == goalNode):
                self.found = True
            else:
                self.awakenNode(tempCost, tempNode, tempPath, goalNode)

        # Put the result to attributes
        self.resultPath = tempPath + [tempNode]
        self.distance = tempCost

        # Clear the queue and visited set
        while (not self.queue.empty()):
            self.queue.get()
        self.visited.clear()