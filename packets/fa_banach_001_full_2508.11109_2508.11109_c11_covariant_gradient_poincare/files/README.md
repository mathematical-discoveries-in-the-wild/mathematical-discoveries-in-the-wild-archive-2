# C1,1 covariant-gradient Poincare theorem

Status: `candidate_full_result_likely_valid_needs_human_review`

This packet gives a full affirmative answer to the explicit question after
Lemma 3.2 of arXiv:2508.11109. On every compact connected embedded
`C^{1,1}` hypersurface of intrinsic dimension `d>=2`, and for every
`1<p<infinity`, the covariant gradient is injective on tangential `W^{1,p}`
fields and satisfies

```text
||v||_{W^{1,p}} <= C ||nabla_Gamma v||_{L^p}.
```

The new replacement for the source's `C^2` curvature-continuity argument is:

1. the Lipschitz outward Gauss map is onto;
2. its area formula forces `det B != 0` on a positive-measure set;
3. a weakly parallel field bootstraps to `W^{1,infinity}`;
4. the distributional Gauss equation forces it to vanish wherever `B` is
   invertible;
5. its length is constant, so it vanishes everywhere.

The theorem immediately lowers the weak `L^2` Bochner--Laplace theory to
`C^{1,1}`. The packet also audits why the source's weak `W^{1,p}` Bochner
proof uses only `nu in W^{1,infinity}` and `B in L^infinity` after this
geometric step. It does not lower any separately stated higher-order
`C^{m+2,1}` hypotheses.

Contents:

- `solution_packet.pdf`: four-page proof and scope/novelty audit.
- `source_paper.pdf`: arXiv:2508.11109v3.
- `figures/open_question_and_poincare.png`: exact source question and Theorem
  3.3 on PDF page 14.
- `code/make_open_question_crop.py`: reproducible crop script.
- `verification.md`: mathematical, literature, and rendering audit.

Rebuild from this directory with:

```bash
conda run --no-capture-output -n sandbox python code/make_open_question_crop.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

Final SHA-256:

```text
d66ce6fc82c9cd98345ced42efdf44e3d5a8b74e003378323568252e1fabaca6  solution_packet.pdf
bb26414eab54c889a4a4b1b0d102cf8e951ac7f64e2629afbe2b3a640f11fa7d  source_paper.pdf
```
