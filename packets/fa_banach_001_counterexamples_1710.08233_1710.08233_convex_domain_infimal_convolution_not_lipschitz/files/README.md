# Convex domains do not preserve Lipschitzness under infimal convolution

Status: `candidate_counterexample_likely_valid`.

Source: Simon Zugmeyer, *Sharp trace Gagliardo--Nirenberg--Sobolev
inequalities for convex cones, and convex domains*, arXiv:1710.08233,
Section 2.2, source PDF page 10.

## Result

The source conjecture is false already in `R^2`.  Let `D` be the closed
Euclidean unit disk and define

```text
f(a1,a2) = 1+a2  on D,  +infinity outside D,
g(b1,b2) = 0     on D,  +infinity outside D.
```

The functions have the same compact convex domain with nonempty interior;
their restrictions are respectively 1- and 0-Lipschitz.  They are also
proper, lower semicontinuous, convex, and nonnegative.

For `x_t=(t,0)`, `0<=t<=2`, the convolution has the exact formula

```text
(f square g)(x_t) = 1 - sqrt(1-t^2/4).
```

Consequently, its difference quotient between `x_(2-epsilon)` and `x_2` is

```text
sqrt(1/epsilon - 1/4),
```

which tends to infinity.  Thus the infimal convolution is not Lipschitz on
its domain `D+D=2D` (indeed, it is not locally Lipschitz at `(2,0)` relative
to that domain).

The same construction on the open unit disk is not globally Lipschitz either:
compare the two interior points `x_(2-epsilon)` and `x_(2-2epsilon)`.  This
guards against an interpretation in which the source intended open domains.

## Proof mechanism

The feasible decompositions of `(t,0)` correspond to the lens
`D intersect ((t,0)-D)`.  The affine cost `1+a_2` selects the bottom of this
lens.  Its vertical radius is exactly `sqrt(1-t^2/4)`, which collapses only at
square-root speed as `t` approaches `2`.

## Verification and scope

The exact proof is in `solution_packet.pdf`.  The checker confirms the scalar
minimax identity on 151,151 rational grid pairs and prints the divergent
closed- and open-disk quotients.

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1710.08233_convex_domain_infimal_convolution_not_lipschitz/code/verify_counterexample.py
```

This settles the printed global-Lipschitz conjecture negatively.  It does not
refute the weaker statement that the convolution is locally Lipschitz at every
point in the interior of the Minkowski-sum domain.

Human review recommendation: verify the intended meaning of “Lipschitz on the
domain” in the source sentence and the one-line lens minimization.  The
construction itself is elementary and exact.

## Files

- `source_paper.pdf`: the arXiv source paper.
- `figures/open_problem_crop.png`: source PDF page 10.
- `main.tex`, `solution_packet.pdf`: complete proof packet.
- `code/verify_counterexample.py`: exact rational and numerical stress checks.
- `novelty.md`: bounded duplicate/literature search.
- `verification.md`: proof, build, and rendering report.
