class Bubble:
    def __init__(self, toSort):
        self.TOSORT = toSort[:]
        self.used   = self.TOSORT[:]
        self.index  = 0
        self.sorted = sorted(self.TOSORT)
        self.done   = False

    def __str__(self):
        return """Bubble sort is a very simple sorting algorithm.
It checks if two numbers next to each other are in the right order, and swaps them if not. It repeats this until the list is sorted.
It has a worst and average time complexity of O(n^2), and a best case performace of O(n)"""

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
