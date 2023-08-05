# Null space optimizer
`nullspace_optimizer` is a package implementing the null space algorithm for nonlinear constrained
optimization.

Please cite the following references when using this source:

FEPPON, Florian, ALLAIRE, Grégoire, et DAPOGNY, Charles.
*Null space gradient flows for constrained optimization with applications to
 shape optimization.* 2019. HAL preprint [hal-01972915](https://hal.archives-ouvertes.fr/hal-01972915/document).

FEPPON, Florian. *Shape and topology optimization of multiphysics systems.* 2019.
Université Paris-Saclay. Thèse préparée à l'École polytechnique.


# Installation

## With pip
```bash
# Light version
pip install nullspace_optimizer

# Full dependencies including colored output and plotting features
pip install nullspace_optimizer[colored,matplotlib]
```

## Manual installation
Add the package to the `PYTHONPATH` environment variable.

# Running examples
A few examples of 2-d inequality constrained optimization are available in the `examples' folder.
They can be run from command line with

```bash
python -m nullspace_optimizer.examples.ex0
python -m nullspace_optimizer.examples.ex1
python -m nullspace_optimizer.examples.ex2
```
and so on. 

For instance, example `ex1` solves the following optimization problem:
```math
\newcommand{\<}{\leq}
\begin{aligned} \min_{(x_0,x_1)\in\mathbb{R}^2} & \quad (x_0+1)^2+(x_1+1)^2 \\
s.t. &\quad  \left\{ \begin{aligned} x_0^2+x_1^2-1 & \< 0\\
                             x_0+x_1-1 & \< 0 \\
                             -x_1-0.7 & \<0.
                             \end{aligned}\right.
\end{aligned}
```
Running `python -m nullspace_optimizer.examples.ex1` should produce the following figure:


<img src="nullspace.png" align="center" alt="Null space gradient flow trajectories" width="40%">

# Requirements
Runs with python 3.6 and the following libraries:
* numpy (>=1.12.1)
* scipy (>=0.19.1)
* cvxopt (>=1.2.1)

Optional dependencies:
* colored (>=1.3.93)   *(for colored output)*
* matplotlib (>=2.0.2) *(for displaying figures while running examples)*
