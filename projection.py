import numpy as np
import matplotlib.pyplot as plt

def main():
    f = 2.0
    zAve = 20.0

    pyrVertices = np.matrix([ [0, 0, (3 ** .5)/2, (3 ** .5)/6], [0, 1, .5, .5], [0, 0, 0, (3 ** .5)/2], [1, 1, 1, 1] ], 'float')
    pyrEdges = np.matrix('0 1 1 1; 0 0 1 1; 0 0 0 1; 0 0 0 0')

    prismVertices = np.matrix([ [0, 0, (3 ** .5)/2, 0, 0, (3 ** .5)/2], [0, 1, .5, 0, 1, .5], [0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1] ], 'float')
    prismEdges = np.matrix('0 1 1 1 0 0; 0 0 1 0 1 0; 0 0 0 0 0 1; 0 0 0 0 1 1; 0 0 0 0 0 1; 0 0 0 0 0 0')

    cubeVertices = np.matrix('1 1 1 1 -1 -1 -1 -1; 1 1 -1 -1 1 1 -1 -1; 1 -1 1 -1 1 -1 1 -1; 1 1 1 1 1 1 1 1', 'float')
    cubeEdges = np.matrix('0 1 1 0 1 0 0 0; 0 0 0 1 0 1 0 0; 0 0 0 1 0 0 1 0; 0 0 0 0 0 0 0 1; 0 0 0 0 0 1 1 0; 0 0 0 0 0 0 0 1; 0 0 0 0 0 0 0 1; 0 0 0 0 0 0 0 0')

    pyrPrep = translation(0, -15, 25) * rotation(np.pi/12., 0) * rotation(np.pi/2., -np.pi/2.) * scaling(3.5, 3.5, 3.5) * pyrVertices
    prismPrep = translation(3, -16, 20) * rotation(np.pi/3., -2 * np.pi/3.) * scaling(2, 3 ** .5, 5) * prismVertices
    cubePrep = translation(3, -10, 20) * rotation(np.pi/12., np.pi/3.) * cubeVertices

    plt.figure(1)
    plotMesh(pProj(f) * pyrPrep, pyrEdges)
    plotMesh(pProj(f) * prismPrep, prismEdges)
    plotMesh(pProj(f) * cubePrep, cubeEdges)
    plt.axis('equal')

    plt.figure(2)
    plotMesh(wpProj(f, zAve) * pyrPrep, pyrEdges)
    plotMesh(wpProj(f, zAve) * prismPrep, prismEdges)
    plotMesh(wpProj(f, zAve) * cubePrep, cubeEdges)
    plt.axis('equal')

    plt.figure(3)
    plotMesh(oProj() * pyrPrep, pyrEdges)
    plotMesh(oProj() * prismPrep, prismEdges)
    plotMesh(oProj() * cubePrep, cubeEdges)
    plt.axis('equal')

    plt.show()

def pProj(f):
    return np.matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, (1 / f), 0] ])

def wpProj(f, zAve):
    return np.matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, (zAve / f)] ])

def oProj():
    return np.matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1] ])

def rotation(theta, phi):
    return np.matrix([ [np.cos(theta), -np.sin(theta), 0, 0], [np.sin(theta), np.cos(theta), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1] ], 'float') * np.matrix([ [np.cos(phi), 0, -np.sin(phi), 0], [0, 1, 0, 0], [np.sin(phi), 0, np.cos(phi), 0], [0, 0, 0, 1] ], 'float')

def translation(x, y, z):
    return np.matrix([ [1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1] ])

def scaling(i, j, k):
    return np.matrix([ [i, 0, 0, 0], [0, j, 0, 0], [0, 0, k, 0], [0, 0, 0, 1] ])

def normalize(vertices):
    return (vertices / vertices[2])[0:-1]

def markVertex(edges, i):
    edges[i, :] = -edges[i, :]
    edges[:, i] = -edges[:, i]
    edges[i, i] = -edges[i, i]

def plotMesh(vertices, edges):
    vertices = normalize(vertices)
    for i in range(0, edges.shape[0]):
        for j in range(i + 1, edges.shape[0]):
            if edges[i, j] != 0:
                if edges[i, j] == 1:
                    plt.plot([vertices[0, i], vertices[0, j]], [vertices[1, i], vertices[1, j]], 'b-', linewidth = 2)
                else:
                    plt.plot([vertices[0, i], vertices[0, j]], [vertices[1, i], vertices[1, j]], 'b--')

if __name__ == '__main__':
    main()
