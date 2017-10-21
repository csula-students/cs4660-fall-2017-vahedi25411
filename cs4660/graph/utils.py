from graph import graph as GRAPH

"""
utils package is for some quick utility methods
such as parsing
"""

class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)




def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph
    Returns graph object
    """
    # TODO: read the filepaht line by line to construct nodes & edges

    # TODO: for each node/edge above, add it to graph
    
    file = open(file_path, encoding='utf-8')
    text = file.read()
    lines = text.split('\n')
    nodes_list = []
    for line in lines:
        if line:
            nodes_list.append([line[i:i+2] for i in range(1, len(line[1:-1]), 2)])
    nodes_list = nodes_list[1:-1]        
    
    file.close()

    # TODO: for each node/edge above, add it to graph
    tiles = {}

    for y in range(len(nodes_list)):
        for x in range (len(nodes_list[0])):
            tile = Tile(x, y, nodes_list[y][x])
            graph.add_node(GRAPH.Node(tile))
            tiles[(x, y)] = tile

    for y in range(len(nodes_list)):
        for x in range (len(nodes_list[0])):
            current_tile = Tile(x, y, nodes_list[y][x])

            if current_tile.symbol == "##":
                continue 
            
            if (x, y - 1) in tiles:
                upper_tile = tiles[(x, y - 1)]
                if upper_tile.symbol != "##":
                    graph.add_edge(GRAPH.Edge(GRAPH.Node(current_tile), GRAPH.Node(upper_tile), 1))   

            if (x, y + 1) in tiles:
                lower_tile = tiles[(x, y + 1)]
                if lower_tile.symbol != "##":
                    graph.add_edge(GRAPH.Edge(GRAPH.Node(current_tile), GRAPH.Node(lower_tile), 1))

            if (x - 1, y) in tiles:
                left_tile = tiles[(x - 1, y)]
                if left_tile.symbol != "##":
                    graph.add_edge(GRAPH.Edge(GRAPH.Node(current_tile), GRAPH.Node(left_tile), 1))

            if (x + 1, y) in tiles:
                right_tile = tiles[(x + 1, y)]
                if right_tile.symbol != "##":
                    graph.add_edge(GRAPH.Edge(GRAPH.Node(current_tile), GRAPH.Node(right_tile), 1))


    return graph


def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile
    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """
    result = ""
    for edge in edges:  
        tile1 = edge.from_node.data
        tile2 = edge.to_node.data
        if tile2.x == tile1.x + 1 and tile1.y == tile2.y:
            result += "E" 
        elif tile2.x == tile1.x - 1 and tile1.y == tile2.y:
            result += "W"
        elif tile1.x == tile2.x and tile2.y == tile1.y + 1:
            result += "S"
        elif tile1.x == tile2.x and tile2.y == tile1.y - 1:
            result += "N"

    return result


