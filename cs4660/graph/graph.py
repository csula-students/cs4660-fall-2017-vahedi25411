"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    if isinstance(graph, AdjacencyList):
        print("AdjacencyList")
    elif isinstance(graph, ObjectOriented):
        mydic = dict()
        f = open(file_path, encoding='utf-8')
        text = f.read()
        lines = text.split('\n')
        number_of_nodes=0

        for line in lines:

            if len(line) > 0:

                items = line.split(':')
                first_node = None
                second_node = None

                if len(items) == 1:
                    number_of_nodes = int(items[0])
                else:
                    if not items[0] in mydic:
                        first_node = Node(items[0])
                        mydic[items[0]] = first_node
                        graph.add_node(first_node)
                    else:
                        first_node = mydic[items[0]]


                    if not items[1] in mydic:
                        second_node = Node(items[1])
                        mydic[items[1]] = second_node
                        graph.add_node(Node(items[1]))
                    else:
                        second_node = mydic[items[1]]

                    graph.add_edge(Edge(first_node, second_node, items[2]))

    
        return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))



class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        pass

    def neighbors(self, node):
        pass

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        pass

    def neighbors(self, node):
        pass

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass

    def __get_node_index(self, node):
        """helper method to find node index"""
        pass

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []


    def adjacent(self, node_1, node_2):

        for edge in self.edges:  

            if int(node_1.data) == int(edge.from_node.data) :
                if int(node_2.data) == int(edge.to_node.data):
                    return True                                    


        return False
        pass

    def neighbors(self, node):
        neighbors = []

        for edge in self.edges:
            if int(edge.from_node.data) == int(node.data):
                neighbors.append(edge.to_node)
        return neighbors
        pass

    def add_node(self, node):
        self.nodes.append(node)
        pass

    def remove_node(self, node):
        self.nodes.remove(node)
        pass

    def add_edge(self, edge):
        self.edges.append(edge)
        pass

    def remove_edge(self, edge):
        for ed in self.edges:
            if ed.hash == edge.hash:
                self.edges.remove(ed)
            return True

        return False
        pass

