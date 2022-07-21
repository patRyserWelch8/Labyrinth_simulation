import numpy as np
import copy
from labyrinth_solver.agent import Agent
from labyrinth_solver.labyrinth import Labyrinth


class Solver:
    EAST = 0
    WEST = 1
    NORTH = 2
    SOUTH = 3

    def __init__(self, alabyrinth) -> None:
        self.labyrinth = alabyrinth
        self.labyrinth_copy = []
        self.solution = [[], []]


        # You may edit the following variables to help you solve the maze.

        # Entry points are values where the labyrinth is 2
        self.entry_points = [(x, y) for y, x in np.array(np.where(self.labyrinth == 2)).transpose()]

        # Exit points are values where the labyrinth is 3
        self.exit_points = [(x, y) for y, x in np.array(np.where(self.labyrinth == 3)).transpose()]



    def parse(self) -> None:
        """
        Parses the labyrinth into data structures which may help in solving the maze.
        """
        self.labyrinth_copy = self._clean()
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
        solution_exists = True
        # create labyrinth for a entry point
        saved_labyrinth = copy.deepcopy(self.labyrinth_copy)

        for i in range(0, len(self.entry_points)):
            # create labyrinth for a entry point
            labyrinth = Labyrinth(saved_labyrinth, self.entry_points[i], self.exit_points[i])
            # add entry point
            labyrinth.set_cell_values(self.entry_points[i][0], self.entry_points[i][1], Labyrinth.STARTING_POINT)
            print(" --- prior: ---")
            print(labyrinth.labyrinth)
            # solve and retried a solution
            solution = self._find_path(labyrinth)
            self.solution[i] = solution[1]
            solution_exists = solution_exists & solution[0]
            saved_labyrinth = copy.deepcopy(labyrinth.labyrinth)
            #
            print("---after ----")
            self.entry_points[i]
            print(labyrinth.labyrinth)
            print("----")

        return solution_exists

    def _clean(self):
        labyrinth_copy = copy.deepcopy(self.labyrinth)
        for entry_points in self.entry_points:
            labyrinth_copy[entry_points[1]][entry_points[0]] = -2
        return labyrinth_copy

    def _find_path(self, labyrinth: Labyrinth) -> [bool,[]]:
        agent = Agent(labyrinth.entry_points[0], labyrinth.entry_points[1], labyrinth.get_boundaries)

        while not labyrinth.found_exit_point(agent.x, agent.y):
            # Drop stone in current location in the labyrinth
            labyrinth.set_cell_values(agent.x, agent.y, Agent.STONE)
            # use a compass to find information on current location surroundings
            values = labyrinth.get_compass_values(agent.x, agent.y)
            # move
            agent.move(values[Solver.EAST], values[Solver.WEST], values[Solver.NORTH], values[Solver.SOUTH])

        return [labyrinth.found_exit_point(agent.x, agent.y), agent.path]

