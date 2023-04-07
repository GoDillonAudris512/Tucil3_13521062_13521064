# File : AStar.py
# Contains the class AStar, that are used for
# Finding the shortest path on a graph using the A* algorithm

from queue import PriorityQueue

class AStar:

    # CONSTRUCTOR
    # Construct and initialize the object
    def __init__(self, nodeName, map, heuristicList):
        self.nodeName = nodeName                      # list of name of node, used for showing the true path 
        self.map = map                                # adjacency matrix used to represent the graph
        self.heuristicList = heuristicList            # matrix of heuristic value, store the straight line distance of node of row i to node of column j
        self.queue = PriorityQueue()                  # queue used to process and pick the node to expand
        self.visited = set()                          # set to store all nodes that are already visited
        self.resultPath = []                          # list of the node that create the shortest path from start node to goal node
        self.distance = 0                             # the optimum distance from start node to goal node

    # GETTER
    # Get the result path
    def getResultPath(self):                           
        return self.getPathName()
    
    # Get the distance
    def getDistance(self):
        return self.distance
    
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
    def awakenNode(self, goalNode):
        # Put the expand node to visited set
        expandNode = self.resultPath[len(self.resultPath) - 1]
        self.visited.add(expandNode)

        # Put all node adjacent to expand node and not visited to the queue
        for i in range(0, len(self.map)):
            if (i not in self.visited and self.map[expandNode][i] != 0):
                self.queue.put((self.distance + self.map[expandNode][i] + self.heuristicList[i][goalNode], i, self.resultPath))

    # Start the A* algorithm until the result path from start node to goal node is found   
    def findRoute(self, startNode, goalNode):
        # Awaken the start node
        self.queue.put((0 + self.heuristicList[startNode][goalNode], startNode, []))

        # Looping until the goalNode is found
        found = False
        while (not found):
            tempCost, tempNode, tempPath = self.queue.get()

            self.resultPath = tempPath.append(tempNode)
            self.distance = tempCost - self.heuristicList[tempNode][goalNode]

            if (tempNode == goalNode):
                found = True
            else:
                self.awakenNode(goalNode)

        # Clear the queue and visited set
        while (not self.queue.empty()):
            self.queue.get()
        self.visited.clear()