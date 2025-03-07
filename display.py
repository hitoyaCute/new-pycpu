import threading



default_map = {
        "x":256,
        "y":255,
        "mode":254
        }

class Display:
    def __init__(self, size:tuple[int,int] = (8,8), map = default_map, ramPath = "./ram"):
        self.size = size
        self.ram = open(ramPath, "r")
        self.map = map
    
    def start(self):
        pass

    def worker_(self):
        pass



