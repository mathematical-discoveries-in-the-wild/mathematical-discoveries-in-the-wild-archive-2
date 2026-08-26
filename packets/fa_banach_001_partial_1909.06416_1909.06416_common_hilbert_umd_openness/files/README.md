# 1909.06416: coherent-Hilbert UMD openness

Status: `candidate partial; likely valid`.

## Result

Conjecture 8.9 of Amenta--Uraltsev asks whether an `r`-intermediate UMD
space with `r>2` is always `r_tilde`-intermediate for some `r_tilde<r`.
This packet proves the conjecture for a precise coherent subclass.

If `theta=2/r` and, for one compatible couple `(Z,H)` with `Z` UMD and
`H` Hilbert,

```text
X ≅ [[Z,H]_alpha,H]_theta     (0<alpha<1),
```

then complex reiteration gives

```text
X ≅ [Z,H]_beta,
beta = theta + alpha(1-theta) > theta.
```

Consequently `X` is `r_tilde=2/beta`-intermediate and
`2<r_tilde<r`.

The packet also proves the source's endpoint bilinear-Hilbert consequence for
any triple satisfying `sum 1/r_i=1` when one member with `r_j>2` has such a
coherent representation.  Improving that one exponent makes the reciprocal
sum strictly greater than one and produces a nonempty exponent region for
source Theorem 1.1.

## Scope

This is not a solution of the full UMD openness conjecture.  It makes the
same-Hilbert heuristic in source Remark 8.10 rigorous under the exact
compatibility hypothesis that the remark identifies as missing.  Abstractly
isomorphic Hilbert endpoints cannot simply be substituted into unrelated
compatible couples.

Eight focused upgrade attempts were audited in the attempt note.  Direct sums,
graphs, pushouts, type/cotype margins, lattice factorization, endpoint limits,
and the source's tensor-BHT counterexample did not remove that general
compatibility obstruction.

## Packet contents

- `main.tex`: theorem, proof, endpoint-BHT corollary, stress checks, and scope.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: local arXiv:1909.06416 PDF.
- `figures/open_problem_crop.png`: genuine full-width crop of source PDF page 67.
- `code/render_open_problem_crop.py`: reproducible crop generator.
- `VERIFICATION.md`: mathematical, source, rendering, and checksum audit.
- `SHA256SUMS`: hashes of durable packet artifacts.
- `tmp/`: LaTeX and page-render QA intermediates.

Related attempt note:
`runs/fa_banach_001/attempts/1909.06416_common_hilbert_umd_openness.md`.

