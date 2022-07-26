import graphviz
import pydotplus
import graphtools as gt

base_graph = pydotplus.graph_from_dot_file("test_files/btman_18903.dot")
second_graph = pydotplus.graph_from_dot_file("test_files/btman_18897.dot")


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


def main():
    nodes = create_node_list(base_graph)
    edges = create_edge_list(base_graph)
    al1 = gt.Graph(nodes, edges)
    nodes2 = create_node_list(second_graph)
    edges2 = create_edge_list(second_graph)
    al2 = gt.Graph(nodes2, edges2)
    print(al1, "\n", al2)
    al1.compare(al2)



if __name__ == '__main__':
    main()
