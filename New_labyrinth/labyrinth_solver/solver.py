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
        self.solution = [[], []]
        self.lab_min: Labyrinth = None
        self.lab_theseus: Labyrinth = None


        # You may edit the following variables to help you solve the maze.

        # Entry points are values where the labyrinth is 2
        self.entry_points = [(x, y) for y, x in np.array(np.where(self.labyrinth == 2)).transpose()]

        # Exit points are values where the labyrinth is 3
        self.exit_points = [(x, y) for y, x in np.array(np.where(self.labyrinth == 3)).transpose()]



    def parse(self) -> None:
        """
        Parses the labyrinth into data structures which may help in solving the maze.
        """

        if len(self.entry_points) >= 2:
            self.lab_theseus = Labyrinth(copy.deepcopy(self._clean()), self.entry_points[0], self.exit_points[0])
            self.lab_theseus.set_cell_values(self.entry_points[0][0], self.entry_points[0][1], Labyrinth.STARTING_POINT)

            self.lab_min = Labyrinth(copy.deepcopy(self._clean()), self.entry_points[1], self.exit_points[1])
            self.lab_min.set_cell_values(self.entry_points[1][0], self.entry_points[1][1], Labyrinth.STARTING_POINT)

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
        print(self.labyrinth)
        # create labyrinth for a entry point
        print(self.exit_points)
        if not self.lab_theseus == None and not self.lab_min == None:
            solution_exists = self._find_path()
            print("minautor:")
            print(self.lab_min.labyrinth)
            print("theseus:")
            print(self.lab_theseus.labyrinth)
        return solution_exists

    def _clean(self):
        labyrinth_copy = copy.deepcopy(self.labyrinth)
        for entry_points in self.entry_points:
            labyrinth_copy[entry_points[1]][entry_points[0]] = -2
        return labyrinth_copy

    def _find_path(self) -> bool:
        theseus = Agent(self.lab_theseus.entry_points[0],
                        self.lab_theseus.entry_points[1],
                        self.lab_theseus.get_boundaries)
        minautor = Agent(self.lab_min.entry_points[0],
                         self.lab_min.entry_points[1],
                         self.lab_min.get_boundaries)
        both_out = self.lab_theseus.found_exit_point(theseus.x, theseus.y) and \
                   self.lab_min.found_exit_point(minautor.x, minautor.y)
        fighting = False
        while not both_out:
            self._move_individual(self.lab_theseus,theseus)
            self._move_individual(self.lab_min,minautor)
            both_out = self.lab_theseus.found_exit_point(theseus.x, theseus.y) and \
                       self.lab_min.found_exit_point(minautor.x, minautor.y)

            if minautor.x == theseus.x and  minautor.y == theseus.y and not both_out:
                fighting = True
                print(fighting)

        self.solution[0] = theseus.path
        self.solution[1] = minautor.path
        return both_out and not fighting

    def _move_individual(self, labyrinth: Labyrinth, agent: Agent):
        if not labyrinth.found_exit_point(agent.x, agent.y):
            labyrinth.set_cell_values(agent.x, agent.y, Agent.STONE)
            values = labyrinth.get_compass_values(agent.x, agent.y)
            agent.move(values[Solver.EAST],
                       values[Solver.WEST],
                       values[Solver.NORTH],
                       values[Solver.SOUTH])