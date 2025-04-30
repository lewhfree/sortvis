import random

class Bogo:
    def __init__(self, toSort):
        self.solved = sorted(toSort[:])
        self.used   = toSort[:]
        
    def step(self):
        if self.used == self.solved:
            return self.used, -1, True
        else:
            random.shuffle(self.used)
            return self.used, -1, False
