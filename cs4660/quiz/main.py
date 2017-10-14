"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

from quiz import utils
import json
import codecs

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.
    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response

def __get_room_info(body):
    
    room_info = utils.RoomInfo(body['location']['x'],body['location']['y'],body['location']['name'])
    
    neighbors = []
    for item in body['neighbors']:
        neighbors.append(__get_room_info(item))

    room = utils.Room(body['id'],room_info,body['neighbors'])

    return room

if __name__ == "__main__":
    # Your code starts here
    
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    end_room = get_state('f1f131f647621a4be7c71292e79613f9')
    #print(empty_room)
    

    empty_room = __get_room_info(empty_room)
    end_room = __get_room_info(end_room)


    node_info = {}
    visited = []
    edges = []
    queue = []
    parents = {}
    parent = None
    find = False

    queue.append(empty_room)

    print(empty_room.id)
    
    parents[empty_room.id]=None
    
    while len(queue) > 0 and not find:
        
        room = queue.pop(0)

        parent = room

        if room not in visited:

            visited.append(room)

            neighbors = room.neighbors
            
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in queue:

                    parents[neighbor.id] = parent


                    if neighbor==end_room:
                        find = True
                        break 
                    else:
                        queue.append(neighbor)
                


    
    current_node = end_room

    if find:        
        while parents[current_node.id] is not None:
            edges.append(parents[current_node.id]+" : "+current_node)
            current_node = parents[current_node.id]

    edges.reverse()








