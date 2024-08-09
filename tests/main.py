


class IntNumbers:
    def __init__(self, *args):
        self.list = []
        for i in args:
            if isinstance(i, int):
                self.list.append(i)
        
    def sum_el(self):
        return sum(self.list)
    
    def mid(self):
        return sum(self.list) / len(self.list)
    
    def max_el(self):
        return max(self.list)
    
    def min_el(self):
        return min(self.list)
