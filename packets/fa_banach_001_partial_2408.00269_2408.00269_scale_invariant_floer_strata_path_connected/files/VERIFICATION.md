# Verification report

Status: `candidate_partial_result_likely_valid`

## Mathematical checks

- Checked the statement of Question 1.7 against arXiv PDF page 6.
- Checked the scalar hypothesis carefully: the source question assumes only
  shift invariance, while Proposition 33.1.5 of Kronheimer--Mrowka assumes
  mild spectrum. For the pair \((H_0,H_2)\), the pair weight is \(h^2\), and
  \(h(2n)\le C h(n)\) implies
  \(h(2n)^2\le C^2 h(n)^2\), exactly the required mildness.
- Checked the graph-norm identities for an invertible weak Hessian \(A\):
  \(\|x\|_1\asymp\|Ax\|_0\) on \(H_1\), and
  \(\|x\|_2\asymp\|Ax\|_1\asymp\|A^2x\|_0\) on \(H_2\).
- Checked that equality of positive and negative growth types gives uniform
  two-sided comparability of the matched eigenvalue magnitudes. Squaring or
  not squaring the source convention makes no difference after taking square
  roots of the comparison constants.
- Checked from the preceding two bullets that the sign-preserving eigenbasis
  matching map and its inverse are bounded on \(H_1\) and \(H_2\).
- Checked that the scale-Kuiper path is continuous on \(H_0\) and \(H_2\),
  hence on \(H_1\) by Hilbert-scale interpolation.
- Checked conjugation preserves \(H_0\)-symmetry, Fredholm invertibility on
  both levels, and the signed spectra.
- Checked the eigenvalue interpolation: matched eigenvalues have the same
  sign, so their convex combinations do not cross zero and remain uniformly
  comparable to the endpoint eigenvalues on both graph-norm levels.
- Checked the noninvertible reduction against the source paper's translation
  invariance of \(\mathcal F_h^{ab}\).

No numerical verification is needed; the argument is qualitative.

## External theorem check

The complete text of Kronheimer--Mrowka, Proposition 33.1.5, was inspected in
the cited book PDF. It states contractibility of the pair-unitary group under
the mild-spectrum condition. Its proof is Kuiper's argument with
pair-boundedness; the real orthogonal version used here is the standard real
analogue of the same proof.

## Literature check

A bounded web/arXiv search used the exact title and question wording and the
phrases `Floer Hessian connected`, `scale invariant Floer Hessian`, and
`Question 1.7 Floer Hessians`. The source paper was the only result addressing
this exact connectivity question. A 2026 paper citing it concerns Fredholm
properties of linearized Floer operators, not connectivity. No exact match for
the theorem in this packet was located.

## Rendering check

The packet was compiled with `latexmk -pdf -interaction=nonstopmode
-halt-on-error -outdir=tmp main.tex`. Every output page was rendered at 150
DPI and visually inspected for clipping, overflow, broken formulas, crop
readability, and page transitions.

## Human-review recommendation

Review as a likely valid substantial partial answer. Highest-value checks are
the real-field applicability of the scale-Kuiper proposition and the
\(H_2\)-graph-norm comparison in Lemma 2.
