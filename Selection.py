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
