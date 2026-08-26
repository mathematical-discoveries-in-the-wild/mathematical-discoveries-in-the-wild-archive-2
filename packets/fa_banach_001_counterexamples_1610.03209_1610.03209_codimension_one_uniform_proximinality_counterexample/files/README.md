# A codimension-one counterexample to uniform ball proximinality

Status: candidate full counterexample; likely valid; expert review recommended.

Model: GPT5.6.

Source: Tanmoy Paul, *Various notions of best approximation property in spaces
of Bochner integrable functions*, arXiv:1610.03209v4 (2016), Problem 4.7.

## Result

Problem 4.7 asks whether a uniformly proximinal subspace `Y` of `X` must
have a uniformly proximinal closed unit ball `B_Y` in `X`.  The answer is no,
even if `Y` is required to be proper and codimension one.

The packet gives an explicit Banach space `E = R x ell_2` whose unit ball is
not uniformly proximinal.  It then takes

```text
X = E +_infty R,       Y = E x {0}.
```

The subspace `Y` is uniformly proximinal with the sharp simple modulus
`delta(epsilon,R)=epsilon`, whereas `B_Y` is not uniformly proximinal.

## Proof mechanism

On `E`, use the equivalent norm

```text
N(t,x)=max(|t|+sup_{n>=2}|x_n|/n, ||x||_2).
```

The vector `u=(1,0)` is an extreme point of the unit ball, but the unit vectors
`a_n=(1-1/n,e_n)` satisfy
`N(2u-a_n)=1+2/n` and `N(a_n-u)=1`.  Hence they are arbitrarily good
approximate nearest points to `2u` while staying a fixed distance from its
unique nearest point `u`; this directly violates uniform proximinality.

The `ell_infty` direct-sum geometry makes `Y` uniformly proximinal by radial
movement in its `E` coordinate, and the bad unit-ball configuration embeds
isometrically into `B_Y`.

## Files

- `solution_packet.pdf`: expert-facing proof packet.
- `source_paper.pdf`: arXiv:1610.03209v4.
- `figures/open_problem_crop.png`: readable crop of Problem 4.7 and the
  immediately following background remark.
- `verification_report.md`: proof and novelty audit.

No computation or unproved external theorem is used. Human review should
focus on the extremality calculation and the transfer of the obstruction to
the codimension-one direct sum.
