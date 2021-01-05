from figures.figure import Figure
class King(Figure):
    def __init__(self):
        self.name = "King"
        self.color = "?"
        self.locX = 0
        self.locY = 0
        self.char = "?"

    def moves(self) -> []:
        res = []
        locX = self.locX - 1
        locY = self.locY + 1
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                res.append([locX + i, locY+j])
        return res



