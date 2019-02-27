#!/usr/bin/env python3

from math import *
import numpy as np
from numpy.linalg import solve
from pprint import pprint
import matplotlib.pyplot as plt

WEIGHT = [
    0.3335674062677772E-03, 0.7327880811491046E-03, 0.1033723454167925E-02,
    0.1195112498415193E-02, 0.1195112498415193E-02, 0.1033723454167925E-02,
    0.7327880811491046E-03, 0.3335674062677772E-03, 0.1806210919443461E-02,
    0.3967923151181667E-02, 0.5597437146194232E-02, 0.6471331443180639E-02,
    0.6471331443180639E-02, 0.5597437146194232E-02, 0.3967923151181667E-02,
    0.1806210919443461E-02, 0.4599755803015752E-02, 0.1010484287526739E-01,
    0.1425461651131868E-01, 0.1648010431039818E-01, 0.1648010431039818E-01,
    0.1425461651131868E-01, 0.1010484287526739E-01, 0.4599755803015752E-02,
    0.8017259531156730E-02, 0.1761248886287915E-01, 0.2484544071087993E-01,
    0.2872441038508419E-01, 0.2872441038508419E-01, 0.2484544071087993E-01,
    0.1761248886287915E-01, 0.8017259531156730E-02, 0.1073501897357062E-01,
    0.2358292149331603E-01, 0.3326776143412911E-01, 0.3846165753898425E-01,
    0.3846165753898425E-01, 0.3326776143412911E-01, 0.2358292149331603E-01,
    0.1073501897357062E-01, 0.1138879740452669E-01, 0.2501915606814251E-01,
    0.3529381699354388E-01, 0.4080402900378691E-01, 0.4080402900378691E-01,
    0.3529381699354388E-01, 0.2501915606814251E-01, 0.1138879740452669E-01,
    0.9223845391285393E-02, 0.2026314273544469E-01, 0.2858464328177232E-01,
    0.3304739223149761E-01, 0.3304739223149761E-01, 0.2858464328177232E-01,
    0.2026314273544469E-01, 0.9223845391285393E-02, 0.4509812715921713E-02,
    0.9907253959306707E-02, 0.1397588340693756E-01, 0.1615785427783403E-01,
    0.1615785427783403E-01, 0.1397588340693756E-01, 0.9907253959306707E-02,
    0.4509812715921713E-02
]

COORD = [
    0.9553660447100000, 0.8862103848242247E-03, 0.9553660447100000,
    0.4537789678039195E-02, 0.9553660447100000, 0.1058868260117431E-01,
    0.9553660447100000, 0.1822327082910602E-01, 0.9553660447100000,
    0.2641068446089399E-01, 0.9553660447100000, 0.3404527268882569E-01,
    0.9553660447100000, 0.4009616561196080E-01, 0.9553660447100000,
    0.4374774490517578E-01, 0.8556337429600001, 0.2866402391985981E-02,
    0.8556337429600001, 0.1467724979327651E-01, 0.8556337429600001,
    0.3424855503358430E-01, 0.8556337429600001, 0.5894224214571626E-01,
    0.8556337429600001, 0.8542401489428375E-01, 0.8556337429600001,
    0.1101177020064157, 0.8556337429600001, 0.1296890072467235,
    0.8556337429600001, 0.1414998546480140, 0.7131752428600000,
    0.5694926133044352E-02, 0.7131752428600000, 0.2916054411712861E-01,
    0.7131752428600000, 0.6804452564827500E-01, 0.7131752428600000,
    0.1171055801775613, 0.7131752428600000, 0.1697191769624387,
    0.7131752428600000, 0.2187802314917250, 0.7131752428600000,
    0.2576642130228714, 0.7131752428600000, 0.2811298310069557,
    0.5451866848000000, 0.9030351006711630E-02, 0.5451866848000000,
    0.4623939674940125E-01, 0.5451866848000000, 0.1078970888004545,
    0.5451866848000000, 0.1856923986620134, 0.5451866848000000,
    0.2691209165379867, 0.5451866848000000, 0.3469162263995455,
    0.5451866848000000, 0.4085739184505988, 0.5451866848000000,
    0.4457829641932884, 0.3719321645800000, 0.1247033193690498E-01,
    0.3719321645800000, 0.6385362269957356E-01, 0.3719321645800000,
    0.1489989161403976, 0.3719321645800000, 0.2564292182833579,
    0.3719321645800000, 0.3716386171366422, 0.3719321645800000,
    0.4790689192796024, 0.3719321645800000, 0.5642142127204264,
    0.3719321645800000, 0.6155975034830951, 0.2143084794000000,
    0.1559996151584746E-01, 0.2143084794000000, 0.7987871227492103E-01,
    0.2143084794000000, 0.1863925811641285, 0.2143084794000000,
    0.3207842387034378, 0.2143084794000000, 0.4649072818965623,
    0.2143084794000000, 0.5992989394358715, 0.2143084794000000,
    0.7058128083250790, 0.2143084794000000, 0.7700915590841526,
    0.9132360790000005E-01, 0.1804183496379599E-01, 0.9132360790000005E-01,
    0.9238218584838476E-01, 0.9132360790000005E-01, 0.2155687489628060,
    0.9132360790000005E-01, 0.3709968314854498, 0.9132360790000005E-01,
    0.5376795606145502, 0.9132360790000005E-01, 0.6931076431371940,
    0.9132360790000005E-01, 0.8162942062516152, 0.9132360790000005E-01,
    0.8906345571362040, 0.1777991514999999E-01, 0.1950205026019779E-01,
    0.1777991514999999E-01, 0.9985913490381848E-01, 0.1777991514999999E-01,
    0.2330157982952792, 0.1777991514999999E-01, 0.4010234473667467,
    0.1777991514999999E-01, 0.5811966374832533, 0.1777991514999999E-01,
    0.7492042865547208, 0.1777991514999999E-01, 0.8823609499461815,
    0.1777991514999999E-01, 0.9627180345898023
]

PTS = [(0, 0), (-1, 1), (1, 1), (1, -1), (-1, -1), (-0.5, 0), (0, 0.5),
       (0.5, 0), (0, -0.5)]
TRI = [(1, 6, 2), (1, 4, 5), (1, 5, 6), (2, 6, 7), (2, 7, 3), (6, 5, 0),
       (6, 0, 7), (0, 5, 8), (0, 8, 7), (5, 4, 8), (8, 3, 7), (8, 4, 3)]


def integrate(func, tri):
    """
    Preforms gaussian quadrature numeric integration according to my source
    for the coordiantes and the weights, this can integrate a 64 degree
    polynomial with a degree of percision of 15... I think, I need to research
    this method of integration more.
    """
    x1 = PTS[tri[0]][0]
    x2 = PTS[tri[1]][0]
    x3 = PTS[tri[2]][0]
    y1 = PTS[tri[0]][1]
    y2 = PTS[tri[1]][1]
    y3 = PTS[tri[2]][1]
    return sum([
        WEIGHT[i] * func(COORD[2 * i] * x1 + COORD[(2 * i) + 1] * x2 +
                         (1.0 - COORD[2 * i] - COORD[(2 * i) + 1]) * x3,
                         COORD[2 * i] * y1 + COORD[(2 * i) + 1] * y2 +
                         (1.0 - COORD[2 * i] - COORD[(2 * i) + 1]) * y3)
        for i in range(len(WEIGHT))
    ])


def pder(func, x, y, dx, dy):
    """
    This preforms the partial derivative using finite difference, This is the
    exact same thing as you would normaly think, just with a higher degree of
    percission (8). Thus it should be able to more accuratly differentiate
    higher order polynomials, and provide a more accurate approximation.

    I think this might be overkill, I'm only ever differentiating the local
    basis functions which are planes... So this is definently overkill, but
    it can't make the approximation worse. Right?
    """
    return (1.0 / 280.0 * func(x - 4 * dx, y - 4 * dy) - 4.0 / 105 * func(
        x - 3 * dx, y - 3 * dy) + 1.0 / 5.0 * func(x - 2 * dx, y - 2 * dy) -
            4.0 / 5.0 * func(x - dx, y - dy) + 4.0 / 5.0 * func(x + dx, y + dy)
            - 1.0 / 5.0 * func(x + 2 * dx, y + 2 * dy) +
            4.0 / 105.0 * func(x + 3 * dx, y + 3 * dy) -
            1.0 / 280.0 * func(x + 4 * dx, y + 4 * dy)) / (dx + dy)


def basis(tri, vert):
    """This gets the basis function, which is the barycentric coordinate
    system, I need to check that this is a valid way of handling it. I think
    that is should be."""
    x1 = PTS[tri[vert]][0]
    y1 = PTS[tri[vert]][1]
    x2 = PTS[tri[(vert + 1) % 3]][0]
    y2 = PTS[tri[(vert + 1) % 3]][1]
    x3 = PTS[tri[(vert + 2) % 3]][0]
    y3 = PTS[tri[(vert + 2) % 3]][1]
    return lambda x, y: ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))


def plot_func(func, res, name):
    """I was just using this to generate the plot of the forcing function."""
    data = np.zeros((res, res))
    for i, x in enumerate(list(np.linspace(-1, 1, res))):
        for j, y in enumerate(list(np.linspace(-1, 1, res))):
            data[res - i - 1][j] = func(x, y)
    plt.imsave("{}.png".format(name), data, vmin=0, vmax=4.5, cmap='jet')


def main():
    # Some constants of the heat equation
    rho = 1
    cp = 1
    u = (1, 1)
    # The forcing function
    f = lambda x, y: (x - 0.5) * (x - 0.5) + (y - 0.5) * (y - 0.5)
    Fe = [[]]
    Ae = [[]]
    # Initalize global matricies
    F = np.zeros((9, 1))
    A = np.zeros((9, 9))

    # Do for every element in the mesh
    for e in range(len(TRI)):
        # Terrible stuff to make lists start at 1 to match the math
        Fe.append([0])
        Ae.append([[]])
        # Do for all three verticies of the triangle
        for i in range(3):
            Ae[-1].append([0])
            # Get the local basis function associated with the ith vertex of
            # the triangle.
            phi_i = basis(TRI[e], i)
            # Solve for the F_i^(e) and add that to the relavant global matrix
            # value.
            Fe[-1].append(integrate(lambda x, y: phi_i(x, y) * f(x, y), TRI[e]))
            F[TRI[e][i]] += Fe[-1][-1]
            # Do for all three verticies of the triangle
            for j in range(3):
                # Get the local basis function associated with the jth vertex
                # of the triangle.
                phi_j = basis(TRI[e], j)
                # Since A=C+K we first solve for C then solve for K then add
                # C+K to the local ang associated global matrix.
                c = integrate(lambda x, y: phi_i(x,y)*pder(phi_j, x, y, 0.001, 0)+phi_i(x,y)*pder(phi_j,x,y,0,0.001), TRI[e])
                k = integrate(lambda x, y: pder(phi_i, x, y, 0.001, 0)*pder(phi_j,x,y,0.001,0)+pder(phi_i,x,y,0,0.001)*pder(phi_j,x,y,0,0.001), TRI[e])
                Ae[-1][-1].append(c + k)
                A[TRI[e][i], TRI[e][j]] += Ae[-1][-1][-1]
            # Note that the A_ij can somewhat be though of as associateing to
            # the edges of the mesh, so A_ij has some contribution from the
            # two trianges that share that edge, then the A_ii have
            # contributions from all trianges that use i as a vertex.

    F = F.reshape((9,))

    # Apply boundary conditions
    A[1] = [0, 1, 0, 0, 0, 0, 0, 0, 0]
    A[2] = [0, 0, 1, 0, 0, 0, 0, 0, 0]
    A[3] = [0, 0, 0, 1, 0, 0, 0, 0, 0]
    A[4] = [0, 0, 0, 0, 1, 0, 0, 0, 0]
    F[1] = 0
    F[2] = 0
    F[3] = 0
    F[4] = 0
    # Solve for boundaries =0
    x = solve(A, F)
    print("CASE 1:", x)
    F[1] = 2.5
    F[2] = 0.5
    F[3] = 2.5
    F[4] = 4.5
    # Solve for other case
    x = solve(A, F)
    print("CASE 2:", x)
    # plot_func(f, 500, "forcing")


if __name__ == "__main__":
    main()
