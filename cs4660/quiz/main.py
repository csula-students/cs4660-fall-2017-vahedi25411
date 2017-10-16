"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import queue as QUEUE
from quiz import utils
from graph import graph as GRAPH
import json
import codecs
import os

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

    result = {}
    file_name = room_id + ".json"
    if not os.path.isfile(file_name):

        result = __json_request(GET_STATE_URL, body)
        print("*******")
        print(result)

        with open(file_name, 'w') as outfile:
            json.dump(result, outfile)

    else:
        with open(file_name) as data_file:    
            result = json.load(data_file)
        pass
    
    return result

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
        new_room = __get_room_info(item)
        neighbors.append(new_room)
    

    room = utils.Room(body['id'],room_info,body['neighbors'])

    return room

def bfs(initial_node, dest_node):

    #empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    #end_room = get_state('f1f131f647621a4be7c71292e79613f9')
    empty_room = get_state(initial_node)
    end_room = get_state(dest_node)
    
    results = []
    queue = []
    visited = {}
    parents = {}

    queue = QUEUE.Queue()

    empty_room = __get_room_info(empty_room)
    
    end_room = __get_room_info(end_room)

    queue.put(empty_room)
    room_finded = False
    parents[empty_room.id] = None
    while not queue.empty() and not room_finded:
        
        room = queue.get()
        parent = room
        visited[room.id] = True

        for neighbor in room.neighbors:
            if neighbor['id'] not in visited:
                new_room = __get_room_info( get_state( neighbor['id'] ) )
                parents[new_room.id] = parent
                if new_room.id == end_room.id:
                    room_finded = True
                    break
                queue.put(new_room)


    current_room = end_room
    total_hp = 0
    while parents[current_room.id] is not None:
        hp = __get_distance(parents[current_room.id],current_room)
        results.append(parents[current_room.id].room_info.name + "(" + parents[current_room.id].id+ ") : "
            + current_room.room_info.name + "(" + current_room.id + ")" + " : " + str( hp ))
        total_hp += hp
        current_room = parents[current_room.id]

    results.reverse()
    results.append("Total hp : " + str(total_hp))

    for result in results:
        print(result)


def dijkstra_search(initial_node, dest_node):
    results = []
    queue = []
    distance = {}
    visited = {}
    parents = {}

    initial_room = get_state(initial_node)
    dest_room = get_state(dest_node)

    initial_room = __get_room_info(initial_room)
    dest_room = __get_room_info(dest_room)
    
    queue = QUEUE.PriorityQueue()

    distance[initial_room.id] = 0
    parents[initial_room.id] = None

    queue.put(utils.WeightedRoom(distance[initial_room.id],initial_room))

    room_finded = False

    while not queue.empty():
        
        weighted_room = queue.get()
        room = weighted_room.room

        parent = room
        visited[room.id] = True

        for neighbor in room.neighbors:
            neighbor_room = __get_room_info( get_state( neighbor['id'] ) )
            cur_distance = __get_distance( parent, neighbor_room)

            if neighbor_room.id not in visited:

                parents[neighbor_room.id] = parent
                
                distance[neighbor_room.id] = distance[parent.id] + cur_distance
                visited[neighbor_room.id] = True
                queue.put(utils.WeightedRoom(-1*distance[neighbor_room.id],neighbor_room))
 
    
    
    current_room = dest_room
    #results.append(current_room.id)
    total_hp = 0
    while parents[current_room.id] is not None:

        hp = __get_distance(parents[current_room.id],current_room)
        results.append(parents[current_room.id].room_info.name + "(" + parents[current_room.id].id+ ") : "
            + current_room.room_info.name + "(" + current_room.id + ")" + " : " + str( hp ))
        total_hp += hp
        #edges.append(parents[current_room.id].id)
        current_room = parents[current_room.id]
    

    results.reverse()
    results.append("Total hp : " + str(total_hp))

    for result in results:
        print(result)
    



def __get_distance( from_room, to_room):

    distance = transition_state(from_room.id, to_room.id)

    return int(distance['event']['effect'])

if __name__ == "__main__":
    # Your code starts here
    print("BFS Result : ")
    bfs('7f3dc077574c013d98b2de8f735058b4','f1f131f647621a4be7c71292e79613f9')
    print("Dijkstra Result : ")
    dijkstra_search('7f3dc077574c013d98b2de8f735058b4','f1f131f647621a4be7c71292e79613f9')
    #print(get_state('b07dcf1aa04ff9dd480c7b2164b7fafb'))
    #print("start :")
    #print(dijkstra_search('7f3dc077574c013d98b2de8f735058b4','f1f131f647621a4be7c71292e79613f9'))
    #print("end :")
    

