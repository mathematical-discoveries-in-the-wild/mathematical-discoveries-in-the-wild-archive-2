# Verification report

## Mathematical audit

- The construction uses pairwise disjoint supports
  `B(p_n,2 rho_n)`, with `p_n=2^{-n-4} e_1` and
  `rho_n=|p_n|^2/100`.  The exact consecutive-ball inequality is checked by
  the verifier; nonconsecutive balls are farther apart.
- The glued value is a convex combination of two strictly positive
  functions away from the origin.  On the inner ball it is exactly
  `a_n(L+tau_n)` after rescaling.
- Cutoff derivatives cost powers of `rho_n^{-1}`.  Both
  `a_n=exp(-rho_n^{-2})` and the background derivatives on the support are
  smaller than every power of `|p_n|`, so all glued derivatives tend to zero
  faster than every power at the origin.
- Any square component is bounded by `sqrt(f)` and is therefore flat at the
  origin.  In particular its value and gradient vanish there.  The gradient,
  Hessian, and Hessian-Hoelder rescaling losses are respectively bounded by
  `rho_n |p_n|/sqrt(a_n)`, `rho_n^2/sqrt(a_n)`, and
  `rho_n^{2+alpha}/sqrt(a_n)` up to fixed constants.
- The source's Lemma 5.2 has a hardness lower bound tending to infinity as
  `tau` tends to zero for each fixed number of squares and each fixed
  modulus.  Since only finitely many pairs are imposed at stage `n`, the
  diagonal choice of `tau_n` is valid despite the absence of a quantitative
  rate.
- Dividing the lower and upper norm bounds by the positive rescaling factor
  gives `n^2 <= C` for all sufficiently large `n`, the required
  contradiction.

Run the supporting verifier with:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2107.12840_flat_R4_regular_sos_counterexample/code/verify_geometry_and_scaling.py
```

The script is a check of exact geometry and chain-rule factors plus sampled
flatness envelopes; it is not a substitute for the analytic proof.

## Source and scope audit

- Source PDF page 5 defines regular, flat, and elliptical functions, states
  the counterexample theorem for `n >= 5`, and identifies dimensions 2, 3,
  and 4 as the remaining range for the weaker-monotonicity question.
- Source PDF page 32 states Lemma 5.2, the precise hard-quartic compactness
  estimate used in the proof.
- The new theorem imposes no monotonicity condition.  It therefore promotes
  the unconstrained counterexample to dimension four, but does not answer
  source Remark 2.7 about prescribed weaker monotonicity assumptions.
- The choice of `tau_n` is nonconstructive but rigorous: it invokes only the
  divergence asserted by Lemma 5.2 for finitely many constraints at each
  stage.

## Novelty check

On 2026-08-17 the run registry, solution, attempt, and proof-gap indexes were
searched for arXiv:2107.12840 and the core terms.  No duplicate result was
found.  Bounded searches for later work on regularity-preserving sums of
squares found Korobenko--Sawyer's published paper and Sullivan MacDonald's
arXiv:2303.07998, which gives other polynomial nondecomposability results,
but no flat elliptical four-dimensional construction matching the theorem
here.  Novelty is plausible, not certified.

## Packet QA

- Local source files and rendered evidence from PDF pages 5 and 32 are
  included.
- The final PDF was compiled from `main.tex`; the LaTeX log has no box,
  reference, or layout warnings, and every rendered page was visually
  inspected.
- Final PDF: 5 A4 pages.
- SHA-256 `solution_packet.pdf`:
  `fbac236d7f885c232c268ca6732608fa037bd32d1eabeff048af18d8ef1d5dda`.
- SHA-256 `source_paper.pdf`:
  `1a5b904420eff7cdb04c16b27241a8dfa52ec049f4d508d4aaf85e523780534f`.
- SHA-256 `figures/source_page_5.png`:
  `0ed78172ea034b736fd0addf8510fc7b2c6e8db2ecb94dddc4ec4889f4b5ae06`.
- SHA-256 `figures/source_page_32.png`:
  `16a4c33ac43ff69d1d411335fdd3eee1b2ad48c9af6caa2d5f9c58d4cdbdb740`.
- SHA-256 `code/verify_geometry_and_scaling.py`:
  `dc78a0a5a149c8165d304e3f5ee1c5c0bf3ea02f88d905a202fa5d0d62ba9672`.

