# Graphs 

**This is a project for my studies. Below is the task translated to english with AI**

Implement tools for computer-based graph generation, visualization, and analysis by implementing the algorithms mentioned below.

**IMPORTANT:** You may use libraries/packages only for graph visualization and the most primitive operations (for example, accessing the neighbors of a given vertex).

Create tools for the **input/generation** of the following types of **simple graphs** (undirected, without loops, and not multi-graphs where two vertices can be connected by more than one edge) with a user-specified number of vertices:

**A complete graph;**
**A k-regular graph (with a user-specified degree parameter k);**
**Any given graph (for example, one drawn on paper);**
**A random graph.**

Also, provide the **ability to assign positive weight coefficients** to the edges of the graph (by default, we will assume they are all equal to 1).

**Visualize** the inputted or generated graph and save the result as a PDF, PNG, or another graphical format file (see .html as result).

Implement the following **shortest path search algorithms**: **BFS** (finds the shortest path between two vertices if all edge weights are equal), **Dijkstra**, **Floyd** (also known as the Floyd-Warshall algorithm). Using the results of the Floyd algorithm, **find**:

1. the vertex in the graph (e.g., the location for building a warehouse in a city) from which the sum of the shortest distances to all other vertices is minimal;

2. the vertex in the graph (e.g., the location for building a fire station in a city) such that the farthest vertex in the graph is as close as possible.
ADDITIONAL (OPTIONAL) TASKS
Additional (optional) tasks for more motivated students, for the successful completion of which you can expect bonuses in the final evaluation for the entire "Graph Theory" section, possibly even exemption from taking the theory exam:

Choose (or generate) and input a graph that is **Eulerian**. Implement an algorithm to search for an **Eulerian cycle**;

**Below is not implemented**

Implement a heuristic algorithm (self-researched on possible heuristics) for finding the shortest Hamiltonian cycle (the shortest traveling salesman route) in a weighted (all edge weights are positive) complete graph. Compare its execution time with that of a complete enumeration algorithm (for a small graph where it is possible to wait for the complete enumeration to finish);

Implement a heuristic algorithm (self-researched on possible heuristics) for finding the chromatic number of the graph and visualize the result by appropriately coloring the graph vertices. Compare the execution time of the algorithm with that of a complete enumeration algorithm (for a small graph where it is possible to wait for the complete enumeration to finish);

Using the LaTeX technical text preparation tool, prepare a short (several pages, including illustrations) report on the work performed and the results obtained, in PDF format.

# Grafai 

Prieš naudojant, suinstaliuokite reikiamus paketus naudodami pip:

```bash
pip install pyvis
```

Programos paleidimas:

```bash
# Atsitiktinis sugeneruotas grafas
python3 example_random_graph.py

# Grafai pagal tipą
python3 example_complete_graph.py
python3 example_euler_graph.py
python3 example_k_regular_graph.py
python3 example_petersen_graph.py

# Rankiniu būdu suvesti arba sugeneruoti grafai, užfiksuoti naudojant `g.print_code_for_graph()`
python3 example_graph_1.py
python3 example_graph_2.py
python3 example_graph_3.py
```

Programos rezultatus ž. failuose `mygraph.html` ir `path.html` naudojant naršyklę.