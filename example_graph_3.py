from graph import Graph, Edge, print_matrix

g = Graph(8, 'regular', [
    Edge(2, 4, 9),
    Edge(2, 7, 3),
    Edge(0, 2, 9),
    Edge(3, 6, 2),
    Edge(4, 7, 4),
    Edge(2, 6, 5),
    Edge(0, 1, 5),
    Edge(2, 3, 1),
    Edge(1, 3, 1),
    Edge(5, 7, 7),
    Edge(2, 5, 7),
])
floyd = g.find_path_floyd(debug=False)

g.draw()
# g.find_path_dijkstra(5).draw()
floyd.get_paths(5).draw()

print(g.find_path_dijkstra(5).parent_nodes)
print("Distances:")
print_matrix(floyd.distances)
print("Parents:")
print_matrix(floyd.parent_nodes)

# Naudodamiesi Floyd algoritmo rezultatais, raskite grafo viršūnę (pavyzdžiui, sandėlio statymo vietą mieste) 
# nuo kurios trumpiausių atstumų iki visų kitų viršūnių suma yra minimali
print(f"Geriausia sandėlio vieta: {floyd.find_best_warehouse_location()}")

# Naudodamiesi Floyd algoritmo rezultatais, raskite grafo viršūnę (pavyzdžiui, gaisrinės statymo vietą mieste) tokią, 
# kad labiausiai nuo jos nutolusi grafo viršūnė būtų kaip įmanoma arčiau
print(f"Geriausia gaisrinės statymo vieta: {floyd.find_best_fire_station_location()}")
