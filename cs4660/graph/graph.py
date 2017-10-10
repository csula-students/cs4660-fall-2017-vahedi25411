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

    mydic = dict()
    f = open(file_path, encoding='utf-8')
    text = f.read()
    lines = text.split('\n')
    number_of_nodes=0


    if isinstance(graph, AdjacencyMatrix):
        for line in lines:

            if len(line) > 0:

                items = line.split(':')
                first_node = None
                second_node = None

                if len(items) == 1:
                    number_of_nodes = int(items[0])

                    for i in range(0,number_of_nodes):
                        graph.add_node(Node(int(i)))

                    main_list = []
                    for i in range(0, number_of_nodes):
                        row_list = []
                        for j in range(0, number_of_nodes):
                            row_list.append(0)

                        main_list.append(row_list)

                    graph.adjacency_matrix = main_list
                    
                else:
                    first_node = Node(int(items[0]))
                    second_node = Node(int(items[1]))

                    graph.add_edge(Edge(first_node, second_node, int(items[2])))
                
    
        return graph

    elif isinstance(graph, AdjacencyList):
        for line in lines:

            if len(line) > 0:

                items = line.split(':')
                first_node = None
                second_node = None

                if len(items) == 1:
                    number_of_nodes = int(items[0])

                    for i in range(0,number_of_nodes):
                        graph.add_node(Node(int(i)))
                        mydic[Node(i)] = Node(i)
                else:

                    first_node = Node(int(items[0]))
                    if not first_node in mydic:       
                        mydic[first_node] = []
                        graph.add_node(first_node)

                    second_node = Node(int(items[1]))
                    if not second_node in mydic:                        
                        mydic[second_node] = []
                        graph.add_node(second_node)


                    graph.add_edge(Edge(first_node, second_node, items[2]))

    
        return graph

    elif isinstance(graph, ObjectOriented):

        for line in lines:

            if len(line) > 0:

                items = line.split(':')
                first_node = None
                second_node = None

                if len(items) == 1:
                    number_of_nodes = int(items[0])
                    for i in range(0,number_of_nodes):
                        graph.add_node(Node(int(i)))
                        mydic[i] = Node(i)
                else:
                    if not items[0] in mydic:
                        first_node = Node(int(items[0]))
                        mydic[items[0]] = first_node
                        graph.add_node(first_node)
                    else:
                        first_node = mydic[items[0]]


                    if not items[1] in mydic:
                        second_node = Node(int(items[1]))
                        mydic[items[1]] = second_node
                        graph.add_node(Node(items[1]))
                    else:
                        second_node = mydic[items[1]]

                    graph.add_edge(Edge(first_node, second_node, items[2]))

    
        return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data=0):
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
        return self.from_node.data == other_node.from_node.data and self.to_node.data == other_node.to_node.data and self.weight == other_node.weight
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
        self.nodes=[]

    def adjacent(self, node_1, node_2):
        #print(node_1)
        #print(self.adjacency_list[node_1])

        list = self.adjacency_list[node_1]
        
        for edge in list:
            if node_2 == edge.to_node:
                return True
                
        return False
        pass
        

    def neighbors(self, node):
        neighbors=[]
        list = self.adjacency_list[node]
        for edge in list:
            neighbors.append(edge.to_node)

        return neighbors     
        pass

    def add_node(self, node):
        if not node in self.adjacency_list:
            self.nodes.append(node)
            self.adjacency_list[node] = []
            return True
        else:
            return False
        pass

    def remove_node(self, node):
        if not node in self.adjacency_list:
            return False
        else: 
            for related_node in self.nodes:
                for edge in self.adjacency_list[related_node]:
                    if edge.to_node == node:
                        self.remove_edge(edge)
            
            del self.adjacency_list[node]
            self.nodes.remove(node)
            return True
            
        pass

    def add_edge(self, edge):
        node = edge.from_node
        if not edge in self.adjacency_list.get(node,[]):
            self.adjacency_list.get(node,[]).append(edge)
            return True
        else:
            return False

        pass

    def remove_edge(self, edge):
        if edge in self.adjacency_list.get(edge.from_node,[]):
            self.adjacency_list.get(edge.from_node,[]).remove(edge)
            return True
        else:
            return False
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

        if self.adjacency_matrix[self.__get_node_index(node_1)][self.__get_node_index(node_2)]>0:
            return True
        else:
            return False
        pass

    def neighbors(self, node):
        neighbors =[]
        counter = 0
        node_index = self.__get_node_index(node)
        
        for i in range(0,len(self.nodes)):
            if self.adjacency_matrix[node_index][counter]>0:
                neighbors.append(self.nodes[i])
            counter += 1
        
        return neighbors
        pass

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True            
        pass

    def remove_node(self, node):
        if node in self.nodes:
            row=-1
            for i in range(0,len(self.adjacency_matrix)):
                for j in range(0,len(self.adjacency_matrix[0])):
                    if i==self.__get_node_index(node):
                        row = i
                        #del self.adjacency_matrix[i]
                    if j==self.__get_node_index(node):
                        del self.adjacency_matrix[i][j]

            #self.nodes.remove(node)
            if row > -1:
                del self.adjacency_matrix[row]

            self.nodes.remove(node)     
            return True
        else:
            return False
        pass

    def add_edge(self, edge):
        index1 = self.__get_node_index(edge.from_node)
        index2 = self.__get_node_index(edge.to_node)

        if self.adjacency_matrix[index1][index2] == int(edge.weight):
            return False
        else:
            self.adjacency_matrix[index1][index2] = int(edge.weight)
            return True
        pass

    def remove_edge(self, edge):
        if self.adjacency_matrix[self.__get_node_index(edge.from_node)][self.__get_node_index(edge.to_node)] == 0:
            return False
        else:
            self.adjacency_matrix[self.__get_node_index(edge.from_node)][self.__get_node_index(edge.to_node)] = 0
            return True
        pass
        pass

    def __get_node_index(self, node):
        index=-1

        for i in range(0,len(self.nodes)):
            if self.nodes[i]==node:
                index=i
        return index
    
        #return self.nodes.index(node)
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

            if node_1 == edge.from_node :
                if node_2 == edge.to_node:
                    return True                                    


        return False
        pass

    def neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if edge.from_node == node:
                neighbors.append(edge.to_node)
        return neighbors
        pass

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True
        pass

    def remove_node(self, node):
        if node in self.nodes:
            for edge in self.edges:
                if edge.from_node == node or edge.to_node == node:
                    self.remove_edge(edge)

            self.nodes.remove(node)
            return True
        else:
            return False
        pass

    def add_edge(self, edge):
        if edge in self.edges:
            return False
        else:
            self.edges.append(edge)
            return True
        pass

    def remove_edge(self, edge):
        """
        for ed in self.edges:
            if ed.hash == edge.hash:
                self.edges.remove(ed)
            return True
        """
        if edge in self.edges:  
            self.edges.remove(edge)
            return True      
        else:
            return False

        pass

