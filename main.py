from graph import Graph
import random


def main():
    # test_basic_graph()
    file_name = ""
    print("Hello, please choose the input file you would want to use: ")
    print("1- graph1k")
    print("2- graph10k")
    print("3- graph100k")
    print("4- graph1m")
    file_opt = int(input())
    if file_opt == 1:
        file_name = "graph1k.txt"
    elif file_opt == 2:
        file_name = "graph10k.txt"
    elif file_opt == 3:
        file_name = "graph100k.txt"
    elif file_opt == 4:
        file_name = "graph1m.txt"
    elif file_opt == 5:
        file_name = "graph.txt"

    graph = read_graph_data_from_text_file(file_name)
    opt = 1

    while opt:
        display_options()
        opt = int(input("Please choose your option: "))
        if opt == 1:
            print_outbound_neighbors(graph)
        elif opt == 2:
            print_inbound_neighbors(graph)
        elif opt == 3:
            get_user_input_for_edge_check(graph)
        elif opt == 4:
            get_user_input_for_adding_a_vertex(graph)
        elif opt == 5:
            get_user_input_for_adding_an_edge(graph)
        elif opt == 6:
            get_user_input_for_inbound_degree(graph)
        elif opt == 7:
            get_user_input_for_outbound_degree(graph)
        elif opt == 8:
            get_the_cost_of_an_edge(graph)
        elif opt == 9:
            get_the_info_for_modifying_the_cost_of_an_edge(graph)
        elif opt == 10:
            get_the_info_for_deleting_a_vertex(graph)
        elif opt == 11:
            get_the_info_for_deleting_an_edge(graph)
        elif opt == 12:
            if graph.number_of_edges() > 0:
                print(graph.number_of_edges())
            else:
                print("There is no edge. \n")
        elif opt == 13:
            if graph.number_of_vertices() > 0:
                print(graph.number_of_vertices())
            else:
                print("There is no vertex. \n")
        elif opt == 14:
            write_to_file(graph)


def get_user_input_for_edge_check(g):
    vertex1 = input("The source vertex you want to check for an edge is: ")
    vertex2 = input("The destination vertex you want to check for an edge is: ")
    if g.is_edge(vertex1, vertex2):
        print("There is an edge between ", vertex1, vertex2)
    else:
        print("There is no edge between ", vertex1, vertex2)


def get_user_input_for_adding_a_vertex(g):
    vertex_to_be_added = input("Please give the vertex you want to add: ")
    try:
        g.add_vertex(vertex_to_be_added)
    except :
        print("The vertex you are trying to add already exists. ")


def get_user_input_for_adding_an_edge(g):
    vertex1 = input("The first vertex you want to add for an edge is: ")
    vertex2 = input("The second vertex you want to add for an edge is: ")
    try:
        g.add_edge(vertex1, vertex2)
    except :
        print("The edge you are trying to add already exists. ")


def get_user_input_for_inbound_degree(g):
    vertex = int(input("The vertex you want the inbound degree for is: "))
    try:
        print(g.in_degree(vertex))
    except :
        print("The vertex does not exist. ")


def get_user_input_for_outbound_degree(g):
    vertex = int(input("The vertex you want the outbound degree for is: "))
    try:
        print(g.out_degree(vertex))
    except :
        print("The vertex does not exist.")


def write_to_file(graph):
    file_name = input("Enter the name of the file to save the graph to: ")
    write_graph_to_text_file(graph,file_name)


def read_graph_data_from_text_file(file_name):
    f = open(file_name, 'r')
    a = f.readline()
    a = a.strip()
    a = a.split()
    n = int(a[0])
    m = int(a[1])
    g = Graph(n)

    for i in range(m):
        a = f.readline()
        a = a.strip()
        a = a.split()
        g.add_edge(int(a[0]), int(a[1]), int(a[2]))

    return g


def write_graph_to_text_file(g, file_name):
    """
    Write the graph to a text file with the specified format:
    n m
    x1 y1 c1
    x2 y2 c2
    ...
    xn yn cn
    where n is the number of vertices, m is the number of edges,
    and xi, yi, ci represent the origin, target, and cost of the ith edge.

    :param g: the graph to be written
    :param file_name: the name of the file to write the graph to
    """
    n = g.number_of_vertices()
    m = g.number_of_edges()

    with open(file_name, 'w') as f:
        f.write(f"{n} {m}\n")
        for source, targets in g.get_out_edges().items():
            for target in targets:
                cost = g.get_cost(source, target) | 0
                f.write(f"{source} {target} {cost}\n")
    print("Graph saved successfully to the ", file_name, " file. \n")

def display_options():
    print("Option 1: Display the outbound neighbours. \n")
    print("Option 2: Display the inbound neighbours. \n")
    print("Option 3: Check if there is an edge between two vertices. \n")
    print("Option 4: Add a vertex. \n")
    print("Option 5: Add an edge between two vertices. \n")
    print("Option 6: Get the inbound degree. \n")
    print("Option 7: Get the outbound degree. \n")
    print("Option 8: Get the cost of an edge. \n")
    print("Option 9: Modify the cost of an edge. \n")
    print("Option 10: Delete a vertex. \n")
    print("Option 11: Delete an edge. \n")
    print("Option 12: Get the number of edges. \n")
    print("Option 13: Get the number of vertices. \n")
    print("Option 14: Save the graph to a text file. \n")


def create_small_graph():
    """
    Function that creates a small graph
    :return: the created graph (with vertices and edges)
    """
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    return g


def create_random_graph(n, m):
    """
    Function that creates a graph with random values
    :param n: the number of vertices
    :param m:
    :return: the created graph (with vertices and edges)
    """
    g = Graph(n)
    while m > 0:
        x = random.randrange(n)
        y = random.randrange(n)
        if g.add_edge(x, y):
            m = m - 1
    return g


def print_outbound_neighbors(g):
    print("Outbound:")
    for x in g.parse_vertices():
        print(f"{x}:", end='')
        for y in g.parse_nout(x):
            print(f" {y}", end='')
        print()


def print_inbound_neighbors(g):
    print("Inbound:")
    for x in g.parse_vertices():
        print(f"{x}:", end='')
        for y in g.parse_nin(x):
            print(f" {y}", end='')
        print()


def get_the_cost_of_an_edge(graph):
    x = int(input('Vertex 1: '))
    y = int(input('Vertex 2: '))
    try:
        print(graph.get_cost(x, y))
    except:
        print("The edge does not exist. \n")


def get_the_info_for_modifying_the_cost_of_an_edge(graph):
    x = int(input('Vertex 1: '))
    y = int(input('Vertex 2: '))
    c = int(input('Cost: '))
    try:
        graph.change_cost(x, y, c)
    except ValueError:
        print("The edge does not exist.")


def get_the_info_for_deleting_a_vertex(graph):
    x = int(input('Vertex 1: '))
    try:
        graph.remove_vertex(x)
    except ValueError:
        print("The vertex does not exist.")


def get_the_info_for_deleting_an_edge(graph):
    x = int(input('Vertex 1: '))
    y = int(input('Vertex 2: '))

    try:
        graph.remove_edge(x, y)
    except:
        print("The edge you are trying to remove does not exist. \n")


def test_basic_graph():
    g = create_small_graph()
    # g = create_random_graph(4, 1)
    print_inbound_neighbors(g)
    print_outbound_neighbors(g)


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
