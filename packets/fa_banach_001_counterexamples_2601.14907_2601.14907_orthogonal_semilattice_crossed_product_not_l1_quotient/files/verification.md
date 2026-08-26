# Verification

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2601.14907_orthogonal_semilattice_crossed_product_not_l1_quotient/code/verify_orthogonal_semilattice.py
```

Expected output records `||1_N||_1=N`, `||1_N||_max=1` for the tested finite
truncations and the shrinking sup-norm tail of harmonic truncations.  The
script is only a sanity check.  The exact proof is in `solution_packet.pdf`.

Packet build and QA:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=runs/fa_banach_001/solutions/counterexamples/2601.14907_orthogonal_semilattice_crossed_product_not_l1_quotient/tmp \
  runs/fa_banach_001/solutions/counterexamples/2601.14907_orthogonal_semilattice_crossed_product_not_l1_quotient/main.tex
```

The final PDF is rendered to PNG in `tmp/` and inspected page by page.  Text
extraction is additionally checked for missing glyphs and accidental clipping.

