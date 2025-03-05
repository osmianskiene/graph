from graph import Graph, Edge, print_matrix

g = Graph(10, "regular", [
    Edge(0, 1),
    Edge(0, 4),
    Edge(0, 5, 10),
    Edge(1, 2, 10),
    Edge(1, 6, 10),
    Edge(2, 3, 10),
    Edge(2, 7, 10),
    Edge(3, 4, 10),
    Edge(3, 8, 10),
    Edge(4, 9, 10),
    Edge(5, 7, 10),
    Edge(5, 8, 10),
    Edge(6, 8, 10),
    Edge(6, 9, 10),
    Edge(7, 9, 10)
])

g.draw()
g.find_path_dijkstra(5).draw()
floyd = g.find_path_floyd()
floyd.get_paths(5).draw()

print(g.find_path_dijkstra(5).parent_nodes)
print_matrix(floyd.parent_nodes)
