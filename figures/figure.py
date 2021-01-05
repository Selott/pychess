class Figure:
    def __init__(self):
        pass
    def moves(self) -> []:
        pass
    def can_beat(self, other) -> bool:
        return [other.locX, other.locY] in self.moves()
