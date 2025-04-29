class Bubble:
    def __init__(self, toSort):
        self.TOSORT = toSort
        self.used   = self.TOSORT
        self.index  = 0
        self.sorted = self.TOSORT.sort()
    def step():
        if not self.sorted == self.used:
            if self.index + 1 > len(self.used):
                self.index = 0
            if self.used[self.index] > self.used[self.index+1]:
                tmp = self.used[self.index]
                self.used[self.index] = self.used[self.index + 1]
                self.used[self.index + 1] = tmp
            return False
        else:
            return True

class QSort:
    def __init__(self, toSort):
        self.TOSORT = toSort
        self.used   = self.TOSORT

    def step():
        self.used = self.used
