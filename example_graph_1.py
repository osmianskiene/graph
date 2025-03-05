from graph import Graph, Edge, print_matrix

g = Graph.create_any(5, [
    Edge(0, 1),
    Edge(0, 2),
    Edge(0, 3),
    Edge(0, 4),
    Edge(1, 2),
    Edge(1, 3),
    Edge(1, 4),
    Edge(2, 3),
    Edge(2, 4),
    Edge(3, 4)
])
