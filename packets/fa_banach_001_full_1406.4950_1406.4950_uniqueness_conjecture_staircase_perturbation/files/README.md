# Candidate full solution: Conjecture 2 of arXiv:1406.4950

**Status:** `candidate_full_solution_likely_valid` (human verification required)

This packet gives an affirmative proof of Conjecture 2 in S. Astashkin,
F. Sukochev, and D. Zanin, *On uniqueness of distribution of a random
variable whose independent copies span a subspace in* \(L_p\), Studia
Mathematica 230 (2015), 41--57, arXiv:1406.4950.

The source criterion says that a decreasing rearrangement \(h=f^*\) generates
the canonical \(\ell_M\)-basis precisely when its two-term Hardy envelope

\[
T_p h(t)=
\left(\frac1t\int_0^t h(s)^p\,ds\right)^{1/p}
+
\left(\frac1t\int_t^1 h(s)^2\,ds\right)^{1/2}
\]

is comparable with \(m(t)=1/M^{-1}(t)\). If \(h\asymp m\) near zero, the
source paper's Theorem 9 already forces strict interior convexity and
concavity indices. Otherwise, this packet constructs a decreasing staircase
\(u\) with \(T_pu\lesssim m\), while \((h+u)/h\) is unbounded on
positive-measure intervals accumulating at zero. Hence \(h+u\) is a second,
non-equivalent generator, contradicting uniqueness.

## Packet contents

- `solution_packet.pdf`: compiled proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: local copy of arXiv:1406.4950.
- `figures/open_problem_crop.png`: page-3 crop containing Conjecture 2.
- `verification.md`: adversarial proof audit, literature-search bounds, and
  reviewer checklist.
- `code/check_staircase_bounds.py`: numerical sanity check for representative
  power Orlicz envelopes. It is supporting evidence, not part of the proof.

## Reproduction

From this packet directory:

```bash
conda run --no-capture-output -n sandbox python code/check_staircase_bounds.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/pdfs main.tex
cp tmp/pdfs/main.pdf solution_packet.pdf
```

## Human-review recommendation

Prioritize expert review of the staircase lemma, especially the arbitrary-\(t\)
head and tail estimates and the positive-measure non-equivalence argument.
Then check that the explicit symmetrization has rearrangement \(h+u\), so that
Proposition 6 of the source paper applies exactly as stated.

