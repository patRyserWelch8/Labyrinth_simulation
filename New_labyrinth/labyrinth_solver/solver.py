import numpy as np
from labyrinth_solver.agent import  Agent


class Solver:
    def __init__(self, labyrinth) -> None:
        self.labyrinth = labyrinth

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

        # set the agent traversing the labyringth
        #self.agent = Agent(0, 0, 0, 0,  len(self.labyrinth[0])-1, len(self.labyrinth)-1)
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

        #for entry_point in self.entry_points:
        #    agent = Agent(entry_point[0], entry_point[1], 0, 0, len(self.labyrinth[0]) - 1, len(self.labyrinth) - 1)

            #agent = Agent(4, 13, 0, 0, len(self.labyrinth[0]) - 1, len(self.labyrinth) - 1)
            #print(agent.y)
            #print(agent.path)
            #agent.move(1, 1, 1, 3)
            #print(agent.y)
            #print(agent.found_exit_point(3))
            #print(agent.path)


        agent = Agent(5, 5, 0, 0, len(self.labyrinth[0]) - 1, len(self.labyrinth) - 1)
        print(agent.path)
        agent.move(1, -1, 0, 0) # move east
        print(agent.path)
        agent.move(0,1,-1, 0) # move west
        print(agent.path)
        agent.move(0, 0, -1, 1) # move south
        print(agent.path)
        agent.move(1, 0, 0, -1) # move east
        print(agent.path)
        agent.move(-1, 1, 0, 0) # move west
        print(agent.path)
        agent.move(0, -1, 0, 1) # move south
        print(agent.path)
        agent.move(0, 0, 1, -1)  # move north
        print(agent.path)
        agent.move(-1, 0, 1, 0) #  move north
        print(agent.path)
        agent.move(1, -1, 0, 1)  # south
        print(agent.path)
        agent.move(-1, 1, 1, 0)  # north
        print(agent.path)
        agent.move(1, 0, -1, 1)  # east
        print(agent.path)
        agent.move(0, 1, 1, -1)  # west
        print(agent.path)

        return False

