# Verification record

Status: `candidate_counterexample_likely_valid`  
Agent: `agent_lane_03`  
Model: `GPT5.6`  
Date: 2026-08-11

## Mathematical audit

- The exact targets are Conjectures 2.8, 2.9, 3.7, and 3.8 on printed pages
  7--8 and 14--15 of arXiv:2209.12833.
- Each statement explicitly requires the product-Haar diagonal mass to equal
  `|mu(G)|^2/|d|`, not merely to be one term in a maximum.
- On any infinite compact group, normalized Haar measure has no atoms. If a
  singleton had mass `a>0`, finite subsets of arbitrarily large cardinality
  would have mass `N a`, contradicting total mass one.
- Tonelli's identity gives
  `(mu x mu)(Delta)=integral mu({g}) dmu(g)=0`.
- With `d=1` and normalized total mass, every conjecture requires this zero to
  equal `|1|^2/|1|=1`. The contradiction precedes every vector, functional,
  norm, integral-operator, and diagonalizability condition.
- The circle group is a concrete locally compact counterexample. The same
  argument works for every infinite compact group.
- The non-Archimedean side is nonvacuous: `R((t))` with its t-adic absolute
  value satisfies (FU), since the leading coefficients in a finite sum of
  squares over `R` cannot cancel. The p-adic side works over every `Q_p`.
- The structural upgrade is correct: coordinatewise integrability and
  self-normalization make the constant one integrable, so Haar measure is
  finite and the group compact. Positive diagonal mass gives positive
  singleton mass and hence discreteness. A compact discrete group is finite.
- This does not classify the four max-form questions; the packet states that
  limitation explicitly.

## Upgrade audit

The durable attempt note records eight focused routes/upgrades: transfer of the
discrete repeated-vector construction, the diagonal-null observation,
dimension-one reduction, a concrete FU field, every p-adic field, the general
compact obstruction, compactness forced by integrability, and finite-group
necessity. The result therefore goes beyond one example while preserving the
correct scope.

## Reproducible sanity check

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_diagonal_measure.py
```

Output:

```text
normalized finite-group diagonal masses:
  C_2: 1/2
  C_3: 1/3
  C_5: 1/5
  C_10: 1/10
  C_100: 1/100
  C_1000: 1/1000
nonatomic compact-group limit: 0; conjectural d=1 right side: 1
```

The computation is illustrative only; the proof uses exact Haar-measure
identities.

## Literature and duplicate audit

- No exact-ID duplicate appeared in the run registry, solutions, attempts, or
  proof-gap indexes.
- A nearby packet for arXiv:2210.07062 resolves a discrete repeated-vector
  formulation. Its mechanism is distinct from this continuous null-diagonal
  counterexample.
- Exact conjecture-name, arXiv-ID, and correction/counterexample searches
  through 2026-08-11 returned the source and companion discrete papers but no
  later amendment or answer to these four statements.
- This is a bounded novelty check, not an exhaustive priority guarantee.

## Build and visual QA

- The source crops were regenerated from the official 19-page arXiv PDF.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- Final log search found no LaTeX warnings, undefined references, overfull
  boxes, or underfull boxes.
- The final four-page PDF was rendered at 1.8x with PyMuPDF.
- Every final page was visually inspected. Both stitched source excerpts show
  the conjecture labels and exact equalities; no title, text, equation, image,
  reference, or page number is clipped or overlapped.

## SHA-256

- `solution_packet.pdf`:
  `82e170c11445776aab01ad696fe813ff64af22b5cc228c00fb04703d9bab580f`
- `source_paper.pdf`:
  `d05093ea47d5b37a0f397d4bc893a7caacec4f8c79caf09b4dc751f3cd02c640`
- `source_nonarch_crop.png`:
  `8ccdc9a5c64c35e8be6c5e171a422ee12cab15fd62b72b748bc58defef08e8f8`
- `source_padic_crop.png`:
  `ab6679e6b1b1497206dcad76fae5ca9fbc5a24239f4bd603c45b959b73626698`

