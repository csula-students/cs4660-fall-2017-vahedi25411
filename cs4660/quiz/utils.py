

"""
utils package is for some quick utility methods
such as parsing
"""

class RoomInfo(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return 'x: {}, y: {}, name: {}'.format(self.x, self.y, self.name)
    def __repr__(self):
        return 'x: {}, y: {}, name: {}'.format(self.x, self.y, self.name)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.name == other.name
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.name)

class Room(object):
    def __init__(self, rid, room_info, neighbors):
        self.id = rid
        self.room_info = room_info
        self.neighbors = neighbors

    def __str__(self):
        return 'Room(id: {}, location: {}, neighbors:{})'.format(self.id, self.room_info,self.neighbors)
    def __repr__(self):
        return 'Room(id: {}, location: {}, neighbors:{})'.format(self.id, self.room_info,self.neighbors)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id and self.room_info == other.room_info 
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)