# File : UCS.py
# Contains the class UCS, that are used for
# Finding the shortest path on a graph using the UCS algorithm

from queue import PriorityQueue

class UCS:

    # Constructor
    def __init__(self, adjacency_matrix, start_node, node_name):
        self.adjacency_matrix = adjacency_matrix
        self.start_node = start_node
        self.node_name = node_name
        self.path_result = [] # Notes: 0 means the 1st node, 1 means the 2nd node, etc.
        self.distance = 0

    # Getter
    def getAdjacencyMatrix(self):
        return self.adjacency_matrix
    
    def getStartNode(self):
        return self.start_node
    
    def getPathResult(self):
        return self.path_result
            
    def getDistance(self):
        return self.distance
    
    # Path Result in Alphabets
    def printPathResult(self):
        path_res = ""
        for i in range(0, len(self.path_result)-1):
            path_res += self.node_name[self.path_result[i]] + " - "
        path_res += self.node_name[self.path_result[len(self.path_result)-1]]
        return path_res
    
    # Uniform Cost Search (UCS) Algorithm
    # Find shortest path and distance from start node to goal node    
    def find_path_UCS(self, goal_node):
        visited_nodes = set()
        node_queue = PriorityQueue()
        node_queue.put((0, self.start_node, []))

        # There are still nodes to explore
        while (not node_queue.empty()):
            total_weight, current_node, path = node_queue.get()

            # Reach goal node
            if (current_node == goal_node): 
                self.path_result = path + [current_node]
                self.distance = total_weight
                break
            
            # If the current node is not visited before, add to visited nodes
            if (not (current_node in visited_nodes)):    
                visited_nodes.add(current_node)
                for neighbor_node, edge_weight in enumerate(self.adjacency_matrix[current_node]):
                    if (neighbor_node not in visited_nodes and edge_weight > 0):
                        new_path = path + [current_node]
                        new_distance = total_weight + edge_weight
                        node_queue.put((new_distance, neighbor_node, new_path))