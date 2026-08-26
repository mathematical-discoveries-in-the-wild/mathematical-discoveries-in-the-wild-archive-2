# Periodic-jet monodromy counterexample

Status: `candidate_full_counterexample_likely_valid_needs_human_review`

Source conjecture: Kevin O'Neill, *A Whitney Extension Problem for
Manifolds*, arXiv:2310.13115, the sentence immediately after Theorem 3.5
(source PDF page 15).

## Result

The conjecture that O'Neill's M-bundle section theorem extends from `m=1` to
all `m>=2` is false. For every integer `m>=4`, the packet constructs a
nontrivial, Glaeser-stable, proper, consistent M-bundle over the unit circle
in `R^3`. Its Grassmannian bundle is the constant singleton horizontal plane,
but it has no manifold section.

In horizontal tubular coordinates `(theta,sigma)`, the allowed local height
jets are those of

```text
(b + theta - t) sigma^(m-1)/(m-1)! + c sigma^m/m!.
```

Every allowed jet extends over a short arc, so all Glaeser tests pass. A
global section, however, would define a periodic coefficient
`b(t)=partial_sigma^(m-1)F(t,0)` satisfying `b'(t)=1`, which is impossible.

The technical point is that coordinate realization must preserve affine
fixed-Q fibers. Because all nonlinear terms below degree `m-1` vanish, the
first nonlinear interaction has degree `2m-3>m`; hence graph-coordinate
changes are affine-linear through the retained order.

## Files

- `main.tex` / `solution_packet.pdf`: self-contained construction and proof.
- `source_paper.pdf`: the 37-page source arXiv PDF.
- `figures/source_conjecture.png`: source page 15 with Theorem 3.5 and the
  conjecture.
- `VERIFICATION.md`: proof audit, scope, and human-review focus.
- `code/check_periodic_jet.py`: exact symbolic coordinate-change and local
  derivative audit.
- `code/render_source_evidence.py`: reproducible source crop.
- `code/render_solution_pdf.py`: RGB rendering of every final packet page.

## Reproduction

Run the exact audit:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2310.13115_mge4_mbundle_section_counterexample/code/check_periodic_jet.py
```

Compile from the packet directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/pdfs main.tex
```

The final PDF is rendered to RGB PNGs, and every page is visually inspected
before promotion.
