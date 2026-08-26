# Verification

## Mathematical audit

- **Block decomposition:** For a finite direct sum, conjugation by all block
  sign matrices decomposes the domain and range of `Df` into the diagonal
  character and one distinct character for each unordered block pair.  Direct
  sum differentiation identifies the diagonal restriction with the summand
  derivatives.  After a block permutation, a pair-character restriction is
  exactly the off-diagonal restriction at the corresponding two-summand point.
- **Pairwise criterion:** An invertible two-summand derivative is block diagonal
  across its diagonal/off-diagonal characters, so its off-diagonal restriction
  is invertible.  Hence regular summands plus pairwise compatibility make every
  restriction at the full direct sum invertible.
- **Induction:** The forced set `C_n` is a finite union of continuous images of
  compact products (the compositions of `n`, earlier compact closures, and the
  compact orthogonal/unitary group).  The regular and compatibility loci are
  invariant open sets containing `C_n`, `C_n x C_n`, and each
  `C_n x closure(B_i)`.  A sufficiently small distance tube around `C_n` has
  compact closure inside all these conditions.  The tube is group invariant
  because the norm and `C_n` are invariant.
- **Free domain:** Since each `B_n` contains all earlier direct sums of total
  size `n`, their disjoint union is closed under direct sums.  It is finitely
  open and compact-group invariant.  In the GL cases, its full similarity
  envelope is a union of open linear images, remains in the original GL-free
  domain, is closed under direct sums, and preserves derivative invertibility.
- **Inverse:** The standard two-point block derivative identity turns any
  collision into a nonzero kernel vector, so `f` is injective.  The ordinary
  finite-dimensional inverse theorem makes each image level open and the
  inverse levelwise `C^r`; uniqueness gives direct-sum and conjugation laws.

## Literature boundary

The source's uniformly-open theorem and arXiv:1502.05254 require uniform/cb
control.  Pascoe's fine theorem assumes derivative nonsingularity on an entire
nc domain.  Exact-phrase, citation, nc-germ, and fine-topology searches through
2026-08-12 found no explicit later resolution of the exact question.

## Artifact checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully after the final edit.
- The final log contains no undefined references, overfull boxes, or LaTeX
  warnings.
- `pdftotext` extraction contains all theorem, proof, and reference sections.
- All four rendered pages were inspected at 130 dpi; no clipping, collision,
  illegible text, or malformed formula remains.
- `SHA-256(solution_packet.pdf) =
  db8b1b66b602145ba898f9cda2740d03403f11de6fc1b4e07f58ed0f23024e76`.

## Human-review recommendation

Check the pair-character decomposition in Lemma 2 and the quantifiers in the
distance-tube induction.  Those are the only nonstandard ingredients; the GL
similarity-envelope and final inverse-theorem steps are routine once the
regular free neighborhood exists.
