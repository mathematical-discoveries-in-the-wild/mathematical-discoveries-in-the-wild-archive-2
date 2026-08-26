# Literal reverse counterexample and canonical repair

Status: `candidate_full_counterexample_and_repair_likely_valid_needs_human_review`

This packet settles the conjecture printed on PDF page 3 of
arXiv:2502.07448.

- Literally, the conjecture is false: its positive-degree coefficient sum
  vanishes on `f=1`, while its weighted spatial norm is strictly positive.
- The canonical modulo-constants repair is fully true. If `S_mu(f)` is the
  source's logarithmically weighted positive-degree coefficient sum and

  ```text
  Q_mu(f) = inf_a integral log^2(e+|x|)|f-a|^2 dmu
            + integral |f'|^2 dmu,
  ```

  then universal constants satisfy

  ```text
  c Q_mu(f) <= S_mu(f) <= C Q_mu(f).
  ```

The new direction is proved in the comparable hyperbolic-secant model. The
Meixner--Pollaczek generating function turns differentiation into a one-sided
Hilbert matrix, controlled by a dyadic near/far argument. Multiplication by
the spatial logarithm is controlled from the Jacobi recurrence using a
self-contained limiting `K`-functional interpolation lemma. Dilation,
bounded-density comparison, and coefficient-tail summation transfer the
result to the symmetric exponential measure. The source theorem supplies the
opposite direction after subtracting a constant.

Contents:

- `solution_packet.pdf`: five-page counterexample and repaired equivalence.
- `source_paper.pdf`: arXiv:2502.07448v1.
- `figures/open_conjecture.png`: exact conjecture on source PDF page 3.
- `code/make_conjecture_crop.py`: reproducible source crop.
- `code/finite_section_probe.py`: non-proof Jacobi/derivative stress test.
- `verification.md`: proof, endpoint, literature, computation, and rendering
  audit.

Rebuild from this directory with:

```bash
pdftoppm -f 3 -l 3 -png -r 180 source_paper.pdf tmp/source_page
conda run --no-capture-output -n sandbox python code/make_conjecture_crop.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

Reproduce the numerical stress test with:

```bash
conda run --no-capture-output -n sandbox python code/finite_section_probe.py \
  --sizes 16 32 64 128 256 --pad 512
```

Final SHA-256:

```text
575e2d9bdbdf6fb717903b64ff9fcd5eec6dd311ebc0de04d26d4b6a76020e59  solution_packet.pdf
6464374cae6f4b731d0052179bc89f1b457d0b33f6f7e7fb8b3d48e017220399  source_paper.pdf
cd8ce25638bddadf7f9681d1e27a9a4f9193d45806fe43835cb08f17c7a2aac5  figures/open_conjecture.png
```
