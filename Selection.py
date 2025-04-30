class Selection:
    def __init__(self, toSort):
        self.solved = sorted(toSort[:])
        self.used   = toSort[:]
        self.index  = 0
        self.scan = 1
        self.mini = 0

    def __str__(self):
        return """Selection sort is a easy algorithm.
It compares each number with all following numbers and swaps if there is a smaller number.
It has a best, worst, and average time complexity of O(n^2)"""
    def step(self):

        if self.index>= len(self.used):
            return self.used, self.index - 1, True
        for i in range(len(self.used)-self.index):
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
