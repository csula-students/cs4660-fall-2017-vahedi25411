
from graph import graph as GRAPH
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

    while not find:
        if len(queue) > 0:
            node = queue.pop(0)
        else:
            break

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
    print(initial_node)
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
    pass

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass


def DFS(graph,current_node, dest_node, parents):

    neighbors = graph.neighbors(current_node)

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
                print(GRAPH.Edge(current_node,neighbor,int(edge_value)))

            elif isinstance(graph, GRAPH.AdjacencyList):

                for edge in graph.adjacency_list[node]:
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





