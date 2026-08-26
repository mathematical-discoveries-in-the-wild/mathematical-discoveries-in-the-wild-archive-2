# Verification record

## Source identification

- Target: arXiv:2209.13576, *Metrical almost periodicity: Levitan and
  Bebutov concepts*.
- Problem: source PDF page 13, immediately after the specialization in
  Section 2.1.
- Definitions checked in the extracted TeX at Definition 2.3(i)--(ii) and
  the specialization at source lines 497--506.
- `source_paper.pdf` was downloaded from the official arXiv PDF endpoint.
- PDF page 13 was rendered at 180 dpi and the problem excerpt was visually
  checked before cropping to `figures/source_problem.png`.

## Proof audit

- For Levitan recurrence, fixed one `a`-almost period on `K`, applied
  `b`-recurrence to the shifted compact `K + sigma`, and checked the exact
  inclusion `sigma + E_b(K + sigma, delta) subset E_ab(K, epsilon)`.
- Relative density is preserved by translation.
- For Poisson recurrence, used a diagonal selection because Definition
  2.3(ii) permits the recurrence sequence to depend on the compact set.
- Required `|tau_j| > j + |sigma_j|`; hence the sums have norm greater than
  `j` even if the two selected translations nearly cancel.
- Used error `1/[j(1+|b|)]` in both stages, which yields total error at most
  `1/j`.
- Induction with multipliers `c^m` and `c` establishes every positive power.
- No boundedness or continuity hypothesis enters the argument.

## Novelty screen

On 2026-08-12, checked the run registry, solution, attempt, and proof-gap
indexes; exact title and exact problem wording; citations to the source; and
targeted searches combining `Levitan (N,c)`, `c^2`, `uniformly c-Poisson
stable`, and power closure. No later claimed resolution was found. This was
a bounded search and does not certify exhaustive coverage of non-arXiv
literature.

## Packet QA

The packet was compiled with `latexmk -pdf -interaction=nonstopmode
-halt-on-error`. The build log was checked for LaTeX warnings and box
diagnostics. Every output page was rendered to PNG and inspected for clipping,
overlap, illegible mathematics, and malformed source imagery.
