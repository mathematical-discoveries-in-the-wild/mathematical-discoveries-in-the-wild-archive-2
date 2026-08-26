# arXiv:1703.02792 — complete `K_p+K_q` classification

Status: `candidate_full_solution_likely_valid`

This packet answers Question 3.10(ii) of Anand and Chavan, *On sum of two
subnormal kernels* (arXiv:1703.02792).

For `m=min(p,q)`, `M=max(p,q)`, and `r=M-m`, multiplication by `z` on
`H(K_p+K_q)` is subnormal exactly when:

- `r=0`;
- `0<r<=1`; or
- `1<r<=2` and `M>=phi(r)`, where `phi` is the standard zero-free phase
  boundary for `E_{r,beta}(-x)`.

It is never subnormal for `r>2`. At `r=2`, `phi(2)=3`, so the criterion is
`m>=1`, recovering the exact theorem already proved in the source.

The new bridge is a bounded-analytic uniqueness argument: if the integer
sequence `1/((k+1)^m+(k+1)^M)` is a Hausdorff moment sequence, its representing
measure forces the entire shifted interpolation. Its unique inverse Laplace
density is

`t^(M-1) E_{r,M}(-t^r)`.

Thus subnormality is equivalent to nonnegativity of this density. The middle
regime is exactly the published Mittag–Leffler zero-free phase boundary, and
for `r>2` the dominant conjugate poles force infinitely many sign changes.

Files:

- `main.tex`: full theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: printed source page 12 with Question 3.10(ii).
- `code/check_classification.py`: high-precision special-function sanity check.
- `verification.md`: proof audit, novelty record, and review focus.

The special-function phase curve is established prior literature and is not
claimed as new. Bounded searches on 2026-08-11 found no later paper connecting
it to Question 3.10(ii) or giving this operator classification.
