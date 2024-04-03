from copy import deepcopy


class Graph:
    def __init__(self, n=0):
        """
        Function that constructs a graph with n vertices numbered from 0 to n and no edges
        :param n: the number of vertices
        """
        self.__number_of_vertices = n
        self.__in_edges = {}
        for i in range(n):
            self.__in_edges[i] = []
        self.__out_edges = {}
        for i in range(n):
            self.__out_edges[i] = []
        self.__costs = {}

    def is_vertex(self, val):
        if val in self.__out_edges.keys():
            return True
        return False

    def add_vertex(self, x):
        """
        Function that inserts the vertex into the graph.
        :param x: x - the vertex to be added (one that doesn't already exist)
        :return: -
        """
        if self.is_vertex(int(x)):
            raise ValueError("The vertex you are trying to add already exists. ")

        self.__in_edges[x] = []
        self.__out_edges[x] = []

    def add_edge(self, x, y, c=0):
        """
        Function that adds an edge from vertex x to vertex y and returns True.
        :param c: the cost of the new edge
        :param x: a vertex that is valid
        :param y: a vertex tht is valid
        :return: -, if the edge can be successfully added between x and y
        :raise: ValueError, if the edge already exists
        """
        y = int(y)
        x = int(x)
        if y in self.__out_edges[x]:
            raise ValueError
        self.__costs[(x, y)] = c
        self.__out_edges[x].append(y)
        self.__in_edges[y].append(x)

    def is_edge(self, x, y):
        """
        Function that checks if there is an edge between two vertices
        :param x: a valid vertex
        :param y: a valid vertex
        :return: True if there is an edge from x to y in the graph
                 False, otherwise
        """
        if int(y) in self.__out_edges[int(x)]:
            return True
        else:
            return False

    def parse_nout(self, x):
        """
        Function that, given a vertex x, will return all the outbound neighbors
        :param x:
        :return: an iterable that contains all the outbound neighbors of vertex x
        """
        return set(self.__out_edges[x])

    def parse_nin(self, x):
        """
        Function that, given a vertex x, will return all the inbound neighbors
        :param x:
        :return: an iterable that contains all the inbound neighbors of vertex x
        """
        return set(self.__in_edges[x])

    def parse_vertices(self):
        """
        :return: iterable that contains all the vertices of the graph
        """
        return set(self.__in_edges.keys())

    def get_out_edges(self):
        return self.__out_edges

    def in_degree(self, x):
        return len(self.__in_edges[x])

    def out_degree(self, x):
        return len(self.__out_edges[x])

    def number_of_edges(self):
        return len(self.__costs.keys())

    def number_of_vertices(self):
        return len(self.__in_edges)

    def remove_vertex(self, vertex):
        """
        Function that removes a given vertex from the graph
        :param vertex: the vertex to be removed
        :return: -, if the remove operation goes well
        """
        if vertex not in self.__out_edges:
            raise ValueError("Vertex does not exist in the graph")

        # Remove the vertex from out_edges and in_edges if it exists
        del self.__out_edges[vertex]
        if vertex in self.__in_edges:
            del self.__in_edges[vertex]

        # Remove edges containing the vertex from the costs dictionary
        edges_to_remove = []
        for edge in self.__costs:
            if vertex in edge:
                edges_to_remove.append(edge)
        for edge in edges_to_remove:
            del self.__costs[edge]

        # Update the remaining edges in the in_edges and out_edges dictionaries
        for source in self.__in_edges:
            if vertex in self.__in_edges[source]:
                self.__in_edges[source].remove(vertex)

        for source in self.__out_edges:
            if vertex in self.__out_edges[source]:
                self.__out_edges[source].remove(vertex)

    def remove_edge(self, x, y):
        """
        Function that removes the edge from the graph based on the source vertex and destination vertex
        :param x: source vertex
        :param y: destination vertex
        :return: -, if the edge was removed properly
        :raise: ValueError if the edge does not exist
        """
        if not self.is_edge(x, y):
            raise ValueError('Edge does not exist')

        for elem in self.__costs.keys():
            if y == elem[1] and x == elem[0]:
                del self.__costs[elem]
                break
        self.__in_edges[x].remove(x)
        self.__out_edges[x].remove(y)

    def change_cost(self, x, y, val):
        """
        Function that changes the cost of an edge to a new value val
        :param x: the source vertex of an edge
        :param y: the destination vertex of an edge
        :param val: the new coat for the edge
        :return: -, if the change is being done properly
        """
        if not self.is_edge(x, y):
            raise ValueError('Edge does not exist')

        self.__costs[(x, y)] = val

    def get_cost(self, x, y):
        """
        Function that returns the cost of an edge, symbolized by its source and destination vertex
        :param x: the source vertex
        :param y: te destination vertex
        :return: the cost of an edge
        :raise: ValueError if the edge does not exist
        """
        if not self.is_edge(x, y):
            raise ValueError('Edge does not exist')
        return self.__costs[(x, y)]

    def copy_graph(self):
        return deepcopy(self)

    def __repr__(self):
        return str(self)

    def __str__(self):
        r = ''
        for i in self.__costs.keys():
            r += str(i[0]) + ' ' + str(i[1]) + ' ' + str(self.__costs[i]) + '\n'
        for i in self.__in_edges.keys():
            if len(self.__out_edges[i]) == 0 and len(self.__in_edges[i]) == 0:
                r += str(i) + ' -1\n'
        return r
