import matplotlib.pyplot as plt
import numpy as np
import random
import time


def flipCoords(rcpos, LIMITS):
    y = rcpos[0]
    x = rcpos[1]
    return (x, y)

# Definition of super class Organism


class Organism:
    def __init__(self, name, pos, colour):
        self.name = name  # Name of an entity
        self.pos = pos  # Position of an entitiy
        self.colour = colour    # Color of an antity

    # Method to return the position of an entity
    def getPos(self):
        return self.pos
    # Method to plot an entity

    def plotMe(self, ax, LIMITS, shape, size):
        XYpos = flipCoords(self.pos, LIMITS)
        if shape == "circle":
            obj = plt.Circle(XYpos, size, color=self.colour)
        elif shape == "rectangle":  # This is specifically to plot trunk part of tree
            obj = plt.Rectangle(
                (XYpos[0] + size * 2, XYpos[1]), size, size * 2, color=self.colour)
        ax.add_patch(obj)

    # Code to detect collision

    def check_collision(self, other_pos):
        if self.pos == other_pos:
            return True
        return False

# Definition of Ant class inheriting the super class Organism


class Ant(Organism):
    size = 0.3

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.colour = "red"
        # self.heading = heading

    # def getPos(self):
    #     return self.pos

    # Modification of stepchange method to check for collisions with rocks before moving
    def stepChange(self, subgrid, rocks):
        validMoves = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
        possible_moves = []
        for move in validMoves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            if new_pos not in rocks:
                # The ant will move in only tunnel
                for a in range(len(subgrid)):
                    for b in range(len(subgrid)):
                        if subgrid[a, b] == 0:
                            possible_moves.append((a-1, b-1))

        if possible_moves and len(possible_moves) > 0:
            move = random.choice(possible_moves)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    # def plotMe(self, ax, LIMITS):
    #     XYpos = flipCoords(self.pos, LIMITS)
    #     circle1 = plt.Circle(XYpos, self.size, color=self.colour)
    #     ax.add_patch(circle1)

# Definition of Butterfly class inheriting the super class Organism


class Butterfly(Organism):
    size = 1

    # def __init__(self, name, pos, colour):
    #     self.name = name
    #     self.pos = pos
    #     self.colour = colour
    #     self.size = 0.7

    # def getPos(self):
    #     return self.pos

    def stepChange(self, subgrid, plants):
        # validMoves = [(1,-1),(1,1)]

        # Check if the butterfly is on a plant
        if self.pos in plants:
            print(f'Butterfly {self.name} is resting on a plant.')
            time.sleep(3)  # Rest for 3 seconds before moving again
        # Valid moves using Moore neighbourhood
        validMoves = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1),
                      (1, 0), (1, -1), (0, -1), (-1, -1)]
        # print(f'Butterflies validmoves: {validMoves}')
        # print(validMoves)
        if len(validMoves) > 0:
            move = random.choice(validMoves)
            self.pos = (self.pos[0] + move[0],  self.pos[1] + move[1])


# Definition of Ladybug class inheriting the super class Organism
class Ladybug(Organism):
    # def __init__(self, name, pos, colour):
    #     self.name = name
    #     self.pos = pos
    #     self.colour = colour
    #     self.size = 0.5

    # def getPos(self):
    #     return self.pos

    def stepChange(self, subgrid, plants):
        # Check if the ladybug is on a plant
        if self.pos in plants:
            print(f'Ladybug {self.name} is resting on a plant.')
            time.sleep(3)  # Rest for 3 seconds before moving again
        validMoves = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]
        move = random.choice(validMoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])


# Definition of Caterpillar class inheriting the super class Organism


class Caterpillar(Organism):
    def __init__(self, name, pos, colour, num_segments):
        super().__init__(name, pos, colour)
        self.segment_radius = 0.2
        self.num_segments = num_segments
        # self.size = 0.4

    # def getPos(self):
    #     return self.pos

    def stepChange(self, subgrid, plants):
        # check if the caterpillar is on a plant
        if self.pos in plants:
            print(f'Caterpillar {self.name} is resting on plant.')
            time.sleep(3)  # Rest for 3 seconds before moving again
        # Caterpillar moves left,right and forward only
        validMoves = [(0, 1), (-1, 0), (1, 0)]
        move = random.choice(validMoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plotMe(self, ax, LIMITS, shape, size):
        for i in range(self.num_segments):
            segment_pos = (self.pos[0], self.pos[1] +
                           i * 2 * self.segment_radius)
            segment_pos = flipCoords(segment_pos, LIMITS)
            if shape == "circle":
                obj = plt.Circle(segment_pos, size, color=self.colour)
            ax.add_patch(obj)


# Defining obstacles class


class Plant():
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.trunk_colour = "brown"  # Color of the tree trunk
        self.foliage_colour = "green"  # Color of the foliage
        self.trunk_width = 1.2  # Width of the tree trunk
        self.trunk_height = 3  # Height of the tree trunk
        self.foliage_radius = 1.5  # Radius of the foliage

    def getPos(self):
        return self.pos

    def plotMe(self, ax, LIMITS):
        trunk_pos = flipCoords(self.pos, LIMITS)
        trunk = plt.Rectangle((trunk_pos[0] + self.trunk_width*2, trunk_pos[1]),
                              self.trunk_width, self.trunk_height, color=self.trunk_colour)
        ax.add_patch(trunk)

        foliage_pos = flipCoords(
            (self.pos[0], self.pos[1] + self.trunk_height), LIMITS)
        foliage = plt.Circle(
            foliage_pos, self.foliage_radius, color=self.foliage_colour)
        ax.add_patch(foliage)


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

# Defining rain for simulation of rain


class Raindrop():
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed
        # size of the rain
        self.size = 0.1

    def getPos(self):
        return self.pos

    def stepChange(self):
        # Simulating the raindrop falling down by updating the position
        if self.pos[0] < 15:
            self.pos = (self.pos[0], self.pos[1] - self.speed)
        else:
            # Remove the raindrop when it hits row 15 (Making visible only above the ground)
            self.pos = None

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle = plt.Circle(XYpos, self.size, color='aqua')
        ax.add_patch(circle)
