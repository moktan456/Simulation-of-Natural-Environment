import matplotlib.pyplot as plt
import numpy as np
import random


def flipCoords(rcpos, LIMITS):
    y = rcpos[0]
    x = rcpos[1]
    return (x, y)


class Ant():
    size = 0.5

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.colour = "red"
        # self.heading = heading

    def getPos(self):
        return self.pos

    # def stepChange(self, subgrid):
    #     validMoves = []
    #     # Valid moves using Von Neuman Neighbourhood
    #     # validMoves = [(0,0),(1,0),(0,1),(-1,0),(0,-1)]
    #     print(f'Ants valid moves: {validMoves}')
    #     for a in range(len(subgrid)):
    #         for b in range(len(subgrid)):
    #             if subgrid[a, b] == 0:
    #                 validMoves.append((a-1, b-1))
    #     if len(validMoves) > 0:
    #         move = random.choice(validMoves)
    #         self.pos = (self.pos[0] + move[0],  self.pos[1] + move[1])
    # Modification of stepchange method to check for collisions with rocks before moving
    def stepChange(self, subgrid, rocks):
        validMoves = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
        possible_moves = []
        for move in validMoves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            if new_pos not in rocks:
                # Added from here
                for a in range(len(subgrid)):
                    for b in range(len(subgrid)):
                        if subgrid[a, b] == 0:
                            possible_moves.append((a-1, b-1))

        if possible_moves and len(possible_moves) > 0:
            move = random.choice(possible_moves)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)


class Butterfly():

    def __init__(self, name, pos, colour):
        self.name = name
        self.pos = pos
        self.colour = colour
        self.size = 1

    def getPos(self):
        return self.pos

    def stepChange(self, subgrid):
        # validMoves = [(1,-1),(1,1)]
        # Valid moves using Moore neighbourhood
        validMoves = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1),
                      (1, 0), (1, -1), (0, -1), (-1, -1)]
        print(f'Butterflies validmoves: {validMoves}')
        # print(validMoves)
        if len(validMoves) > 0:
            move = random.choice(validMoves)
            self.pos = (self.pos[0] + move[0],  self.pos[1] + move[1])

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)

# Class for ladybug


class Ladybug():
    def __init__(self, name, pos, colour):
        self.name = name
        self.pos = pos
        self.colour = colour
        self.size = 0.8

    def getPos(self):
        return self.pos

    def stepChange(self, subgrid):
        validMoves = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]
        move = random.choice(validMoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)


class Caterpillar():
    def __init__(self, name, pos, colour):
        self.name = name
        self.pos = pos
        self.colour = colour
        self.size = 0.4

    def getPos(self):
        return self.pos

    def stepChange(self, subgrid):
        # Caterpillar moves left,right and forward only
        validMoves = [(0, 1), (-1, 0), (1, 0)]
        move = random.choice(validMoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)

# Creating obstacles


class Plant():
    def __init__(self, name, pos, colour):
        self.name = name
        self.pos = pos
        self.colour = colour
        self.size = 1.3

    def getPos(self):
        return self.pos

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)


class Rock():
    def __init__(self, name, pos, colour):
        self.name = name
        self.pos = pos
        self.colour = colour
        self.size = 2

    def getPos(self):
        return self.pos

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)
