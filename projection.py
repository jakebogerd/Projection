import numpy as np
import matplotlib.pyplot as plt

def main():

    # A triangular pyramid
    pyrVertices = np.matrix([ [0, 0, (3 ** .5)/2, (3 ** .5)/6], [0, 1, .5, .5], [0, 0, 0, (3 ** .5)/2], [1, 1, 1, 1] ], 'float')
    pyrEdges = np.matrix('0 1 1 1; 0 0 1 1; 0 0 0 1; 0 0 0 0')

    # A triangular prism
    prismVertices = np.matrix([ [0, 0, (3 ** .5)/2, 0, 0, (3 ** .5)/2], [0, 1, .5, 0, 1, .5], [0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1] ], 'float')
    prismEdges = np.matrix('0 1 1 1 0 0; 0 0 1 0 1 0; 0 0 0 0 0 1; 0 0 0 0 1 1; 0 0 0 0 0 1; 0 0 0 0 0 0')

    # A cube
    cubeVertices = np.matrix('1 1 1 1 -1 -1 -1 -1; 1 1 -1 -1 1 1 -1 -1; 1 -1 1 -1 1 -1 1 -1; 1 1 1 1 1 1 1 1', 'float')
    cubeEdges = np.matrix('0 1 1 0 1 0 0 0; 0 0 0 1 0 1 0 0; 0 0 0 1 0 0 1 0; 0 0 0 0 0 0 0 1; 0 0 0 0 0 1 1 0; 0 0 0 0 0 0 0 1; 0 0 0 0 0 0 0 1; 0 0 0 0 0 0 0 0')

    # Scale, rotate, and translate the models with matrix multiplication
    pyrPrep = translation(0, -15, 15) * rotation(np.pi/12., 0) * rotation(np.pi/2., -np.pi/2.) * scaling(3.5, 3.5, 3.5) * pyrVertices
    prismPrep = translation(10, -16, 20) * rotation(np.pi/3., -2 * np.pi/3.) * scaling(2, 3 ** .5, 5) * prismVertices
    cubePrep = translation(3, -10, 25) * rotation(np.pi/12., np.pi/3.) * scaling(3, 3, 3) * cubeVertices

    # Plot the perspective projections
    plt.figure(1)
    plotMesh(pProj(2.0) * pyrPrep, pyrEdges)
    plotMesh(pProj(2.0) * prismPrep, prismEdges)
    plotMesh(pProj(2.0) * cubePrep, cubeEdges)
    plt.axis('equal')

    # Plot the weak perspective projections
    plt.figure(2)
    plotMesh(wpProj(2.0, 15) * pyrPrep, pyrEdges)
    plotMesh(wpProj(2.0, 20) * prismPrep, prismEdges)
    plotMesh(wpProj(2.0, 25) * cubePrep, cubeEdges)
    plt.axis('equal')

    # Plot the orthographic projections
    plt.figure(3)
    plotMesh(oProj() * pyrPrep, pyrEdges)
    plotMesh(oProj() * prismPrep, prismEdges)
    plotMesh(oProj() * cubePrep, cubeEdges)
    plt.axis('equal')

    plt.show()

# Returns a perspective projection matrix for the given focal length f
def pProj(f):
    return np.matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, (1 / f), 0] ])

# Returns a weak perspective projection matrix for the given focal length f and average depth zAve
def wpProj(f, zAve):
    return np.matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, (zAve / f)] ])

# Returns an orthographic projection matrix
def oProj():
    return np.matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1] ])

# Returns a matrix for the composition of a rotation in the XZ plane by angle phi and then a rotation in the XY plane by angle theta
def rotation(theta, phi):
    return np.matrix([ [np.cos(theta), -np.sin(theta), 0, 0], [np.sin(theta), np.cos(theta), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1] ], 'float') * np.matrix([ [np.cos(phi), 0, -np.sin(phi), 0], [0, 1, 0, 0], [np.sin(phi), 0, np.cos(phi), 0], [0, 0, 0, 1] ], 'float')

# Returns a matrix for translation x = x + a, y = y + b, z = z + c
def translation(a, b, c):
    return np.matrix([ [1, 0, 0, a], [0, 1, 0, b], [0, 0, 1, c], [0, 0, 0, 1] ])

# Returns a matrix for scaling x = i * x, y = j * y, z = k * z
def scaling(i, j, k):
    return np.matrix([ [i, 0, 0, 0], [0, j, 0, 0], [0, 0, k, 0], [0, 0, 0, 1] ])

# Divide out homogeneous coordinate and truncate vectors to prepare for plotting
def normalize(vertices):
    return (vertices / vertices[2])[0:-1]

# Plot the projected coordinates of a mesh by connecting adjacent vertices with line segments
def plotMesh(vertices, edges):
    vertices = normalize(vertices)
    for i in range(0, edges.shape[0]):
        for j in range(i + 1, edges.shape[0]):
            if edges[i, j]:
                plt.plot([vertices[0, i], vertices[0, j]], [vertices[1, i], vertices[1, j]], 'b-', linewidth = 2)

if __name__ == '__main__':
    main()
