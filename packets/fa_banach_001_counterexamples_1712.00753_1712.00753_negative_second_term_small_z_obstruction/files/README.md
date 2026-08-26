# Counterexample Packet: Pure Negative Second Term Cannot Hold for All `z>0`

Run: `fa_banach_001`

Source: Asma Hassannezhad and Ari Laptev, *Eigenvalue bounds of mixed
Steklov problems*, arXiv:1712.00753.

Status: `candidate_counterexample_likely_valid`.

## Result

Open Question 1.8 asks whether there is a positive angle-dependent constant
`C(alpha,beta)` for which the mixed Steklov--Dirichlet Riesz mean satisfies a
two-term upper bound with no remainder. Under the all-`z>0` reading used by
the surrounding results, the answer is **no**.

The proposed right side is

```text
z^(n+gamma-2) (C_{n,gamma}|F| z - C(alpha,beta)).
```

It is negative for every sufficiently small positive `z`, whereas the Riesz
mean is always nonnegative. Thus no positive `C(alpha,beta)` can make the
printed inequality hold for all `z>0`.

## Scope limitation

This packet does not refute a repaired eventual-asymptotic question with
`z>=z0`, nor a two-term inequality carrying a positive lower-order remainder.
The source's Theorem 1.7 includes such a positive constant remainder in the
planar right-angle case.

## Files

- `main.tex`, `solution_packet.pdf`: full proof packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: Open Question 1.8 on source page 6.
- `code/verify_sign.py`: elementary numerical sign check.
- `tmp/`: build and render intermediates.

## Human review recommendation

Accept as a complete counterexample to Open Question 1.8 exactly as printed.
If the authors intended only sufficiently large `z`, reclassify this as a
wording/quantifier correction and retain the eventual inequality as open.
