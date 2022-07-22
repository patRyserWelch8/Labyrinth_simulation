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
            self.lab_theseus = Labyrinth(self._clean(), self.entry_points[0], self.exit_points[0])
            self.lab_theseus.set_cell_values(self.entry_points[0][0], self.entry_points[0][1], Labyrinth.STARTING_POINT)

            self.lab_min = Labyrinth(self._clean(), self.entry_points[1], self.exit_points[1])
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

        # create labyrinth for a entry point

        if not self.lab_theseus == None and not self.lab_min == None:
            solution_exists = self._find_path()
            print(self.lab_min.labyrinth)
            print(self.lab_theseus.labyrinth)


        #for i in range(0, len(self.entry_points)):
            # create labyrinth for a entry point
            #labyrinth = Labyrinth(copy.deepcopy(self.labyrinth_copy), self.entry_points[i], self.exit_points[i])
            # add entry point
            #labyrinth.

           # print(" --- prior: ---")
           # print(labyrinth.labyrinth)
            # solve and retried a solution
           # solution = self._find_path(labyrinth)
           # self.solution[i] = solution[1]
           # solution_exists = solution_exists & solution[0]
           # print("---after ----")
           # self.entry_points[i]
           # print(labyrinth.labyrinth)
           # print("----")

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

        while not both_out:
            if not self.lab_theseus.found_exit_point(theseus.x, theseus.y):
                self.lab_theseus.set_cell_values(theseus.x, theseus.y, Agent.STONE)
                values = self.lab_theseus.get_compass_values(theseus.x, theseus.y)
                theseus.move(values[Solver.EAST],
                             values[Solver.WEST],
                             values[Solver.NORTH],
                             values[Solver.SOUTH])
                #print(self.lab_theseus.labyrinth)

            if not self.lab_min.found_exit_point(minautor.x, minautor.y):
                self.lab_min.set_cell_values(minautor.x, minautor.y, Agent.STONE)
                values = self.lab_min.get_compass_values(minautor.x, minautor.y)
                minautor.move(values[Solver.EAST],
                              values[Solver.WEST],
                              values[Solver.NORTH],
                              values[Solver.SOUTH])
                #print(self.lab_min.labyrinth)

            both_out = self.lab_theseus.found_exit_point(theseus.x, theseus.y) and \
                       self.lab_min.found_exit_point(minautor.x, minautor.y)
            print(both_out)

        self.solution[0] = theseus.path
        self.solution[1] = minautor.path
        return both_out


