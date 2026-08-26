# Banach-space well-separating common complements

Status: `candidate_full_proof_likely_valid`

Source: Florian Noethen, *Well-separating common complements of a sequence of
subspaces of the same codimension in a Hilbert space are generic*,
arXiv:1906.08514.

Source locations:

- Conjecture 3.4, source PDF page 5: existence in arbitrary real Banach spaces.
- Conjecture 3.15, source PDF page 11: prevalence in arbitrary real Banach
  spaces.
- The source says Conjecture 3.4 follows from a Banach version of Lemma 3.6,
  and Proposition 3.20 says existence implies prevalence.

## Result

This packet proves both conjectures. Its quantitative core is stronger than
the missing lemma: for every sequence `(phi_j)` of norm-one functionals on an
arbitrary real Banach space, there is a unit vector `x` and an absolute
constant `C` such that

```text
|phi_j(x)| >= exp(-C (log(j+1))^2)  for all j.
```

The proof has two steps. First, quotient by the common kernel of any `N`
functionals and put the finite-dimensional quotient in John position. A
translated Euclidean-slab estimate gives, around every base point and within
every radius `r`, a perturbation satisfying all `N` lower bounds at scale
`r/(8N^2)`. Second, apply this lemma to dyadic initial batches with summable
perturbation radii. Later corrections are less than one quarter of every
earlier margin, while the accumulated margin loss is only quadratic in the
logarithm of the index.

For codimension one this produces a well-separating common complement. The
source's Banach-space induction propagates it to every finite codimension, and
its Proposition 3.20 upgrades existence to prevalence.

## Packet contents

- `main.tex`: complete proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/source_page_05.png`: source existence conjecture page.
- `figures/source_page_11.png`: source prevalence conjecture page.
- `verification.md`: constant, tail, scope, and literature audit.

Human review recommendation: **review as a full proof of Conjectures 3.4 and
3.15**. The key checks are the translated slab probability in Lemma 1 and the
tail estimate in Theorem 2.
