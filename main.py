import graphviz
import pydotplus
import graphtools as gt

base_graph = pydotplus.graph_from_dot_file("test_files/btman_18897.dot")


def create_node_list(graph):
    nodes = []
    for node in graph.get_nodes():
        nodes.append(gt.Node(node.get_name()))

    return nodes


def create_edge_list(graph):
    edges = []
    for edge in graph.get_edges():
        labels = edge.obj_dict["attributes"]["label"].split("\\n")
        label = labels[1].replace('"', "").replace(" ", "")

        edges.append(gt.Edge(edge.get_source(),
                             edge.get_destination(),
                             label))

    return edges


def main():
    nodes = create_node_list(base_graph)
    edges = create_edge_list(base_graph)
    print(nodes)
    print(edges)


if __name__ == '__main__':
    main()
