# 2605.21069 — recurrence does not control the complex property in ell^p for p>2

Status: candidate full counterexample and sharpened positive replacement; likely valid, human review requested.

Model: GPT5.6.

Source: Philipp Bartmann and Matthias Keller, *The complex property of the boundary operator on simplicial complexes*, arXiv:2605.21069v1 (2026), the remark after Theorem 4.1 on source PDF page 9.

## Result

For every `p>2`, recurrence of all link components does **not** imply that the boundary operator has the complex property on `ell^p`. A single weighted augmented half-line works for every such `p`: the edge from `v_(n-1)` to `v_n` has weight `n`, and the edge cochain has value `1/n`. Its weighted `ell^p` norm is `sum n^(1-p)<infinity`, while it carries constant unit flux to infinity. Its boundary is the nonzero endpoint charge, so its boundary of boundary at the empty simplex equals `-1`.

The packet also proves the natural positive replacement. If `q=p/(p-1)` and every component of the relevant link is `q`-parabolic, then the complex property holds on `D(partial partial) intersect ell^p`. The half-line is 2-parabolic but q-hyperbolic for every q<2, showing exactly why recurrence ceases to suffice past p=2.

## Files

- `main.tex`: self-contained expert-facing theorem and proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: PDF reconstructed without mathematical edits from the official arXiv source archive.
- `figures/open_problem_crop.png`: readable full-width crop of the source remark on PDF page 9.
- `verification_report.md`: verification and novelty-search record.

No computational experiment is used in the proof.

## Reviewer focus

Please check:

1. the augmented orientation at the empty simplex and the signs in the endpoint-flux computation;
2. the direct verification that the cochain lies in `D(partial partial)`, not merely in `ell^p`;
3. the localization identity equating the `ell^q` norm of the localized coboundary with link q-energy;
4. whether any literature after the May 2026 source already records this exact counterexample or the q-parabolic replacement.

## Novelty bound

Bounded searches through 11 August 2026 covered all four run indexes, the exact source title and arXiv id, and combinations of `boundary of boundary`, `complex property`, `ell^p`, `p>2`, `weighted half-line`, `unit flux`, and `q-parabolicity`. The nearby background paper arXiv:2507.13696 develops p-parabolicity on weighted graphs but does not discuss this simplicial boundary question. No matching resolution was found. The source itself is only from May 2026, so novelty remains provisional.
