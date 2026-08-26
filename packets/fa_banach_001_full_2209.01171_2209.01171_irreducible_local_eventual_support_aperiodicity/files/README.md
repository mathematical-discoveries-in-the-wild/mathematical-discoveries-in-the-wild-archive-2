# Irreducible local eventual support growth implies aperiodicity

Status: `candidate_full_proof_likely_valid`

Source: Jochen Gluck, *Aperiodicity of positive operators that increase the
support of functions*, arXiv:2209.01171.

Source location: immediately after Theorem 1.2 on PDF page 2. The paper asks
whether its irreducible local theorem remains true if, for every positive
`f` supported in a fixed positive-measure set `S`, one merely assumes that
some consecutive supports satisfy

```text
supp(T^n f) contains supp(T^(n-1) f),
```

with `n` allowed to depend on `f`.

## Result

The packet gives an affirmative answer. If `Tz=lambda z` with unimodular
`lambda`, positivity, power boundedness, irreducibility, and the KB property
of `L^p` imply that `e=|z|` is a strictly positive fixed vector and that `T'`
has a strictly positive fixed functional. Normalizing the principal ideal of
`e` gives a unital positive map `R` on `L^infinity` and a unitary
`u=z/e` satisfying `Ru=lambda u`.

The unitary is in the multiplicative domain of `R`. Therefore a narrow phase
slice `b(u)` is sent at time `n` into the rotated slice `b(lambda^n u)`.
When `lambda!=1`, the bump `b` can be chosen so that consecutive rotated
slices are disjoint. Intersecting this slice with `S` produces a nonzero
positive `f` supported in `S` whose consecutive iterates always have disjoint,
nonempty supports. Thus no value of `n` can satisfy the proposed inclusion.

## Packet contents

- `main.tex`: complete proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/source_page_02.png`: source theorem and open question.
- `verification.md`: line-by-line proof and scope audit.

Human review recommendation: **review as a full affirmative resolution of
the question after Theorem 1.2**. The key check is the multiplicative-domain
identity on the normalized principal ideal.
