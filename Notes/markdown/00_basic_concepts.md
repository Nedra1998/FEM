# Basic Concepts #

The finite element method provides a method for generating algorithms for
approximating the solutions of differential equations.

## Weak Formulation of Boundary Value Problem ##

Considering the two-point boundary value problem

$$
\begin{aligned}
-\sder{u}{x}=f\quad(0,1)\\
u(0)=0\quad u'(1)=0
\end{aligned}
$$

Taking some function $v$, and finding the inner product with $f$, we find

$$
(f,v)=\int_{0}^{1}u'(x)v'(x)dx=a(u,v)
$$

We define a vector space $V$ as follows

$$
V \equiv \left\{ v\in L^2(0,1):\quad a(v,v)< \infty \ \text{and}\ v(0) = 0\right\}
$$

Using this we can characterize the solution to the differential equation as any
function $u\in V$ that satisifes the boundary condition and that satisfies

$$
a(u,v)=(f,v)\quad \forall v\in V
$$

This is called the *variational* or *weak* formulation of the differential
equation. It is variational because $v$ is allowed to vary arbitrarily. It is
called weak, because there are other ways in which to interpret the equation
with less restrictives assumptions on $f$.

## Ritz-Galrkin Approximation ##

Let $S \subset V$ be any (finite dimensional) subspace. Then when we replace
$V$ in the previous declaration we find

$$
u_S \in S\quad a(u_S,v)=(f,v)\quad \forall v\in S
$$

With this approximation, it can be shown that the solution $u_S$ must *exist*
and be *unique*.

## Error Estimates ##

Observing the fundamental *orthogonality* between $u$ and $u_S$ implies
$$
a(u-u_S,w)=0\quad \forall w\in S
$$

Now we define the energy norm as

$$
\norm{v}_E=\sqrt{a(v,v)}
$$
Using this norm, the Schwarz' inequality relates the energy norm and
inner-product

$$
\abs{a(v,w)}\leq \norm{v}_E\norm{w}_E\quad \forall v,w \in V
$$

## Piecewise Polynomial Spaces ##

## Relationship to Difference Methods ##

## Computer Implementation of FInite Element Methods ##

## Local Estimates ##

## Adaptive Approximation ##

## Weighted Norm Estimates ##

