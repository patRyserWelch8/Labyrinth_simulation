

class Labyrinth:
    def __init__(self, aLabyrinth):
        self.labyrinth  = aLabyrinth

    @property
    def get_boundaries(self):
        return [0, len(self.labyrinth[0]), 0, len(self.labyrinth)]

