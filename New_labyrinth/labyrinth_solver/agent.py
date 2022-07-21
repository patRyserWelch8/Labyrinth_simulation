import copy

import numpy as np


class Agent:
    WALL : int = 0
    TRANSVERSALE : int = 1
    STONE: int = -1

    def __init__(self, x: int, y: int, boundaries: [int, int, int, int]) -> None:
        self.x : int = x
        self.y : int = y
        self.path : int = [(self.x,self.y)]
        self.entry : int = [(self.x,self.y)]
        self.boundaries : [int, int, int, int] = boundaries

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

        # decide and move
        if total >= 0: # can move on a transversal and increment path
            self._move_forward(east, west, north, south)
            self._add_to_path()
        elif total < 0 : # has reached a dead-end and need correcting path
            self._correct_path(east, west, north, south)

    @property
    def get_stone(self) -> int:
        return Agent.STONE

    def _adjust(self) -> None:
        if self.x < self.boundaries[0]: # x has left boundaries on the left
            self.x = self.boundaries[0]
        elif self.x >= self.boundaries[1]: # x has left boundaries on the right
            self.x = self.boundaries[1]-1
        if self.y < self.boundaries[2]:  # y has left boundaries on the north
            self.y = self.boundaries[2]
        elif self.y >= self.boundaries[3]:  # x has left boundaries on the right
            self.y = self.boundaries[3]-1
        if len(self.path) >= 1:
            self.path[len(self.path)-1] = (self.x, self.y)
        else:
            self.path = [(self.x, self.y)]

    def _pop_from_path(self):
        self.path = self.path[:-1]

    def _add_to_path(self) -> None:
        self.path.append((self.x, self.y))

    def _correct_path(self, east: int, west: int, north: int, south: int) -> None:
        environment =  [east, west, north, south]
        if Agent.TRANSVERSALE in environment: # can move forward to a possible unvisited transversal
            self._move_forward(east, west, north, south)
            self._add_to_path()
        else :
            if len(self.path) < 1:
               self.path = copy.deepcopy(self.entry)
            # retrace and correct path
            self.x = self.path[len(self.path)-1][0]
            self.y = self.path[len(self.path)-1][1]
            # remove coordinates from path
            self._pop_from_path()


    def _move_forward(self, east: int, west : int, north:int , south : int) -> None:
        if east >= Agent.TRANSVERSALE: # move east
            self.x += 1
        elif south >= Agent.TRANSVERSALE:
            self.y += 1
        elif west >= Agent.TRANSVERSALE: # move west
            self.x -= 1
        elif north >= Agent.TRANSVERSALE:
            self.y -= 1
        self._adjust()


