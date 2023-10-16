import matplotlib.pyplot as plt
import numpy as np
from garden import *


def getSubgrid(t, pos):
    rmin = pos[0]-1
    rmax = pos[0]+2
    cmin = pos[1]-1
    cmax = pos[1]+2
    print(rmin, rmax, cmin, cmax)
    sub = t[rmin:rmax, cmin:cmax]
    return sub


def main():
    # LIMITS = (50,50)
    print("\nWelcome to the Secret Garden...\n")

    # Creating an objects
    ants = []
    bflies = []
    # Defining a list of colors for butterflies
    bflies_colors = ['red', 'blue', 'orange', 'purple', 'yellow']
    ladybugs = []
    caterpillars = []
    # Adding Obstacles
    plants = []
    rocks = []
    raindrops = []
    for index, color in enumerate(bflies_colors):
        brow = 10
        bcol = 5
        bflies.append(Butterfly('B'+str(index+1), (brow, bcol+index*5), color))
    for index in range(5):
        arow = 40
        acol = 15
        ants.append(Ant('A' + str(index+1), (arow, acol+index*5)))

        brow = 10
        bcol = 5
        # bflies.append(Butterfly('B'+str(index+1),
        #             (brow, bcol+index*5), 'yellow'))

        lrow = 10
        lcol = 30
        ladybugs.append(
            Ladybug('L'+str(index+1), (lrow, lcol+index*5), 'black'))

        crow = 10
        ccol = 15
        caterpillars.append(Caterpillar(
            'C' + str(index + 1), (crow, ccol + index * 5), 'green'))
    # Creating instances of Plant and Rock
    for index in range(3):
        prow = 10
        pcol = 10
        plants.append(Plant('P' + str(index + 1), (prow, pcol + index * 8)))

        rrow = 40
        rcol = 10
        rocks.append(Rock('R' + str(index + 1),
                     (rrow, rcol + index * 15), 'gray'))

    plt.figure(figsize=(8, 8))
    ax = plt.axes()
    ax.set_aspect("equal")

    # Getting the terrain value from CSV file
    tlist = []
    terrain_obj = open('garden3.csv', 'r')
    for line in terrain_obj:
        line_s = line.strip()
        # using list comprehension to convert each value into integer value
        ints = [int(x) for x in line_s.split(',')]
        tlist.append(ints)
    terrain_obj.close()
    # End of reading value from csv
    print(tlist)
    # new limits
    terrain = np.array(tlist)
    LIMITS = terrain.shape
    print(f'LIMITS are: {LIMITS}')
    for index in range(50):
        row = random.randint(0, LIMITS[0])
        col = random.randint(0, LIMITS[1])
        speed = random.uniform(1, 2)
        raindrops.append(Raindrop((row, col), speed))
    # print(tlist[0][4])
    # To plot objects at different time stam
    for timesteps in range(5):
        print('\nSteps Change')
        for i in range(5):
            plt.imshow(terrain, cmap='terrain_r')
            # Updating the positions of different objects at different time stamp
            ants[i].stepChange(getSubgrid(terrain, ants[i].getPos()), [
                               rock.getPos() for rock in rocks])
            # bflies[i].stepChange(getSubgrid(terrain, bflies[i].getPos()))
            # ladybugs[i].stepChange(getSubgrid(terrain, ladybugs[i].getPos()))
         #   caterpillars[i].stepChange(getSubgrid(
         #       terrain, caterpillars[i].getPos()))

        # Plotting the objects for visual representation
            ants[i].plotMe(ax, LIMITS)
            bflies[i].plotMe(ax, LIMITS)
            ladybugs[i].plotMe(ax, LIMITS)
            caterpillars[i].plotMe(ax, LIMITS)
        for rock in rocks:
            rock.plotMe(ax, LIMITS)

        for plant in plants:
            plant.plotMe(ax, LIMITS)
        # Simulation of caterpillar, butterfly and ladybug resting on collision with plants for 3 seconds

        for caterpillar in caterpillars:
            caterpillar.stepChange(getSubgrid(terrain, caterpillar.getPos()), [
                                   plant.getPos() for plant in plants])
        for butterfly in bflies:
            butterfly.stepChange(getSubgrid(terrain, butterfly.getPos()), [
                plant.getPos() for plant in plants])
        for ladybug in ladybugs:
            ladybug.stepChange(getSubgrid(terrain, ladybug.getPos()), [
                plant.getPos() for plant in plants])

        for raindrop in raindrops:
            if raindrop.getPos() is not None:
                raindrop.stepChange()
                # To check if the raindrop still exists
                if raindrop.getPos() is not None:
                    raindrop.plotMe(ax, LIMITS)
            else:
                # Remove raindrops
                raindrops.remove(raindrop)
        plt.title(f'This is Plot {timesteps+1}', fontsize='18')
        plt.grid()
        plt.pause(1)
        plt.cla()


if __name__ == "__main__":
    main()
