class Bubble:
    def __init__(self, toSort):
        self.used = toSort[:] # makes a copy so its not changing the real toSort
    def __str__(self):
        return """Name, description, how it works, time complexity"""

    def step(self):
        #should run one step of the algo. See bubble.py because that is what it should be like
        
        return 1
        #should return the modified array, the index the pointer is at (-1 to have none), and if it has been solved

        #Not done
        #return self.used, self.index, False

        #Done
        #return self.used, self.index, True
