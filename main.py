from ActionDataFile import getTimeValueFromFile
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from os.path import dirname, join


def getValues(pathFile):

    path = pathFile
    return getTimeValueFromFile(path)


if __name__ == '__main__':

    values = getValues("../NIR3/NIR3/dataInPoint.txt")
    timeValues = values[0]
    cancerValues = values[1]
    print(timeValues)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)

    fig.suptitle(f"Dynamics of the N", fontsize=28)
    plt.xlabel('time (month)', fontsize=26)
    plt.ylabel('N (mm)', fontsize=26)
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    # plt.plot(timeValues, cancerValues, label=f"Heat {heatDissipationValues[number - 1]}")
    plt.plot(timeValues, cancerValues)
    plt.grid(True)
    # plt.legend(prop={"size": 20})
    current_dir = dirname(__file__)
    pathSave = join(current_dir, f"data.png")
    plt.show()
    fig.savefig(pathSave)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
