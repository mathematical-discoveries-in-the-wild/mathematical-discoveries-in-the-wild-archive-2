# Component propagation for the sun-dual resolvent inclusion

Status: `candidate_partial_result_likely_valid_needs_human_review`

Source: Karsten Kruse and Felix L. Schwenninger, *Sun dual theory for
bi-continuous semigroups*, arXiv:2203.12765. The target is the second open
question following Proposition 4.8.

## Result

For the setting and notation of the source paper, let

\[
\Omega=\{\lambda\in\rho(A):
R(\lambda,A)^\bullet X^\bullet\subset D(A^\bullet)\}.
\]

Then \(\Omega\) is both relatively open and relatively closed in \(\rho(A)\).
Consequently it is a union of connected components of \(\rho(A)\), and it
contains the component containing the right half-plane
\(\operatorname{Re}\lambda>\omega_0(T)\). In particular, the source question
has an affirmative answer whenever \(\rho(A)\) is connected.

Thus any failure of the full-resolvent inclusion must occur in a connected
component of \(\rho(A)\) disjoint from the right half-plane. The result does
not seed such a component and does not settle the separate question about
whether mixed-topology continuity is necessary.

## Files

- `main.tex` / `solution_packet.pdf`: self-contained statement, proof,
  upgrade audit, and limitations.
- `source_paper.pdf`: the source arXiv PDF.
- `figures/open_questions_crop.png`: source page 18 showing both open
  questions.
- `VERIFICATION.md`: line-by-line proof-obligation and scope audit.

## Reproduction

From this directory, compile with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

The final PDF was rendered to RGB PNG images and every page was visually
inspected.

