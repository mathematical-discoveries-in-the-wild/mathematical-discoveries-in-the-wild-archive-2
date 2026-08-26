# Verification report

Status: candidate_counterexample_likely_valid

## Mathematical checks

- Checked the exact Section 4.2 statement on PDF page 12 of arXiv:1810.05714.
- Checked that {1,q}, q(t)=t, is locally linearly independent in L0([0,1]):
  every level set of q has Lebesgue measure zero.
- Checked Sections 1.1-1.2 of arXiv:0712.2378 for existence, local finite
  representation, uniqueness of local coefficients, and the characterization
  of band-preserving maps by commutation with band projections.
- Checked that permuting two elements of a local Hamel basis produces a
  well-defined linear involution commuting with every band projection.
- Checked completeness and the exact rectangular identity after transporting
  the L2 norm.
- Checked the discontinuity argument using simple approximations to q:
  U(s_n)=q s_n tends to q^2, while continuity would force convergence to
  U(q)=1.
- Checked that a fixed convergence-in-measure neighborhood missed by a
  norm-null sequence rules out almost-everywhere convergence of every
  subsequence.

No numerical computation is needed; all assertions are exact.

## Literature check

Searched the run indexes, the exact source sentence, the exact title and arXiv
id, and combinations of rectangular function space, subsequence property, and
band preserving.  The searches found the source and the older Wickstead
machinery, but no later stated answer to the 2018 question.  This is a bounded
novelty check.

## Rendering check

Compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.  The
final six-page PDF was rendered at 150 DPI with the bundled Poppler runtime,
and every rendered page was visually inspected after the final source-image
crop.  The proof, source evidence, and references are readable and unclipped;
the final LaTeX log contains no overfull, underfull, or warning diagnostics.

## Human-review recommendation

Review as a likely valid full counterexample.  Audit the local-Hamel-basis
coordinate permutation carefully.  Once that involution is accepted, the
transported norm and the failure of the subsequence property are elementary.
