# Introduction #

Short introduction explaining the reasoning for FEM. A short explanation of the
utility of FEM

# Mesh Construction #

Why we need to construct the mesh

## Delaunay Triangulation ##

Explanation of what delaunay triangulation is, and why it is useful.

## Construction of Triangulation ##

Overview of the major methods sof the construciton of delaunay triangulation,
and the merits of each one.

### Divide and Conqure ###

Short explanation of the divide and conqure algorithm develped by chew.

### Sweep Line ###

This is one of the faster methods for constructing the delaunay triangulation.

### Edge Flipping ###

Explanation of the edge flipping algorithm, with psudocode of the algorithms
utilized in the process.

#### BinSort ####

#### TriLoc(Walking mesh) ####

#### EdgeFlip ####

#### In Circumcircle ####

## Construction of Constrained Triangulation ##

Comment on the importance and use of the constrained alternative of dalaunay
triangulations

### Divide and Conqure ###

There is a modification that construces the constrained triangulation at the
same time.

### Sweep Line ###

There is a implementation that construces the constrained triangulation during
the implementation of the unconstrained sweep line algorithm. This is extreamly
fast, but was too difficult for me to implement.

### Edge Flipping ###

This just uses the same stuff from triloc and edge flipping, but it adds one or
two new algorithms.

#### Intersecting edges ####

#### Find All intersections ####

# System Of Equations #

## Sparse Matrix ##

Most of the elements in the matricies will be zero, so we want to implement
optimizations for sparce matricies. Explain more as to why this is important,
from the memory issues.

## Krylov Subspaces ##

This is a really cool thing. It is a subspace of the solution of the system of
linear equations. Check with paul on the proof of this.

## Iterative Methods ##

These are a methods for approximating the solution to systems of linear
equation of the form $Ax=b$. They convere to the actual soultion at different
rates. And we require a tolerance that we stop at.

### Stationary Methods ###

These methods are very simple to implement and understand, but they converge
very slowly, and are not great. They should be avoided.

* Jacobi
* Gauss-Seidel
* SOR
* SSOR

#### Guass-Seidel ####

We present an implementation of this method??

### Nonstationary Methods ###

These methods are much faster, but they are much more complicated and take a
lot more work to implement. Most of these use sequences of orthogonal vecotrs,
which can be constructed by the basis if Krylov subspace.

* Conjugate Gradient
* Minimum Residual
* Conjugate Gradient on the Normal Equations
* Generalized Minimal Residual
* BiConjugate Gradient
* Quasi-Minimal Residual
* Conjugate Gradient Squared
* Biconjugate Gradient Stabilized
* Chebyshev Iteration

#### GMRES ####

We examine further an implementation of gmres, and provide psudocode.
