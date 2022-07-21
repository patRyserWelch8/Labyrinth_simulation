import numpy as np
import copy
from labyrinth_solver.agent import Agent
from labyrinth_solver.labyrinth import Labyrinth


class Solver:
    EAST = 0
    WEST = 1
    NORTH = 2
    SOUTH = 3

    def __init__(self, labyrinth) -> None:
        self.labyrinth = labyrinth
        self.labyrinth_copy = labyrinth

        # You may edit the following variables to help you solve the maze.

        # Entry points are values where the labyrinth is 2
        self.entry_points = [(x, y) for y, x in np.array(np.where(labyrinth == 2)).transpose()]

        # Exit points are values where the labyrinth is 3
        self.exit_points = [(x, y) for y, x in np.array(np.where(labyrinth == 3)).transpose()]

        # Walls are values where the labyrinth is 0
        self.walls = [(x, y) for y, x in np.array(np.where(labyrinth == 0)).transpose()]

        # Traversable points are values where the labyrinth is 1
        self.traversable = [(x, y) for y, x in np.array(np.where(labyrinth == 1)).transpose()]

        self.solution = [[], []]

    def parse(self) -> None:
        """
        Parses the labyrinth into data structures which may help in solving the maze.
        """
        print("entry points:", self.entry_points)
        print("exit points:", self.exit_points)
        print("walls:", self.walls)
        print("transversable:", self.traversable)
        print(self.labyrinth)

        pass

    @property
    def solve(self) -> bool:
        """
        Returns True if a solution was found, False otherwise.
        A valid solution is a complete set of paths from each entry point
        to a distinct exit point where no two paths intersect with each other
        and no path intersects with a wall.
        A path is an ordered list of adjacent traversable points.
        """
        self.labyrinth_copy = self._clean()
        for i in range(0, len(self.entry_points)):
            # for i in range(0,1):
            labyrinth = Labyrinth(copy.deepcopy(self.labyrinth_copy), self.entry_points[i], self.exit_points[i])
            labyrinth.set_cell_values(self.entry_points[i][0], self.entry_points[i][1], Agent.STARTING_POINT)
            print(labyrinth.labyrinth)
            self._find_path(labyrinth)

        return False

    def _clean(self):
        labyrinth_copy = copy.deepcopy(self.labyrinth)
        for entry_points in self.entry_points:
            labyrinth_copy[entry_points[1]][entry_points[0]] = -2
        return labyrinth_copy

    def _find_path(self, labyrinth: Labyrinth) -> object:

        agent = Agent(labyrinth.entry_points[0], labyrinth.entry_points[1])
        print("+++++ start +++++++")
        print(labyrinth.labyrinth)

        for i in range(1, 66):
            # Drop stone in current location in the labyrinth
            labyrinth.set_cell_values(agent.x, agent.y, agent.get_stone)
            # use a compass to find information on current location surroundings
            values = labyrinth.get_compass_values(agent.x, agent.y)
            print("+++++ values +++++++")
            print(values)
            # move
            print("+++++ move +++++++")
            print(agent.x)
            print(agent.y)
            agent.move(values[Solver.EAST], values[Solver.WEST], values[Solver.NORTH], values[Solver.SOUTH])
            print(labyrinth.labyrinth)
            print(agent.x)
            print(agent.y)
            print(agent.found_exit_point(labyrinth.labyrinth[agent.y, agent.x]))
