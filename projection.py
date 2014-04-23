import numpy as np
import matplotlib.pyplot as plt

def main():
    oProj = np.matrix('1 0 0 0; 0 1 0 0; 0 0 0 1', 'float')
    wpProj = np.matrix('1 0 0 0; 0 1 0 0; 0 0 0 1', 'float')
    pProj = np.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0', 'float')

    f = 2.0
    zAve = 20.0

    wpProj[2, 3] = zAve / f
    pProj[2, 2] = 1 / f

    oCube = np.matrix('1 1 1 1 -1 -1 -1 -1; 1 1 -1 -1 1 1 -1 -1; 1 -1 1 -1 1 -1 1 -1; 1 1 1 1 1 1 1 1', 'float')
    Cube = np.matrix('4 1 1 1 -1 -1 -1 -1; 4 1 -1 -1 1 1 -1 -1; 4 -1 1 -1 1 -1 1 -1; 1 1 1 1 1 1 1 1', 'float')
    adjCube = np.matrix('0 1 1 0 1 0 0 0; 0 0 0 1 0 1 0 0; 0 0 0 1 0 0 1 0;0 0 0 0 0 0 0 1; 0 0 0 0 0 1 1 0; 0 0 0 0 0 0 0 1; 0 0 0 0 0 0 0 1; 0 0 0 0 0 0 0 0')
    rCube = rotation(0, np.pi/3.) * oCube
    #tCube = np.matrix('1 0 0 0; 0 1 0 10; 0 0 1 20; 0 0 0 1', 'float') * rCube
    tCube = translation(0, 10, 20) * rCube
    cubeProj = pProj * tCube
    plotMesh(homogeneousToCartesian(cubeProj), adjCube)

def rotation(theta, phi):
    return np.matrix([ [np.cos(theta), -np.sin(theta), 0, 0], [np.sin(theta), np.cos(theta), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1] ], 'float') * np.matrix([ [np.cos(phi), 0, -np.sin(phi), 0], [0, 1, 0, 0], [np.sin(phi), 0, np.cos(phi), 0], [0, 0, 0, 1] ], 'float')

def translation(x, y, z):
    return np.matrix([ [1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1] ])

def homogeneousToCartesian(vertices):
    return (vertices / vertices[2])[0:-1]

def plotMesh(vertices, edges):
    for i in range(0, 8):
        for j in range(i + 1, 8):
            if (edges[i, j]):
                plt.plot([vertices[0, i], vertices[0, j]], [vertices[1, i], vertices[1, j]], 'bo-', linewidth = 2)
    plt.axis([-.25, .25, 1.25, .75])
    plt.show()

if (__name__ == "__main__"):
    main()
