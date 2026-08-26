# Verification

Run the finite atomic sanity check from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1912.01162_subhomogeneous_noncommutative_marcinkiewicz_grothendieck/code/check_matrix_corner_norms.py
```

For each tested matrix field it checks
`max corner norm <= whole norm <= sum of corner norms` and exact entrywise
reconstruction.  The script is not part of the proof.

Build the packet from its directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
```

The final PDF is rendered to PNG under `tmp/`, visually inspected page by
page, and checked by layout-preserving text extraction.

