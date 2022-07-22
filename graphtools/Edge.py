
class Edge:
    def __init__(self, start, end, label:str):
        self.start = start
        self.end = end
        self.label = label

    def __str__(self):
        return f'{self.start}->{self.end}'

    def __repr__(self):
        return f'Edge[{self.start}->{self.end}][{self.label}]'

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __eq__(self, other):
        pass
