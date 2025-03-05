from graph import Graph, Edge, print_matrix

# euler_graph = Graph.create_complete(5)
euler_graph = Graph.create_k_regular(9, 4)
euler_graph.draw()
print(euler_graph.find_cycle_euler())
