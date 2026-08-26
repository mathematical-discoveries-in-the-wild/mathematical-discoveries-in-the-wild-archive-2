# Verification report

Verdict: `candidate_counterexample_likely_valid`

## Source and quantifier audit

Section 5 asks whether quotienting the extreme points of `M_D(A)` by
unitaries commuting with `D`, for arbitrary positive `d` and arbitrary `A`,
leaves finitely many extreme-point classes.  No restriction excluding maximal
states is stated.  One admissible pair with infinitely many classes therefore
gives a negative answer to general finiteness.

## Channel audit

Normalize `D` to a full-rank density matrix and let `d=lambda_min(D)`.  For an
arbitrary state `rho`,

```text
D-d rho = (D-d I)+d(I-rho) >= 0,
```

because `D>=d I` and every density matrix satisfies `rho<=I`.  Its trace is
`1-d`, so `tau=(D-d rho)/(1-d)` is a state.

In an eigenbasis with `e_1` a minimum-eigenvalue eigenvector, define

```text
T(X)=<e_1,Xe_1>rho + sum_{j=2}^n <e_j,Xe_j>tau.
```

This is a measure-and-prepare channel.  More explicitly, diagonalizing each
prepared state gives Kraus operators
`sqrt(s_jk)|v_jk><e_j|`; their adjoint products sum to the identity, so `T`
is completely positive and trace preserving.  Direct substitution gives

```text
T(|e_1><e_1|)=rho,
T(D)=d rho+(1-d)tau=D.
```

Thus every state lies in `M_D(A)`.  The reverse containment holds because a
channel maps a state to a state.

## Extreme-point audit

The extreme points of the density matrices are exactly the rank-one
projections.  Rank at least two permits a nonzero traceless perturbation inside
the support; rank one forces every state in a convex decomposition to have the
same one-dimensional support.

Write `D=sum_j lambda_j P_j` over its distinct eigenvalues.  Every unitary in
the commutant is block diagonal on the spectral subspaces and preserves

```text
w_j(psi)=||P_j psi||^2.
```

Conversely, two unit vectors with the same weights can be matched component by
component by unitaries on the spectral subspaces.  Hence their rank-one
projections are commutant-conjugate exactly when their weight vectors agree.
Every simplex weight vector is realized.  The quotient is therefore
`Delta_{r-1}`, where `r` is the number of distinct eigenvalues.  It is
uncountable exactly when `D` is nonscalar.

## Explicit qubit audit

For `D=diag(1/3,2/3)` and `A=|e_1><e_1|`, the preceding construction gives
`M_D(A)` equal to the Bloch ball.  The pure states

```text
P_t = |sqrt(t)e_1+sqrt(1-t)e_2><same|,  0<=t<=1,
```

are extreme.  A diagonal unitary preserves `t`, so distinct parameters give
inequivalent extreme points.

## Novelty audit

The run indexes were searched for `2004.05613`, `D-majorization`, `M_D(A)`,
commutant, unitary equivalence, and extreme points.  Bounded web/arXiv searches
on 11 August 2026 used the exact question and close variants.  No explicit
resolution was found.  The source author's 2020 dissertation repeats the
question.  Because the construction builds directly on the source's maximal
state mechanism, novelty confidence is moderate, not definitive.

## Human verifier focus

1. Confirm the source's informal question has the universal/general reading
   used here and does not silently exclude maximal initial states.
2. Check that equality of spectral weights is sufficient, not only necessary,
   for commutant equivalence.
3. Check the final PDF crops and all displayed formulas after rendering.

## Packet render audit

`main.tex` compiled without LaTeX warnings to a four-page PDF.  All four pages
were rendered at 150 dpi and inspected individually.  The two source crops are
readable, the complete question appears on page 2, and no clipping, overlap,
broken glyphs, or malformed displays were found.  Final packet SHA-256:

```text
1581e59a86aea8e89ad362780d45f244eaacb58909b45b56d01f4b65e817c996
```

