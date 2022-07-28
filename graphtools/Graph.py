import graphviz
import pydotplus


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.adj_list = {}

        for node in nodes:
            self.adj_list[node.name] = []

        for edge in edges:
            self.adj_list[edge.start].append(edge)

        self.nodes_copy = self.nodes.copy()
        self.edges_copy = self.edges.copy()
        self.copy = self.adj_list.copy()


    def __str__(self):
        return f'{self.adj_list}'

    def __repr__(self):
        return self.adj_list

    def order(self):
        for i in self.adj_list.keys():
            self.adj_list[i].sort()

    def compare(self, other):

        nodes = self.nodes.copy()
        edges = self.edges.copy()
        other_nodes = other.nodes.copy()
        other_edges = other.edges.copy()

        if other_nodes != nodes:
            a = set(nodes)
            b = set(other_nodes)
            for i in list(a.difference(b)):
                i.mark = "red"

            for i in list(b.difference(a)):
                i.mark = "green"

        for i in edges:
            if i not in other_edges:
                i.mark = "red"

        for i in other_edges:
            if i not in edges:
                i.mark = "green"

        a = set(nodes)
        b = set(edges)
        c = set(other_nodes)
        d = set(other_edges)

        return Graph(list(a.union(c)), list(b.union(d)))







