# Realizuokite kompiuterinius grafų generavimo, vizualizavimo bei analizės (įgyvendindami toliau paminėtus algoritmus) instrumentus.
# SVARBU: bibliotekas/paketus galite naudoti tik grafų vizualizavimui ir primityviausioms operacijoms (pavyzdžiui, duotosios viršūnės kaimynų pasiekimui).

# Sukurkite šių paprastųjų (neorientuotų, be kilpų ir ne multi-grafų, kuriuose dvi viršūnes gali jungti daugiau nei viena briauna) grafų (su vartotojo nurodomu viršūnių skaičiumi) tipų įvedimo/generavimo priemones:

#       pilnojo grafo;
#       k-reguliariojo (su vartotojo nurodomu laipsnio k parametru) grafo;
#       bet kokio duoto (pavyzdžiui, nubraižyto ant popieriaus lapo) grafo;
#       atsitiktinio grafo.

# Taip pat numatykite teigiamų svorių koeficientų (pagal nutylėjimą laikysime, kad jie visi lygūs 1) priskyrimo grafo briaunoms galimybę.

# Vizualizuokite įvestą arba sugeneruotą grafą, rezultatą išsaugokite kaip PDF, PNG ar kito grafinio formato bylą.

# Realizuokite šiuos trumpiausių kelių paieškos algoritmus: BFS (randa trumpiausią kelią tarp dviejų viršūnių, jeigu visų briaunų svoriai vienodi), Dijkstra, Floyd (dar žinomas kaip Floyd-Warshall algoritmas).
# Naudodamiesi Floyd algoritmo rezultatais, raskite:
#       a) grafo viršūnę (pavyzdžiui, sandėlio statymo vietą mieste) nuo kurios trumpiausių atstumų iki visų kitų viršūnių suma yra minimali;
#       b) grafo viršūnę (pavyzdžiui, gaisrinės statymo vietą mieste) tokią, kad labiausiai nuo jos nutolusi grafo viršūnė būtų kaip įmanoma arčiau.

# PAPILDOMAI
# Papildomi (neprivalomi) darbai labiau motyvuotiems studentams už kurių bent dalies sėkmingą įgyvendinimą galite tikėtis bonusų, rašant galutinį vertinimą už visą "Grafų teorijos" dalį, galbūt netgi atleidžiant nuo teorijos egzamino laikymo:

#       pasirinkite (arba sugeneruokite) ir įveskite grafą, kuris būtų Oilerio. Realizuokite Oilerio ciklo paieškos algoritmą;
#       realizuokite euristinį (savarankiškai susiradę informaciją apie galimas euristikas) mažiausio ilgio Hamiltono ciklo (trumpiausio keliaujančio pirklio maršruto) paieškos algoritmą svertiniame (visi briaunų svoriai teigiami) pilnajame grafe. Palyginkite jo veikimo trukmę su pilno perrinkimo algoritmo veikimo trukme (nedideliam grafui, kuriam įmanoma sulaukti pilno perrinkimo pabaigos);
#       realizuokite euristinį (savarankiškai susiradę informaciją apie galimas euristikas) grafo chromatinio skaičiaus radimo algoritmą bei vizualizuokite rezultatą atitinkamai nuspalvindami grafo viršūnes. Palyginkite algoritmo veikimo trukmę su pilno perrinkimo algoritmo veikimo trukme (nedideliam grafui, kuriam įmanoma sulaukti pilno perrinkimo pabaigos);
#       panaudodami LaTeX techninių tekstų ruošimo įrankį, parenkite trumpą (keleto puslapių apimties, įskaitant iliustracijas) vykdytų darbų ir gautų rezultatų aprašą PDF formatu.

import math
import random
from pyvis.network import Network

# Reprezenduoja grafą
class Graph:
    #region Grafo sukurimas
    def __init__(self, node_count, type, edges):
        self.node_count = node_count
        self.type = type
        self.edges = edges

    def copy(self):
        return Graph(self.node_count, self.type, self.edges.copy())

    def create_complete(node_count):
        edges = []

        for i in range(node_count):
            for j in range (i + 1, node_count):
                edges.append(Edge(i, j))

        return Graph(node_count, 'complete', edges)
        
    def create_k_regular(node_count, degree, max_weight=2): 
        # If k=2m
        #  is even, put all the vertices around a circle, and join each to its m
        #  nearest neighbors on either side.

        # If k=2m+1
        #  is odd, and n
        #  is even, put the vertices on a circle, join each to its m
        #  nearest neighbors on each side, and also to the vertex directly opposite.

        # Handshaking Lemma -------------------------------------------
        # The Handshaking Lemma states that in any graph, the sum of the degrees of all vertices is equal to twice the number of edges. 
        # The sum of degrees of all vertices (i.e., n × k for a k-regular graph) must be even because it is equal to  2 × number of edges, which is naturally even.

        edges = []
        m = degree // 2

        for i in range(node_count):
            for j in range(i + 1, i + m + 1):
                edge = Edge.create_sorted(i, j % node_count, random.randrange(1, max_weight))

                if not edge.in_array(edges):
                    edges.append(edge)

            for j in range(i - 1, i - m - 1, -1):
                edge = Edge.create_sorted(i, j % node_count, random.randrange(1, max_weight))

                if not edge.in_array(edges):
                    edges.append(edge)
        
            if degree % 2 != 0:
                edge = Edge.create_sorted(i, (i + node_count // 2) % node_count, random.randrange(1, max_weight))

                if not edge.in_array(edges):
                    edges.append(edge)

        return Graph(node_count, 'k_regular', edges)

    def create_any(node_count, edges):
        return Graph(node_count, 'any', edges)

    def create_random(node_count, edge_count, max_weight=2):
        edges = []

        while len(edges) < edge_count:
            from_node = random.randrange(node_count)
            to_node = random.randrange(node_count)
            weight = random.randrange(1, max_weight)

            if (to_node == from_node):
                continue

            edge = Edge.create_sorted(from_node, to_node, weight)
            
            if not edge.in_array(edges):
                    edges.append(edge)

        return Graph(node_count, 'random', edges)

    #endregion

    #region Grafo vizualizavimas
    def draw(self, filename='mygraph.html'):
        net = Network(height="750px", width="100%", font_color="black")

        for i in range(self.node_count):
            net.add_node(i, label=f'{i}', shape="circle", physics=False, labelHighlightBold=True)

        for edge in self.edges:
            net.add_edge(edge.from_node, edge.to_node, label=f"{edge.weight}")

        # net.show_buttons(["manipulation"])
        net.options.interaction.hover = True
        net.write_html(filename)
    #endregion

    #region Pagalbiniai
    def create_adjacency_matrix(self):
        matrix = [[math.inf for x in range(self.node_count)] for y in range(self.node_count)]

        # Atstumas iš viršūnės iki jos pačios yra 0 - tai yra reikšmės pagrindinėje įstrižainėje
        for i in range(self.node_count):
            matrix[i][i] = 0

        # Įrašome atstumus, kuomet viršūnes tiesiogiai sujungtos briauna
        for edge in self.edges:
            matrix[edge.from_node][edge.to_node] = edge.weight
            matrix[edge.to_node][edge.from_node] = edge.weight

        return matrix

    def find_neighbours(self, node):
        neighbours = []

        for edge in self.edges:
            if edge.from_node == node:
                neighbours.append(edge.to_node)
            elif edge.to_node == node:
                neighbours.append(edge.from_node)

        return neighbours


    def find_weighted_neighbours(self, node):
        """
        Randa duotos viršūnės kaimynus ir jų svorius

        Args:
            node (int): Viršūnės numeris

        Returns:
            list[WeightedNode]: Sąrašas su kaimynų numeriais ir jų svoriais
        """

        weighted_nodes = []

        for edge in self.edges:
            if edge.from_node == node:
                weighted_nodes.append(WeightedNode(edge.to_node, edge.weight))
            elif edge.to_node == node:
                weighted_nodes.append(WeightedNode(edge.from_node, edge.weight))

        return weighted_nodes

    def print_code_for_graph(self):
        print(f"graph1 = Graph({self.node_count}, 'regular', [")
        for edge in self.edges:
            print(f"    Edge({edge.from_node}, {edge.to_node}, {edge.weight}),")
        print(f"])")

    #endregion

    #region Trumpiausio kelio paieška
    def find_path_bfs(self, from_node):
        # Iš esmės tai BFS algoritmas iš skaidrių, tik skirtingi kintamųjų pavadinimai:
        #
        # - `G` -> `self`
        # - `u` -> `from_node`
        # - `dist` -> `distances`
        # - `ScanQ` -> `queue`
        #
        # Dar skirtumai:
        #
        # - Taip pat įsimename `parent_nodes` masyvą, kuris viekvienai viršūnei `v` saugo viršūnę iš kurios buvo ateita, einant trumpiausiu keliu iš `from_node`. Vėliau šis masyvas naudojamas trumpiausią kelio vizualizavimui.
        # - Skaidrėse, sąlygoje `if w not on ScanQ` yra loginė klaida, kurią iliustruoja šis pavydzys. Tarkime, turime kvadratą (viršūnės 0, 1, 2, 3 i6d4liotos ant apskritimo ir kaimynės sujungtos), ir ieškome trumpiausio kelio iš viršūnės 0. Pradžioje eilėje `ScanQ` yra 0, po pirmo ciklo 0 išimamas ir įdedami 0 kaimynai, t.y. 1 ir 3. Po antro ciklo 1 ir 3 išimami, ir įdedami kiekvieno iš jų kaimynai, t.y. 0 ir 2. Tokiu būdu, gauname amžiną ciklą. Sprendimas yra dėti į eilę tik neapeitas viršūnes. Kad ištaisyti šią klaidą, atitinkamą sąlygą `if not w in queue` papildžiau taip: `if not w in queue and distances[w] == math.inf`.

        distances = [math.inf for x in range(self.node_count)]
        parent_nodes = [None for x in range(self.node_count)]
        distances[from_node] = 0
        queue = [from_node]

        while len(queue) > 0:
            v = queue.pop(0)

            for neighbour_node in self.find_neighbours(v):
                # Pridedame į eilę tik neapeitas viršūnes
                if not neighbour_node in queue and distances[neighbour_node] == math.inf:
                    queue.append(neighbour_node)
                    distances[neighbour_node] = distances[v] + 1
                    parent_nodes[neighbour_node] = v

        return Paths(self.node_count, distances, parent_nodes)

    def find_path_dijkstra(self, from_node):
        # Inicializuojame taip pat kaip ir BFS algoritme
        distances = [math.inf] * self.node_count
        parent_nodes = [None] * self.node_count
        unvisited_nodes = set(range(self.node_count))
        distances[from_node] = 0

        # Pradedame algoritmą nuo pradinės viršūnės
        current_node = from_node

        # Kartojame algoritmą, kol neišrinkame visų viršūnių
        while current_node != None:
            unvisited_nodes.remove(current_node)

            # Einame per visas "nefinalizuotas" `current_node` kaimynes
            for neighbour in self.find_weighted_neighbours(current_node):
                if not neighbour.node in unvisited_nodes:
                    continue

                # Jei kaimyno kelias per `current_node` yra trumpesnis nei dabartinis trumpiausias kelias, 
                # tai atnaujiname jo `distances` ir `parent_nodes` reikšmes. Čia verta pastebėti, kad 
                # iš pradžių `distances[neighbour.node]` reikšmė yra `math.inf`, tad pirmą kartą apeinant šią
                # viršūnę, šio `if` sąlyga bus visada `True`.
                if distances[neighbour.node] > distances[current_node] + neighbour.weight:
                    distances[neighbour.node] = distances[current_node] + neighbour.weight
                    parent_nodes[neighbour.node] = current_node

            # Tarp visų neaplankytų viršūnių, surandame artimiausią pradinei viršūnei
            closest_neighbour_node = None
            for node in unvisited_nodes:
                if closest_neighbour_node == None or distances[node] < distances[closest_neighbour_node]:
                    closest_neighbour_node = node

            # Per kitą algoritmo ciklą rastą artimiausią viršūnę nustatome kaip `current_node`. Tai gali būti ir `None`,
            # kas lems išėjimą iš pagrindinio ciklo
            current_node = closest_neighbour_node

        return Paths(self.node_count, distances, parent_nodes)

    def find_path_floyd(self, debug=False):
        # Skirtingai nuo BFS ir Dijkstra, čia mes operuojame 2-mačiais `distances` ir `parent_nodes` masyvais, o ne 1-mačiais.
        # `distances[y][x]` yra trumpiausias atstumas iš viršūnės `y` į viršūnę `x` (pradinės reikšmės yra `math.inf`), o
        # `parent_nodes[y][x]` yra viršūnė, iš kurios buvo ateita, einant trumpiausiu keliu iš `y` į `x` (pradinės reikšmės yra `x`). Čia `x` žymime matricos stulpelį, o `y` - eilutę.
        distances = self.create_adjacency_matrix()
        parent_nodes = [[x for x in range(self.node_count)] for y in range(self.node_count)]

        # Pabaigėme pasiruošimus, pradedame pagrindinį Floyd algoritmo ciklą, kurio kiekvienoje iteracijoje 
        # mes pažymime (highlight) i-ajį stulpelį ir į-ają eilutę, ir bandome pildyti likusias reikšmes.
        for i in range(self.node_count):
            if debug:
                print(f"Iteration {i}\n-------------------------------------------------------------")
                print("distances")
                print_matrix(distances)
                print("parent_nodes")
                print_matrix(parent_nodes)
                print("assignments")

            # Begame per visus `distances[y][x]`, išskyrus i-ąją eilutę ir i-ąjį stulpelį ir išskyrus pagrindinę įstrižainę
            for y in range(self.node_count):
                for x in range(self.node_count):
                    # Praleidžiame i-ąją eilutę ir i-ąjį stulpelį
                    if x == i or y == i:
                        continue

                    # Praleidžiame pagrindinę įstrižainę
                    if x == y:
                        continue

                    # Štai, čia visa magija :D

                    # Jeigu iš `y` į `x` kelias per `i` yra trumpesnis nei dabartinis trumpiausias kelias,
                    # tai atnaujiname jo `distances` ir `parent_nodes` reikšmes taip, kad `i` būtų `y -> x` kelyje.
                    if distances[y][x] > distances[y][i] + distances[i][x]:
                        if debug:
                            print(f"{y}->{x} per {i}: {distances[y][x]} > {distances[y][i]} + {distances[i][x]}")

                        distances[y][x] = distances[y][i] + distances[i][x]
                        parent_nodes[y][x] = i

        return FloydMatrices(self.node_count, distances, parent_nodes)

    #endregion

    #region Oilerio ciklas

    def find_cycle_euler(self):
        # Pradžiai, patikriname ar visų viršūnių laipsniai yra lyginiai - kitaip Oilerio ciklo nėra
        for node in range(self.node_count):
            degree = len(self.find_neighbours(node))

            if degree == 0 or degree % 2 != 0:
                return None

        # Toliau, pagal skaidres
        used_edges = set()

        tour = None
        for start_node in range(self.node_count):
            sub_tour = self.find_euler_sub_tour(start_node, used_edges)

            while sub_tour:
                tour = self.merge_euler_tours(tour, sub_tour)
                sub_tour = self.find_euler_sub_tour(start_node, used_edges)

        if len(used_edges) == len(self.edges):
            return tour
        else:
            return None

    # Randa sub-tour'ą, kuris prasideda nuo `start_node`, arba None, jei tokio iš nepanaudotų briaunų nepavyksta sukurti
    def find_euler_sub_tour(self, start_node, used_edges):
        tour = []
        current_node = start_node

        while True:
            tour.append(current_node)

            next_node = None

            for edge in self.edges: 
                if edge in used_edges:
                    continue

                if edge.from_node == current_node:
                    next_node = edge.to_node
                    used_edges.add(edge)
                    break
                elif edge.to_node == current_node:
                    next_node = edge.from_node
                    used_edges.add(edge)
                    break

            if next_node == None:
                return None

            current_node = next_node

            if current_node == start_node:
                tour.append(current_node)
                break

        return tour

    def merge_euler_tours(self, target_tour, source_tour):
        if target_tour == None:
            return source_tour
        
        for i in range(len(target_tour)):
            if target_tour[i] == source_tour[0]:
                return target_tour[:i] + source_tour + target_tour[i + 1:]

        return None

    #endregion

# Reprezenduoja grafo briauną
class Edge:
    #region Briaunos sukurimas
    def __init__(self, from_node, to_node, weight=1):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def create_sorted(from_node, to_node, weight=1):
        if from_node <= to_node:
            return Edge(from_node, to_node, weight)
        else:
            return Edge(to_node, from_node, weight)
    #endregion

    #region Pagalbiniai
    def in_array(self, edges):
        for edge in edges:
            if self.equals(edge):
                return True
        
        return False

    def equals(self, edge):
        return self.from_node == edge.from_node and self.to_node == edge.to_node
    #endregion

    def __repr__(self):
        return f"{self.from_node} -> {self.to_node} ({self.weight})"

# Reprezenduoja trumpiausią kelią iš duotos viršūnės iki visų kitų viršūnių
class Paths:
    def __init__(self, node_count, distances, parent_nodes):
        self.distances = distances
        self.parent_nodes = parent_nodes
        self.node_count = node_count

    def draw(self, filename='path.html'):
        edges = []

        for i in range(len(self.parent_nodes)):
            if self.parent_nodes[i] != None:
                edges.append(Edge.create_sorted(i, self.parent_nodes[i], self.distances[i]))
        
        path_graph = Graph.create_any(self.node_count, edges)
        path_graph.draw(filename)

class FloydMatrices:
    def __init__(self, node_count, distances, parent_nodes):
        self.distances = distances
        self.parent_nodes = parent_nodes
        self.node_count = node_count

    def get_paths(self, from_node):
        # Čia mes turime konvertuoti Floyd algoritmo `parent_nodes` į tokį kurį mes gautume iš BFS arba Dijkstra algoritmo.
        # 
        # `self.parent_nodes[y][x]` Floyd algoritme yra _kažkuri_ viršūnė kelyje iš `y` į `x`. Tarkime, kad tai yra `i`.
        # Tuomet kita _kažkuri_ viršūnė yra `self.parent_nodes[y][i]`. Ir taip toliau, kol self.parent_nodes[y][i] != i.
        # 
        # Tuo tarpu BFS arba Dijkstra algoritmo `parent_nodes[i]` yra paskutinė viršūnė kelyje iš `from_node` į `i`.
        # 
        # Paimkime pvz. `parent_nodes` randant trumpiausius kelius iš viršūnės 5:
        #
        # - Dijkstra algoritmo `parent_nodes` : `[1, 6, 1, 1, None, None, 5, 5]`
        # - Floyd algoritmo `parent_nodes`:
        #     0     1     1     3     4     6     1     1
        #     0     1     2     3     4     6     6     7
        #     1     1     2     3     4     6     1     1
        #     0     1     2     3     4     6     1     1
        #     0     1     2     3     4     5     6     7
        #     6     6     6     6     4     5     6     7
        #     1     1     1     1     4     5     6     1
        #     1     1     1     1     4     5     1     7
        # 
        # Taigi, norint konvertuoti Floyd algoritmo `parent_nodes` į BFS arba Dijkstra algoritmo `parent_nodes`,
        # reikia sekti kitą viršūnę per `self.parent_nodes` matricą.
        distances = self.distances[from_node]
        parent_nodes = [None] * self.node_count
        queue = [from_node]

        while len(queue) > 0:
            v = queue.pop(0)

            for i in range(self.node_count):
                if i != from_node and self.distances[v][i] != math.inf and parent_nodes[i] == None and self.parent_nodes[v][i] == i:
                    queue.append(i)
                    parent_nodes[i] = v

        return Paths(self.node_count, distances, parent_nodes)

    #region Papildomi uždaviniai
    def find_best_warehouse_location(self):
        # Naudodamiesi Floyd algoritmo rezultatais, raskite grafo viršūnę (pavyzdžiui, sandėlio statymo vietą mieste) nuo kurios trumpiausių atstumų iki visų kitų viršūnių suma yra minimali
        #
        # Floyd atstumo matricoje, `distances[y][x]` yra trumpiausias atstumas iš viršūnės `y` į viršūnę `x`. Ieškome tokio `y`, kad `sum(distances[y])` būtų minimalus.
        node = None
        shortest_total_distance = math.inf

        for y in range(self.node_count):
            total_distance = sum(self.distances[y])

            if total_distance < shortest_total_distance:
                shortest_total_distance = total_distance
                node = y

        return node

    def find_best_fire_station_location(self):
        # Naudodamiesi Floyd algoritmo rezultatais, raskite grafo viršūnę (pavyzdžiui, gaisrinės statymo vietą mieste) tokią, kad labiausiai nuo jos nutolusi grafo viršūnė būtų kaip įmanoma arčiau
        #
        # Floyd atstumo matricoje, `distances[y][x]` yra trumpiausias atstumas iš viršūnės `y` į viršūnę `x`. Ieškome tokio `y`, kad `max(distances[y])` būtų minimalus.
        node = None
        shortest_max_distance = math.inf

        for y in range(self.node_count):
            max_distance = max(self.distances[y])

            if max_distance < shortest_max_distance:
                shortest_max_distance = max_distance
                node = y

        return node
    #endregion

class WeightedNode:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

def print_matrix(matrix):
    n = len(matrix)
    
    # Spausdiname stulpelių indeksus
    print("     ", end="")  # Vieta eilučių indeksams
    for j in range(n):
        print(f"{str(j).rjust(6)}", end="")
    print()
    
    # Spausdiname skiriamąją liniją
    print("     " + "-" * (6 * n))
    
    # Spausdiname eilutes su eilučių indeksais
    for i in range(n):
        print(f"{str(i).rjust(3)} |", end="")
        for j in range(n):
            val = matrix[i][j]
            if val == math.inf:
                val_str = "inf"
            else:
                val_str = str(val)
            print(f"{val_str.rjust(6)}", end="")
        print()
