from labyrinth_solver.agent import Agent


class Labyrinth:
    labyrinth: object

    def __init__(self, aLabyrinth: object, someEntryPoints: object, someExitPoints: object) -> None:
        self.labyrinth = aLabyrinth
        self.entry_points = someEntryPoints
        self.exit_points = someExitPoints
        self._boundaries = [0, len(self.labyrinth[0]), 0, len(self.labyrinth)]
        self.set_cell_values(self.entry_points[1], self.exit_points[0], 2)

    @property
    def get_boundaries(self):
        return self._boundaries


    def get_compass_values(self, x: int, y: int) -> [int, int, int, int]:
        """
        :param x:
        :param y:
        :return: [east, west, north, south]
        """
        east: int = Agent.WALL
        west: int = Agent.WALL
        north : int = Agent.WALL
        south : int = Agent.WALL

        if x <= self._boundaries[0]:  # out of scope on the left <= 0 - unlikely negative
            west = -1
            east = self.labyrinth[y][x + 1]
        elif x >= self._boundaries[1]-1:  # out of scope on the right <= 0 - > than width of labyrinth
            east = -1
            west = self.labyrinth[y][x - 1]
        else:
            east = self.labyrinth[y][x+1]
            west = self.labyrinth[y][x-1]

        if y < self._boundaries[2]: # out of scope on first row <= 0 - unlikely negative
            north = Agent.STONE
            south = self.labyrinth[y + 1][x]
        elif y >= self._boundaries[3]-1: # out of scope on last row >= no of rows.
            south = Agent.STONE
            north = self.labyrinth[y - 1][x]
        else:
            north = self.labyrinth[y-1][x]
            south = self.labyrinth[y+1][x]

        return [east, west, north, south]


            #== y < self._boundaries[3]:

    def set_cell_values(self, x: int, y: int, value: int) -> None:
        if self._boundaries[0] <= x < self._boundaries[1]:
            if self._boundaries[2] <= y < self._boundaries[3]:
                self.labyrinth[y][x] = value
