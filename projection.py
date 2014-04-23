import numpy as np
import matplotlib.pyplot as plt

def main():
    f = 2.0
    zAve = 20.0

    cubeVertices = np.matrix('1 1 1 1 -1 -1 -1 -1; 1 1 -1 -1 1 1 -1 -1; 1 -1 1 -1 1 -1 1 -1; 1 1 1 1 1 1 1 1', 'float')
    cubeEdges = np.matrix('0 -1 -1 0 -1 0 0 0; 0 0 0 1 0 1 0 0; 0 0 0 1 0 0 1 0; 0 0 0 0 0 0 0 1; 0 0 0 0 0 1 1 0; 0 0 0 0 0 0 0 1; 0 0 0 0 0 0 0 1; 0 0 0 0 0 0 0 0')

    cubeProj = pProj(2.0) * translation(0, 10, 20) * rotation(0, np.pi/6.) * cubeVertices
    plotMesh(cartesian(cubeProj), cubeEdges)

def pProj(f):
    return np.matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, (1 / f), 0] ])

def wpProj(f, zAve):
    return np.matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, (zAve / f)] ])

def oProj():
    return

def rotation(theta, phi):
    return np.matrix([ [np.cos(theta), -np.sin(theta), 0, 0], [np.sin(theta), np.cos(theta), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1] ], 'float') * np.matrix([ [np.cos(phi), 0, -np.sin(phi), 0], [0, 1, 0, 0], [np.sin(phi), 0, np.cos(phi), 0], [0, 0, 0, 1] ], 'float')

def translation(x, y, z):
    return np.matrix([ [1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1] ])

def cartesian(vertices):
    return (vertices / vertices[2])[0:-1]

def plotMesh(vertices, edges):
    for i in range(0, 8):
        for j in range(i + 1, 8):
            if (edges[i, j] != 0):
                if (edges[i, j] == 1):
                    plt.plot([vertices[0, i], vertices[0, j]], [vertices[1, i], vertices[1, j]], 'b-', linewidth = 2)
                #else:
                    #plt.plot([vertices[0, i], vertices[0, j]], [vertices[1, i], vertices[1, j]], 'r--')
    plt.axis([-.25, .25, 1.25, .75])
    plt.show()

if (__name__ == "__main__"):
    main()
