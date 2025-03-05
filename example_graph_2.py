from graph import Graph, Edge, print_matrix

g = Graph(8, 'regular', [
    Edge(1, 6, 2),
    Edge(1, 2, 1),
    Edge(3, 6, 9),
    Edge(5, 7, 4),
    Edge(2, 3, 2),
    Edge(0, 1, 2),
    Edge(5, 6, 4),
    Edge(1, 3, 1),
    Edge(1, 7, 3),
    Edge(6, 7, 9),
    Edge(0, 3, 2),
])

g.draw()
# graph1.find_path_dijkstra(5).draw()
floyd = g.find_path_floyd()
floyd.get_paths(5).draw()

print(g.find_path_dijkstra(5).parent_nodes)
print_matrix(floyd.parent_nodes)
