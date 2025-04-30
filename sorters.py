import random

class Bubble:
    def __init__(self, toSort):
        self.TOSORT = toSort[:]
        self.used   = self.TOSORT[:]
        self.index  = 0
        self.sorted = sorted(self.TOSORT)
        self.done   = False
    def step(self):
        if not self.sorted == self.used:
            if self.index > len(self.used) - 2:
                self.index = 0
            if self.used[self.index] > self.used[self.index+1]:
                tmp = self.used[self.index]
                self.used[self.index] = self.used[self.index + 1]
                self.used[self.index + 1] = tmp
            self.index += 1
            return self.used, self.index, False
        else:
            return self.used, self.index, True

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

class Selection:
    def __init__(self, toSort):
        self.solved = sorted(toSort[:])
        self.used   = toSort[:]
        self.index  = 0
        self.scan = 1
        self.mini = 0

    def step(self):

        if self.index>= len(self.used):
            return self.used, self.index - 1, True
        for i in range(1):
            if self.index >= len(self.used):
                break

            if self.scan < len(self.used):
                if self.used[self.scan] < self.used[self.mini]:
                    self.mini = self.scan
                self.scan += 1

            else:
                self.used[self.index], self.used[self.mini] = self.used[self.mini], self.used[self.index]
                self.index += 1
                self.scan = self.index + 1
                self.mini = self.index

        done = bool(self.index >= len(self.used))
        return self.used, self.index - 1, done
