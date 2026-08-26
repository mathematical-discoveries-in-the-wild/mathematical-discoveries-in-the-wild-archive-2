# Full answers to two multilinear type questions

Status: `candidate_full_result_likely_valid_needs_human_review`

This packet answers both explicit open questions in arXiv:1502.00440v2.

1. If `E` has type `p`, then
   `phi_1 tensor ... tensor phi_n tensor id_E` has every proper type tuple
   whose reciprocal sum is at least `1/p`. The sign lower `p`-estimate
   hypothesis from the question is unnecessary.
2. For every `n>=2` and every `1<=r_i<=2`, coordinatewise multiplication

   ```text
   B: ell_{r_1} times ... times ell_{r_n} -> ell_1
   ```

   belongs to `L(tau_{r_1},...,tau_{r_n})` but has no proper multilinear
   type. This proves the requested noninclusion and also covers the excluded
   endpoint where all `r_i=1`.

The first proof is the type-`p` inequality followed by monotonicity from
`ell_p` to `ell_s` and generalized Holder, where `1/s` is the reciprocal
sum of the requested tuple. The second uses generalized Holder to bound the
coordinate product and tests it on the common diagonal basis, where its
`Rad(ell_1)` norm is exactly `k`.

Contents:

- `solution_packet.pdf`: four-page proof, scope audit, and source excerpts.
- `source_paper.pdf`: arXiv:1502.00440v2.
- `figures/question_1.png` and `figures/question_2.png`: exact source
  questions on PDF pages 9 and 12.
- `code/make_question_crops.py`: reproducible source-crop script.
- `verification.md`: mathematical, endpoint, literature, and rendering
  audit.

Rebuild from this directory with:

```bash
conda run --no-capture-output -n sandbox python code/make_question_crops.py
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

Final SHA-256:

```text
0dee0ee97e62135fc8ac23ca1d7d7a1bbb51f48f52861c745e9c1faf50302e97  solution_packet.pdf
e564ec280aadf21ce979c281737d028b785cdb0c8aafc3833ed100b97c0c1552  source_paper.pdf
cd376a6f360d72b80b2d4b00dbfdb223a4ae3804fa5a0a5dff18dc5b772ff457  figures/question_1.png
4b0cff11f4a7393fb1cacfd6de1e3a20842dc9b5d6033ebe49f21abca3db20e0  figures/question_2.png
```
