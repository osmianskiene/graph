from graph import Graph, Edge, print_matrix

g = Graph.create_random(8, 11, 10)
floyd = g.find_path_floyd()

g.print_code_for_graph()
g.draw()

g.find_path_dijkstra(5).draw()
floyd.get_paths(5).draw()

print(g.find_path_dijkstra(5).parent_nodes)
print(floyd.parent_nodes[5])

# Naudodamiesi Floyd algoritmo rezultatais, raskite grafo viršūnę (pavyzdžiui, sandėlio statymo vietą mieste) 
# nuo kurios trumpiausių atstumų iki visų kitų viršūnių suma yra minimali
print(f"Geriausia sandėlio vieta: {floyd.find_best_warehouse_location()}")

# Naudodamiesi Floyd algoritmo rezultatais, raskite grafo viršūnę (pavyzdžiui, gaisrinės statymo vietą mieste) tokią, 
# kad labiausiai nuo jos nutolusi grafo viršūnė būtų kaip įmanoma arčiau
print(f"Geriausia gaisrinės statymo vieta: {floyd.find_best_fire_station_location()}")
