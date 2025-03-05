from graph import Graph, Edge, print_matrix

g = Graph.create_k_regular(8, 3) # at least one of them must be even number
g.draw()
g.find_path_bfs(2).draw()
