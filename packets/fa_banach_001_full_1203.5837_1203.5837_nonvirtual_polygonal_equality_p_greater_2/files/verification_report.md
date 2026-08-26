# Verification report

## Mathematical checks

- Confirmed the exact open question on source PDF page 17: source Lemma 4.5
  makes virtual degeneracy sufficient for `p>2`, and the authors say they do
  not know whether it is necessary.
- Checked the weight normalization `1/2+1/2=1` and that all weights are
  strictly positive.
- Checked positivity of the scale: for every `p>2`,
  `2^(p-2)-1>0` and `2^(p-1)+1/4>0`.
- Checked that `x_1=(-1,0)`, `x_2=(1,c)`, and `y_1=(0,2c)` are pairwise
  distinct for `c>0`, so the signed simplex is completely refined and cannot
  be a trivial equality.
- Expanded all three distances independently:
  `||x_1-y_1||_p^p=1+2^p c^p`,
  `||x_2-y_1||_p^p=1+c^p`, and
  `||x_1-x_2||_p^p=2^p+c^p`.
- Substitution gives the exact gap
  `1-2^(p-2)+(2^(p-1)+1/4)c^p=0`; no limiting or numerical argument is used.
- Numerically checked the original weighted equality at
  `p=2.0001, 2.1, 3, 4, 10`; residuals agree with zero to floating-point
  precision.
- Checked non-virtuality directly from coordinate 1: the scalar weights at
  `-1`, `0`, and `1` do not match across the two sides.
- Checked an independent obstruction using source Lemma 4.4: the left
  weighted barycenter is `(0,c/2)`, while the right weighted barycenter is
  `(0,2c)`.  Since virtual degeneracy implies balance, the simplex cannot be
  virtually degenerate.
- Checked endpoint consistency.  The negative scalar gap is strictly negative
  exactly for `p>2`; this does not contradict the source's necessity theorem
  for `0<p<2` or its separate Hilbert-space discussion at `p=2`.

## Literature and novelty checks

- Cheap run indexes contained no prior result for arXiv:1203.5837 or this
  necessity question.
- Exact-phrase and citation searches found no later paper stating necessity or
  a counterexample to it.
- Inspected the full arXiv:2404.06658 PDF.  It explicitly settles the source's
  separate Schatten-class existence question and proves a general equality-
  existence criterion, but does not mention virtual degeneracy.  The packet's
  explicit non-virtual equality is not claimed there.
- Novelty is therefore assessed as moderate rather than certain; the formula
  should receive human literature review before external dissemination.

## Artifact checks

- `main.tex` compiled under `latexmk -halt-on-error`.
- The final LaTeX log contains no undefined references, multiply defined
  labels, overfull boxes, LaTeX errors, emergency stops, or fatal errors.
- `solution_packet.pdf` has 2 pages with extractable text.
- Both packet pages were rendered at 1.8x and visually inspected; all formulas,
  exponents, fractions, and page breaks are legible with no clipping.
- `source_paper.pdf` has 18 pages and
  `supporting_literature_2404.06658.pdf` has 7 pages.
- `figures/open_question_crop.png` contains the full necessity sentence and
  was rendered at 2.2x and visually inspected.
- The result ledger parses as valid JSON and uses model `GPT5.6`.
