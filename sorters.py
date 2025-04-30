class Bubble:
    def __init__(self, toSort):
        self.TOSORT = toSort[:]
        self.used   = self.TOSORT[:]
        self.index  = 0
        self.sorted = sorted(self.TOSORT)
    def step(self):
        if not self.sorted == self.used:
            if self.index > len(self.used) - 2:
                self.index = 0
            if self.used[self.index] > self.used[self.index+1]:
                tmp = self.used[self.index]
                self.used[self.index] = self.used[self.index + 1]
                self.used[self.index + 1] = tmp
            self.index += 1
            return self.used
        else:
            return self.used

class QSort:
    def __init__(self, toSort):
        self.TOSORT = toSort
        self.used   = self.TOSORT

    def step():
        self.used = self.used
