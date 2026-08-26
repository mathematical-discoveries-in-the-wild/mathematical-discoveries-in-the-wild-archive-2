# Globally continuous cohomology of tori

Status: `candidate_full_solution_likely_valid`

Source: Tim Austin, *Partial difference equations over compact Abelian groups,
I: modules of solutions*, arXiv:1305.7269, Question 10.1 on physical PDF
page 91.

## Result

Question 10.1 asks whether `H^3_cts(T,T)` is non-zero, where `H_cts` is
defined using globally continuous inhomogeneous bar cochains and the
coefficient action is trivial.  The answer is **no**.  More generally,

```text
H^0_cts(T^d,T^m) = T^m,
H^1_cts(T^d,T^m) = Hom_cts(T^d,T^m) = Mat_{m x d}(Z),
H^n_cts(T^d,T^m) = 0 for every n >= 2.
```

Every continuous action of `T^d` on `T^m` by group automorphisms is already
trivial, so this covers all continuous toral module structures.

## Proof mechanism

Pass to normalized continuous cochains.  In degree `n>=2`, a normalized map
`(T^d)^n -> T^m` vanishes on the fat wedge and hence factors through the smash
product `(T^d)^{ smash n}`.  This finite CW complex has no one-cells and is
simply connected, so the cochain has a based continuous lift to `R^m`.

If the original cochain is a cocycle, the differential of the lift is a
continuous `Z^m`-valued function on the connected space `(T^d)^(n+1)`.
It is constant, and normalization makes that constant zero.  The lift is
therefore a genuine real cocycle.  Haar averaging gives a continuous real
primitive, whose reduction modulo `Z^m` is a primitive of the original
torus-valued cocycle.

This route does not use the unavailable long exact coefficient sequence that
motivated the source question.

## Files

- `main.tex`, `solution_packet.pdf`: full theorem and proof.
- `source_paper.pdf`: official arXiv source paper.
- `figures/open_problem_crop.png`: published Question 10.1.
- `code/make_open_problem_crop.py`: reproducible source crop.
- `code/verify_degree_complex.py`: independent exact bar-sign/winding check.
- `verification.md`: proof, source, build, and novelty audit.

## Scope and review recommendation

This fully answers the isolated cohomology question and gives all degrees for
finite-dimensional tori.  It does not by itself complete the source's broader
program for continuous partial-difference equations or compute the measurable,
locally continuous, Segal--Mitchison, or classifying-space theories.

High-priority expert review is recommended.  The two points to check are the
continuous normalized-complex reduction and the based lifting through the
smash product.  Both are standard, finite-CW arguments; once accepted, the
remaining cocycle and averaging calculation is elementary.
