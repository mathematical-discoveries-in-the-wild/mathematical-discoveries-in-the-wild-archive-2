# Exact simplex-section minimum for all two-level normals

Status: `partial_result_likely_valid`

Source: Colin Tang, *Simplex slicing: an asymptotically-sharp lower
bound*, arXiv:2403.13224. The target is Question 16 on source PDF page
17: is the central section parallel to a facet exactly minimal?

## Result

Let `a` be a unit vector in `R^(n+1)` with coordinate sum zero. Suppose
`a` has exactly two coordinate values. After a permutation and possibly
changing sign,

```text
a = (alpha,...,alpha,-beta,...,-beta),
```

with `k` copies of `alpha`, `m=n+1-k` copies of `-beta`, and
`1 <= k <= m`. The density at zero in Webb's probabilistic formula is

```text
D(k,m) = binom(k+m-2,k-1)
         k^(k-1/2) m^(m-1/2) / (k+m)^(k+m-3/2).
```

For fixed `k+m`, this is strictly increasing for
`1 <= k <= floor((k+m)/2)`. Consequently, the facet direction (`k=1`,
or equivalently `m=1`) is the unique minimum among all two-level
central normals, up to permutation and sign. In particular, Tang's
conjectured sharp lower bound holds exactly throughout this family in
every dimension.

The key quotient is

```text
D(k+1,m-1)/D(k,m)
  = A(k)/A(m-1),
A(x) = (1+1/x)^(x+1/2),
```

and `A` is strictly decreasing on `(0,infinity)`.

## Scope

This does **not** settle Question 16 for arbitrary normals with three or
more coordinate values. Dirksen already proved the whole one-positive
coordinate chamber and dimensions at most four. His balancing result
reduces a general sign chamber to equal negative coordinates, but the
remaining positive coordinates need not be equal; his Remark 3.4 and
Lemma 3.6 also show that naive two-level minimization within every sign
chamber is false in higher dimension.

## Files

- `solution_packet.pdf`: expert-facing statement and proof.
- `source_paper.pdf`: locally compiled arXiv source paper.
- `figures/open_problem_crop.png`: Question 16 from source PDF page 17.
- `code/verify_two_level.py`: independent numerical checks of the density
  formula and monotonicity ratios (evidence only; the proof is analytic).
- `verification.md`: build and mathematical verification record.

## Novelty check

A bounded search on 2026-08-11 covered the run indexes, exact arXiv-id and
keyword queries, Tang's cited Dirksen paper arXiv:1509.06408, the later
arXiv:2505.00944, and arXiv:2606.07163. Dirksen treats two-level-looking
vectors while analyzing sign chambers, but no statement comparing every
two-level multiplicity and proving the facet is the unique minimum of this
entire family was located. The latter two papers concern maximum-section
or reverse-Holder questions, not this exact minimum. Novelty confidence is
moderate rather than high because the Gamma computation is short and may
be folklore.

## Human review recommendation

Review as a likely valid substantial partial result. Check the scaling in
the Gamma-density integral, the simplification of `D(k,m)`, and the ratio
monotonicity. Do not label it a full solution of Question 16.

