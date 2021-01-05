from figures.figure import Figure
class Pawn(Figure):
    def __init__(self):
        self.name = "Pawn"
        self.color = "?"
        self.locX = 0
        self.locY = 0
        self.char = "?"
        self.moved = False

    def moves(self) -> []: #Need to include beat-move (one forward, one to either left or right) in board
        locX = self.locX
        locY = self.locY
        if self.moved:
            if self.color == "white":
                return [[locX, locY + 1]]
            else:
                return [[locX, locY - 1]]
        else:
            if self.color == "white":
                return [[locX, locY+1], [locX, locX+2]]
            else:
                return [[locX, locY-1], [locX, locY-2]]


