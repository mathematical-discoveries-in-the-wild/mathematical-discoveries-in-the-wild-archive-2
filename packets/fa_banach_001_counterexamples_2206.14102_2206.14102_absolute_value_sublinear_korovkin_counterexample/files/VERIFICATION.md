# Verification

## Source and target

- arXiv:2206.14102v1, PDF page 12, explicitly asks whether Wulbert's
  non-monotone theorem has an analogue for continuous sublinear maps
  `L1[0,1] -> L1[0,1]`.
- arXiv:2403.03476v2, Theorem 1.3, restates Wulbert's original `L1` theorem:
  convergence on `1` in norm, weak convergence on `x,x^2`, and operator norms
  tending to one force norm convergence on every function, for linear maps.

## Counterexample audit

- Pointwise triangle inequality proves subadditivity of `T(f)=|f|`; positive
  homogeneity is exact for nonnegative scalars.
- The lattice inequality `||f|-|g|| <= |f-g|` proves 1-Lipschitz continuity.
- `||T(f)||_1=||f||_1`, so the nonlinear operator norm is exactly one.
- `1,x,x^2` are nonnegative on `[0,1]`, so all are fixed exactly.
- `T(-1)=1`; the norm error is `int_0^1 2 dt=2`, and pairing against the
  constant dual function one also proves failure of weak convergence.
- `T` is not monotone on the full lattice: `-1<=0` but `T(-1)=1>T(0)=0`.
- The same proof works for every test family contained in the positive cone.

## Scope and novelty

- The result refutes the direct replacement of Wulbert's linear maps by the
  source's continuous sublinear maps.  It does not claim that every possible
  modified sign-symmetric analogue is false.
- Six focused upgrade/audit routes are recorded in the attempt file.  A
  bounded search through 2026-08-11 found no indexed prior statement of this
  modulus obstruction for the source question.

## Render audit

- The final PDF was compiled with intermediates in `tmp/`, text-extracted,
  rendered page by page, and visually inspected on 2026-08-11.
- The source crop is legible and contains the complete open-question sentence.
