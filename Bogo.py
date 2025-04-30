import random

class Bogo:
    def __init__(self, toSort):
        self.solved = sorted(toSort[:])
        self.used   = toSort[:]
        
    def __str__(self):
        return """BogoSort, aka stupid sort, is the random sorting algorithm
It scrambles the list, and checks if it is sorted.
Infinite worst case time complexity, best case of O(n), average of O(n x n!)"""

    def step(self):
        if self.used == self.solved:
            return self.used, -1, True
        else:
            random.shuffle(self.used)
            return self.used, -1, False
