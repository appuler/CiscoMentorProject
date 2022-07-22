import graphviz, pydotplus

graphs = pydotplus.graph_from_dot_file("../test_files/btman_19349.dot")
print(graphs.to_string())

for node in graphs.get_nodes():
    print(node.get_name())
    print(node.to_string())
    print(node.obj_dict)

print()
for edge in graphs.get_edges():
    print(edge.get_source())
    print(edge.get_destination())
    print(edge.to_string())
    print(edge.obj_dict)

print()