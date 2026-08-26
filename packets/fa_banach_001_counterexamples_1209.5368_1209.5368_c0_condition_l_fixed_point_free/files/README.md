# Fixed-point-free condition-(L) map on a weakly compact convex subset of `c0`

This packet gives a full counterexample to the extension asked about in
Remark 4.8 of arXiv:1209.5368 under three of the source paper's principal
geometric hypotheses.

The construction uses moving triangular tents `u_n` in `c0`, their weakly
compact closed convex hull `K`, and the map that sends each point of `K` to
the successor of its least-index nearest tent.  The packet proves that:

- `T:K -> K` has no fixed point;
- `T` satisfies condition `(L)`, hence property `(*)`;
- directly, every asymptotic center occurring in `(*)` is the whole relative
  invariant set;
- `M(c0)=MW(c0)=2` and `c0` is NUNC.

The uniformly nonsquare subcase is not claimed.

## Files

- `solution_packet.pdf` — promoted, self-contained four-page result.
- `main.tex` — packet source.
- `source_paper.pdf` — official arXiv PDF downloaded from
  `https://arxiv.org/pdf/1209.5368`.
- `source_question_crop.png` — page-14 crop containing Corollary 4.7 and
  Remark 4.8.
- `code/crop_source.py` — deterministic crop recipe.
- `code/verify_tents.py` — independent finite diagnostic checks.
- `VERIFICATION.md` — provenance, build, hash, and visual-QA record.

## Rebuild

From this directory:

```sh
python3 code/crop_source.py
python3 code/verify_tents.py
/Library/TeX/texbin/latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/latex main.tex
```

The mathematical proof is analytic; the Python checker is a finite sanity
check of the explicit tent formulas and inequalities.
