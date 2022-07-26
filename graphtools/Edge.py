
class Edge:
    def __init__(self, start, end, label:str):
        self.start = start
        self.end = end
        self.label = label
        self.mark = "black"

    def __str__(self):
        return f'{self.start}->{self.end}'

    def __repr__(self):
        return f'Edge[({self.start}->{self.end})({self.label})]'

    def __ge__(self, other):
        if self.start >= other.start:
            return True
        else:
            if self.end >= other.end:
                return True

        return False

    def __le__(self, other):
        if self.start <= other.start:
            return True
        else:
            if self.end <= other.end:
                return True

        return False

    def __gt__(self, other):
        if self.start > other.start:
            return True
        else:
            if self.end > other.end:
                return True

        return False

    def __lt__(self, other):
        if self.start < other.start:
            return True
        else:
            if self.end < other.end:
                return True

        return False

    def __ne__(self, other):
        tof = self.start == other.start and self.end == other.end
        return False if tof else True

    def __eq__(self, other):
        tof = self.start == other.start and self.end == other.end
        return True if tof else False

    def __hash__(self):
        return hash((self.start, self.end))



