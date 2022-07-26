class Node:
    def __init__(self, name, LUID=""):
        self.name = name
        self.LUID = LUID
        self.mark = "black"

    def __str__(self):
        return f'Node:{self.name}'

    def __repr__(self):
        return f'Node:{self.name}'

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ne__(self, other):
        return self.name != other.name

    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
