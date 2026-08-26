# Greedy sparse-triple counterexample

This packet gives a finite-dimensional counterexample to the unrestricted
greedy suboptimality estimate asked about at the end of Appendix B of
arXiv:1506.03549.

For a fixed sparse approximation triple with `M=ell_1^5`, `H=ell_2^5`, and
four overlapping coordinate subspaces, the source's greedy algorithm makes
three unique but globally incompatible choices.  Every signal in the triple
is compressible because `3A=R^5`, yet a three-term signal is not recovered in
three steps.  A one-parameter family also gives unbounded positive-denominator
two-step ratios.

## Files

- `solution_packet.pdf` — promoted self-contained three-page proof.
- `main.tex` — packet source.
- `source_paper.pdf` — official arXiv PDF.
- `source_question_crop.png` — exact page-27 question and definitions.
- `code/crop_source.py` — deterministic evidence crop.
- `code/verify_counterexample.py` — exact-rational exhaustive verifier.
- `VERIFICATION.md` — proof, provenance, build, hash, and visual-QA record.

## Rebuild

From this directory:

```sh
python3 code/crop_source.py
python3 code/verify_counterexample.py
/Library/TeX/texbin/latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/latex main.tex
```

The verifier uses rational arithmetic and exhausts all support unions; the
mathematical proof in the packet is independent and exact.
