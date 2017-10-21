
from graph import graph as GRAPH
import sys
import queue as QUEUE
import math
from graph import utils
"""
Searches module defines all different search algorithms
"""



def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    
    node_info = {}
    visited = []
    edges = []
    queue = []
    parent = None
    find = False

    queue.append(initial_node)

    
    node_info[initial_node]=NodeInfo(initial_node,None , None)

    while len(queue) > 0 and not find:
        
        node = queue.pop(0)

        parent = node

        if node not in visited:

            visited.append(node)

            neighbors = graph.neighbors(node)
            
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in queue:

                    if isinstance(graph, GRAPH.AdjacencyMatrix):
                        parent_index=-1
                        node_index=-1
                        for i in range(0,len(graph.nodes)):
                            if graph.nodes[i] == neighbor:
                                node_index=i
                            if parent is not None and graph.nodes[i] == parent:
                                parent_index=i

                        edge_value = graph.adjacency_matrix[parent_index][node_index]
                        node_info[neighbor] = NodeInfo(neighbor,node, GRAPH.Edge(node,neighbor,int(edge_value)))

                    elif isinstance(graph, GRAPH.AdjacencyList):

                        for edge in graph.adjacency_list[node]:
                            if edge.to_node == neighbor:
                                node_info[neighbor] = NodeInfo(neighbor,node, edge)

                    elif isinstance(graph, GRAPH.ObjectOriented):
                        
                        for edge in graph.edges:
                            if edge.from_node == node and edge.to_node == neighbor:
                                node_info[neighbor] = NodeInfo(neighbor,node, edge)

                    if neighbor==dest_node:
                        find = True
                        break 
                    else:
                        queue.append(neighbor)
                


    
    current_node = dest_node

    if find:        
        while node_info[current_node].parent is not None:
            edges.append(node_info[current_node].edge)
            current_node = node_info[current_node].parent

    edges.reverse()
    return edges

    pass

def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    edges = []
    parents={}
    parents[initial_node] = None
    parents = DFS(graph, initial_node, dest_node, parents)
    
    cur_node = dest_node
    while parents[cur_node] is not None:
        node_info = parents[cur_node]
        edges.append(node_info.edge)
        cur_node = node_info.parent
        
    edges.reverse()
    return edges
    
    pass

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    edges=[]
    distance = {}
    parent = {}
    visited = {}
    distance[initial_node] = 0
    parent[initial_node] = None
    queue = QUEUE.PriorityQueue()

    for node in graph.nodes:
        if node != initial_node:
            distance[node] = sys.maxsize
            parent[node] = None   
        
        queue.put(PrioritizedNode(int(distance[node]),node))

    while not queue.empty():
        prioritized_node = queue.get()
        node = prioritized_node.node
        visited[node] = True
        edge_value = 0
        node_info = None
        
        neighbors = graph.neighbors(node)
        
        for neighbor in neighbors:

            if isinstance(graph, GRAPH.AdjacencyMatrix):
                parent_index=-1
                node_index=-1
                for i in range(0,len(graph.nodes)):
                    if graph.nodes[i] == neighbor:
                        node_index=i
                    if parent is not None and graph.nodes[i] == node:
                        parent_index=i

                edge_value = graph.adjacency_matrix[parent_index][node_index]
                node_info = NodeInfo(neighbor,node, GRAPH.Edge(node,neighbor,int(edge_value)))

            elif isinstance(graph, GRAPH.AdjacencyList):

                for edge in graph.adjacency_list[node]:
                    if edge.to_node == neighbor:
                        edge_value = edge.weight
                        node_info = NodeInfo(neighbor,node, edge)

            elif isinstance(graph, GRAPH.ObjectOriented):
                
                for edge in graph.edges:
                    if edge.from_node == node and edge.to_node == neighbor:
                        edge_value = edge.weight
                        node_info = NodeInfo(neighbor,node, edge)
                        

            neighbor_distance = distance[node] + int(edge_value)
            if neighbor_distance < distance[neighbor]:
                distance[neighbor] = neighbor_distance
                parent[neighbor] = node_info

            if neighbor not in visited:
                queue.put(PrioritizedNode(int(distance[neighbor]),neighbor))

    cur_node = dest_node
    while parent[cur_node] is not None:
        node_info = parent[cur_node]
        edges.append(node_info.edge)
        cur_node = node_info.parent
            
    edges.reverse()
    return edges

    pass

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    queue = QUEUE.PriorityQueue()
    
    parent = {}
    distance = {}
    parent[initial_node] = None
    distance[initial_node] = 0

    queue.put(PrioritizedNode(int(distance[initial_node]),initial_node))

    while not queue.empty():
        prioritized_node = queue.get()
        current = prioritized_node.node

        if current == dest_node:
            break

        for neighbor in graph.neighbors(current):
            new_dist = distance[current] + graph.distance(current, neighbor)


            if neighbor not in distance or new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                priority = new_dist + heuristic(dest_node, neighbor)
                queue.put(PrioritizedNode(int(distance[neighbor]),neighbor))
                parent[neighbor] = current
                
        

    cur_node = dest_node
    edges = []
    while cur_node!=initial_node:
        parent_node = parent[cur_node]
        edges.append(GRAPH.Edge(parent[cur_node],cur_node,int(distance[cur_node])))
        cur_node = parent_node
            
    edges.reverse()

    return edges

    pass


def DFS(graph,current_node, dest_node, parents):

    neighbors = graph.neighbors(current_node)
    parent = current_node

    for neighbor in neighbors:
        if neighbor not in parents and dest_node not in parents:

            if isinstance(graph, GRAPH.AdjacencyMatrix):
                parent_index=-1
                node_index=-1
                for i in range(0,len(graph.nodes)):
                    if graph.nodes[i] == neighbor:
                        node_index=i
                    if parent is not None and graph.nodes[i] == parent:
                        parent_index=i

                edge_value = graph.adjacency_matrix[parent_index][node_index]
                parents[neighbor] = NodeInfo(neighbor,current_node, GRAPH.Edge(current_node,neighbor,int(edge_value)))

            elif isinstance(graph, GRAPH.AdjacencyList):

                #for edge in graph.adjacency_list[node]:
                for edge in graph.adjacency_list[current_node]:
                    if edge.to_node == neighbor:
                        parents[neighbor] = NodeInfo(neighbor,current_node, edge)

            elif isinstance(graph, GRAPH.ObjectOriented):
                
                for edge in graph.edges:
                    if edge.from_node == current_node and edge.to_node == neighbor:
                        parents[neighbor] = NodeInfo(neighbor,current_node, edge)

            if neighbor == dest_node:
                return parents
        
            DFS(graph,neighbor,dest_node,parents)
    
    if dest_node in parents:
        return parents    
    else:
        return
    
    pass

class NodeInfo(object):
    def __init__(self, node, parent, edge):
        self.node = node
        self.parent = parent
        self.edge = edge

class PrioritizedNode(object):
    def __init__(self, priority, node):
        self.priority = priority
        self.node = node

    def __lt__(self, other):
        return self.priority < other.priority

def heuristic(initial_node, dest_node):
   initial_tile = initial_node.data
   dest_tile = dest_node.data
   
   return abs(dest_tile.x - initial_tile.x) + abs(dest_tile.y - initial_tile.y)






