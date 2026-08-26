# Critical disk sharp constant and Morrey attainment

Status: `partial_new_result_and_literature_answer` (subject to human review)

## Source question

Lorenzo Brasco, David Gómez-Castro, and Juan Luis Vázquez,
*Characterisation of homogeneous fractional Sobolev spaces*,
arXiv:2007.08000v2 (2021).

Section 6, arXiv PDF page 22, asks for the optimal constants and extremals in
the subcritical Sobolev, critical Poincaré-Wirtinger, and supercritical Morrey
embeddings.

## New sharp critical case

For the critical local Hilbert case `(n,s,p)=(2,1,2)`, and every disk
`B_R(x0)`, the exact inequality is

```text
integral_{B_R} |u-u_B|^2
    <= (R^2 / j_{0,1}^2) integral_{R^2} |grad u|^2,
```

where `j_{0,1}=2.404825557...` is the first positive zero of `J_0`.  The
dimensionless sharp constant is

```text
1/j_{0,1}^2 = 0.1729150690...
```

and it is attained in the homogeneous completion.  On the unit disk, all
nonconstant extremals are, up to a constant and a nonzero first angular mode,

```text
J_1(j r)(A cos(theta)+B sin(theta)),  r <= 1,
J_1(j) r^(-1)(A cos(theta)+B sin(theta)),  r >= 1.
```

The proof uses Fourier modes and the exact exterior Dirichlet-to-Neumann
energy.  The first mode has boundary condition
`j J_1'(j)+J_1(j)=j J_0(j)=0`.

## Later Morrey result

Brasco, Prinari, and Sk, arXiv:2309.06058v1, Theorem 6.1 on PDF page 23,
explicitly cite the source paper and prove that the sharp supercritical
fractional Morrey infimum is attained for every `sp>N`.  They do not compute
the sharp constant explicitly.

## Scope

The packet fully resolves one important critical parameter choice and records
the later positive answer to the Morrey-attainment branch.  It does not give
the sharp constants for general fractional parameters or nonlinear critical
cases.

Files:

- `source_paper.pdf`: arXiv:2007.08000v2.
- `supporting_paper_2309.06058.pdf`: later Morrey-extremal paper.
- `figures/open_question_crop.png`: source question, PDF page 22.
- `figures/morrey_theorem_crop.png`: later Theorem 6.1, PDF page 23.
- `main.tex`, `solution_packet.pdf`: full proof, literature status, and scope.
- `verification.py`: numerical Bessel/integral audit of the extremal.

