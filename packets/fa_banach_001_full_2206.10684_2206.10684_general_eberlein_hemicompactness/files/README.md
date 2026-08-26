# General Eberlein--Grothendieck/hemicompactness equivalence

Status: **candidate full solution, likely valid; human review required**.

This packet answers Problem 2.6 of J. Ka̧kol and A. Leiderman,
*When is a locally convex space Eberlein--Grothendieck?*
(arXiv:2206.10684).  The source asks whether, for every Tychonoff space `X`,

`(C_k(X),w) is Eberlein--Grothendieck  <=>  X is hemicompact`.

The source proves the equivalence only for first-countable `X`.  The packet
proves it for arbitrary Tychonoff `X`.

## Main mechanism

The source identifies the EG condition with weak-star sigma-compactness of
`C_k(X)^*` and identifies its elements as compactly supported Radon measures.
The new proof has two steps.

1. The union of the supports of any weak-star compact family of these
   measures is functionally bounded.  Otherwise, support-localized test
   functions in disjoint high level bands combine into one continuous
   function on which a sequence from the compact family is unbounded.
2. EG already forces `X` to be sigma-compact, hence a paracompact `mu`-space,
   so each such support union has compact closure.  For an increasing compact
   cover `(A_n)` of the dual, these closures `(H_n)` are compact.  If they were
   not cofinal, choose a compact `K` and `x_n in K\H_n`.  The positive atomic
   measure `sum 2^{-n} delta_{x_n}` lies in some `A_N`, forcing every `x_n`
   into `H_N`, contrary to `x_n notin H_n` for `n>=N`.

Thus `(H_n)` is cofinal, so `X` is hemicompact.  The converse is the known
metrizable-locally-convex-space implication used by the source.

## Files

- `main.tex` and `solution_packet.pdf`: complete theorem and proof.
- `VERIFICATION.md`: adversarial mathematical and render audit.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: Problem 2.6 and its source context (PDF p. 5).
- Attempt history:
  `runs/fa_banach_001/attempts/2206.10684_general_eberlein_hemicompactness.md`.

## Novelty check

The lightweight run indexes had no earlier packet or attempt for this target.
Bounded exact-title, exact-problem, notation, hemicompactness, and
weak-star-support searches through 2026-08-13 found the source, its conference
presentation, and later citations, but no later explicit resolution.  The
novelty claim remains provisional pending specialist review.

## Human-review recommendation

Prioritize the triangular support-localization lemma and the standard
paracompact `mu`-space step.  Then check that the positive atomic series is a
`C_k(X)`-continuous Radon functional and that monotonicity of the support
envelopes gives the final contradiction.
