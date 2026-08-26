# Partial Result: Vertical Carleman completion of the Heisenberg Ingham gap

- **Source:** Bagchi--Ganguly--Sarkar--Thangavelu, *An analogue of Ingham's theorem on the Heisenberg group*, arXiv:2204.10017.
- **Target:** Remark 4.1, replacing fiberwise open-set vanishing by vanishing of `f` on an open subset of the Heisenberg group.
- **Status:** `candidate_partial_likely_valid`.
- **Model:** `GPT5.6`.

## Result

The open-set conclusion holds if, in addition to the source's sharp
Hermite-only Fourier decay, the central derivative satisfies

```text
sum_m ||T^(2m) f||_2^(-1/(2m)) = infinity.
```

In particular it holds whenever `exp(a|T|)f` belongs to `L2` for some
`a>0`.

The proof first applies the one-dimensional Chernoff theorem to all horizontal
test-function pairings of `f`.  Local vanishing then propagates along the
entire central line, producing a zero cylinder `U x R`.  Every central Fourier
fiber vanishes on `U`, and Theorem 1.5 of the source finishes the argument.

## Scope

This does **not** solve Remark 4.1 in full.  The Hermite-only estimate controls
central frequency only on a square-root scale and does not imply the added
vertical Carleman series.  The general sublaplacian Chernoff theorem remains
the central obstruction.

## Files

- `main.tex` — theorem, proof, proof intuition, and limitations.
- `solution_packet.pdf` — rendered proof packet.
- `source_paper.pdf` — arXiv:2204.10017.
- `figures/open_problem_crop.png` — source Remark 4.1.
- `VERIFICATION.md` — proof and PDF QA record.
