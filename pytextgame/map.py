class Map:
    def __init__(self, name):
        self.name = self.name
        self.elements = []

class Region(Map):
    def __init__(self, name):
        super(name)
        self.map = {
            "n": None,
            "ne": None,
            "e": None,
            "se": None,
            "s": None,
            "sw": None,
            "w": None,
            "nw": None,
        }
    
    def goDirection(self, dir):
        pass

class Room(Map):
    def __init__(self, name):
        super(name)

    def enter(self):
        pass
    
    def leave(self):
        pass