import graphviz
import pydotplus
import pygraphviz
import graphtools as gt
from graphviz import render
import os, sys

base_graph = pydotplus.graph_from_dot_file("test_files/btman_20801.dot")
second_graph = pydotplus.graph_from_dot_file("test_files/btman_20807.dot")


def create_node_list(graph):
    nodes = []
    for node in graph.get_nodes():
        nodes.append(gt.Node(node.get_name().replace('"', "")))

    return nodes


def create_edge_list(graph):
    edges = []
    for edge in graph.get_edges():
        labels = edge.obj_dict["attributes"]["label"].split("\\n")
        label = labels[1].replace('"', "").replace(" ", "")

        edges.append(gt.Edge(edge.get_source().replace('"', ""),
                             edge.get_destination().replace('"', ""),
                             label))

    return edges


def create_graph(graph):
    g = graphviz.Digraph()
    for node in graph.nodes:
        g.node(node.name, node.name, color=node.mark, fillcolor="#ffbb33")
    for edge in graph.edges:
        g.edge(edge.start, edge.end, color=edge.mark)

    gr = g.source
    file = open("random.dot", "w")
    file.write(gr)
    file.close()
    os.system('dot -Tpng random.dot -o random.png')


def main():
    nodes = create_node_list(base_graph)
    edges = create_edge_list(base_graph)
    al1 = gt.Graph(nodes, edges)
    nodes2 = create_node_list(second_graph)
    edges2 = create_edge_list(second_graph)
    al2 = gt.Graph(nodes2, edges2)
    print(al1, "\n", al2)

    for i in al1.compare(al2).nodes:
        print(i, i.mark)
    for j in al1.compare(al2).edges:
        print(j, j.mark)

    create_graph(al1.compare(al2))


if __name__ == '__main__':
    main()
