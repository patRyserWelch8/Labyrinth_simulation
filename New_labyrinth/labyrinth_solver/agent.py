import numpy as np


class Agent:
    STARTING_POINT: int = 2
    EXIT_POINT: int = 3
    WALL : int = 0
    TRANSVERSALE : int = 1
    STONE: int = -1
    STRAIGTH_TUNNEL : int = 0
    JUNCTION: int = 1

    def __init__(self, x: int, y: int, left: int, top: int, right: int, bottom: int) -> None:
        self.x : int = x
        self.y : int = y
        self.min_x : int = left
        self.mix_y : int  = top
        self.max_x : int  = right
        self.max_y : int = bottom
        self.path : int = [(x,y)]

    def found_exit_point(self, current_value: int) -> bool:
        return current_value == Agent.EXIT_POINT

    def move(self, east: int, west: int, north: int, south: int) -> None:
        """
        Decide on the move based on surrounding values.
        :param east: value of the cell on the right [x+1]
        :param west: value of the cell on the left [x-1]
        :param north: value of up cell [y+1]
        :param south: value of down cell [y-1]
        """

        # calculate the metric summarising surrounding
        total = east + west + north + south
        print("total : " , total)
        if total >= 0: # can move on a transversal and increment path
            if total > (Agent.EXIT_POINT + 1): # priority for exit point
                self._move_to_exit_point(east, west, north, south)
            elif total ==  Agent.STRAIGTH_TUNNEL : # move forward horizontally or vertically
                self._move_forward(east, west, north, south)
            elif total == Agent.JUNCTION: # move in junction turn right
                self._move_right(east, west, north, south)
            # add cell to path
            self._add_to_path()
        elif total < 0 : # has reached a dead-end and need correcting path
            self._correct_path(east, west, north, south)

    @property
    def drop_stone(self) -> int:
        return Agent.STONE

    def _pop_from_path(self):
        self.path = self.path[:-1]

    def _add_to_path(self) -> None:
        self.path.append((self.x, self.y))

    def _correct_path(self, east: int, west: int, north: int, south: int) -> None:
        environment =  [east, west, north, south]
        if Agent.TRANSVERSALE in environment: # can move forward to a possible unvisited transversal
            self._move_forward(east, west, north, south)
            self._add_to_path()
        else : # retrace and correct path
            self.x = self.path[len(self.path)-1][0]
            self.y = self.path[len(self.path)-1][1]

            # remove coordinates from path
            self._pop_from_path()



    def _move_forward(self, east: int, west : int, north:int , south : int) -> None:
        if east == Agent.TRANSVERSALE: # move east
            self.x += 1
        elif west == Agent.TRANSVERSALE: # move west
            self.x -= 1
        elif north == Agent.TRANSVERSALE:
            self.x -= 1
        elif south == Agent.TRANSVERSALE:
            self.y += 1

    def _move_right(self, east: int, west : int, north:int , south : int) -> None:
        if east == Agent.WALL: # move west
            self.x -= 1
        elif west == Agent.WALL: # move east
            self.x += 1
        elif north == Agent.WALL: # move south
            self.y -= 1
        elif south == Agent.WALL: # move north
            self.y += 1

    def _move_to_exit_point(self, east: int, west: int, north: int, south: int) -> None:
        if east == Agent.EXIT_POINT:
            self.x += 1
        elif west == Agent.EXIT_POINT:
            self.x -= 1
        elif north == Agent.EXIT_POINT:
            self.y -= 1
        elif south == Agent.EXIT_POINT:
            self.y += 1
