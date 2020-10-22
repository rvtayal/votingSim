class Set:
    def __init__(self):
        self.items = []
    
    def __repr__(self):
        return str(self.items)
    
    def add(item):
        if item in self.items:
            return
        self.items.append(item)

    def remove(item):
        if item in self.items:
            self.items.remove(item)