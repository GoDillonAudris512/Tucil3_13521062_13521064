# File : GraphDrawer.py
# Contains the class GraphDrawer, that are used for
# Draw a graph or a graph with result path and save it as a file, 

import matplotlib.pyplot as plt
import networkx as nx

class GraphDrawer:

    # CONSTRUCTOR
    # Construct and initialize the object
    def __init__(self, nodeName, row, map):
        self.nodeName = nodeName
        self.graph = nx.Graph()
        # Add the node to graph
        for i in range (len(self.nodeName)):
            self.graph.add_node(f"{i+1} - {self.nodeName[i]}")

        # Add the edge and its weight to graph
        for i in range(row):
            for j in range(i, row):
                if (map[i][j] != 0):
                    self.graph.add_edge(f"{i+1} - {self.nodeName[i]}", f"{j+1} - {self.nodeName[j]}", weight=map[i][j])
                    self.graph.add_edge(f"{j+1} - {self.nodeName[j]}", f"{i+1} - {self.nodeName[i]}", weight=map[j][i])

    # TRANSFORMER  
    # Transform the result path into list of edges needed
    def transformResultPath(self, resultPath):
        edgeList = []
        for i in range(len(resultPath)-1):
            edgeList.append((f"{resultPath[i] + 1} - {self.nodeName[resultPath[i]]}", f"{resultPath[i+1] + 1} - {self.nodeName[resultPath[i+1]]}"))
            edgeList.append((f"{resultPath[i+1] + 1} - {self.nodeName[resultPath[i+1]]}", f"{resultPath[i] + 1} - {self.nodeName[resultPath[i]]}"))
        return edgeList

    # DRAWER
    # Draw a graph based on its nodes, edges, and node's name
    def drawGraph(self):
        # Create the image of graph and save it
        edges = [(u, v) for (u, v, d) in self.graph.edges(data=True)]
        edge_labels = nx.get_edge_attributes(self.graph, "weight")
        try:
            pos = nx.planar_layout(self.graph)
        except:
            pos = nx.spring_layout(self.graph, seed=len(self.nodeName))

        nx.draw_networkx_nodes(self.graph, pos, node_size=350, node_color="#EE1AEF")
        nx.draw_networkx_labels(self.graph, pos, font_size=12, font_family="monospace")
        nx.draw_networkx_edges(self.graph, pos, edgelist=edges, width=2)
        if (len(self.nodeName) < 15):
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels, rotate=False)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.savefig("../assets/graph.png")
        plt.close("all")

    # Draw a graph based on its nodes, edges, node's name, and highlight the result path
    def drawGraphResult(self, resultPath):
        # Get all the result edge
        resultEdge = self.transformResultPath(resultPath)

        # Create the image of graph and save it
        normalEdges = [(u, v) for (u, v, d) in self.graph.edges(data=True) if (u, v) not in resultEdge]
        resultEdges = [(u, v) for (u, v, d) in self.graph.edges(data=True) if (u, v) in resultEdge]
        edge_labels = nx.get_edge_attributes(self.graph, "weight")
        try:
            pos = nx.planar_layout(self.graph)
        except:
            pos = nx.spring_layout(self.graph, seed=len(self.nodeName))

        nx.draw_networkx_nodes(self.graph, pos, node_size=350, node_color="#EE1AEF")
        nx.draw_networkx_labels(self.graph, pos, font_size=12, font_family="monospace")
        nx.draw_networkx_edges(self.graph, pos, edgelist=normalEdges, width=2, edge_color="#000000")
        nx.draw_networkx_edges(self.graph, pos, edgelist=resultEdges, width=2, edge_color="#FF1100")
        if (len(self.nodeName) < 15):
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels, rotate=False)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.savefig("../assets/graph.png")
        plt.close("all")