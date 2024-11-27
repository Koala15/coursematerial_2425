class Interval :
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def is_empty(self):
        """if self.lower > self.upper:
            return True
        return False"""
        return (self.lower > self.upper)
    
    def contains(self, x):
        return (x >= self.lower) and (x <= self.upper)
    
    def overlaps_with(self, x):
        """if self.is_empty() or x.is_empty():
            return False"""

        low = max(self.lower,x.lower)
        up = min(self.upper, x.upper)

        return up >= low