import graphviz
import pydotplus


class AdjacencyList:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.adj_list = {}

        for node in nodes:
            self.adj_list[node] = []

        for edge in edges:
            self.adj_list[edge.start].append(edge)

    def __str__(self):
        return self.adj_list

    def __repr__(self):
        return self.adj_list

    def order(self):
        pass
