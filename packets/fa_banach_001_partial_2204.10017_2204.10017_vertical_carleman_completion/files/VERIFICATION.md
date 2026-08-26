# Verification

Status: `candidate_partial_likely_valid`

## Mathematical checks

- The scalar pairing `g_eta(t)` has `g_eta^(2m)` in `L2(R)` and
  `||g_eta^(2m)||_2 <= ||eta||_2 ||T^(2m)f||_2` by Cauchy--Schwarz and
  Fubini.
- The constant `||eta||_2^(-1/(2m))` tends to one, so the vertical Carleman
  divergence passes to every nonzero test pairing.
- Vanishing on a product `U x I` makes every derivative of each pairing zero
  at a point of `I`; the one-dimensional Chernoff theorem therefore applies.
- Pairing against all `eta in C_c^infinity(U)` yields `f=0` on `U x R` in
  the distributional and almost-everywhere senses.
- Fubini then gives `f^lambda=0` on `U` for every central frequency where the
  source fiber is defined.  The source's Theorem 1.5 applies with the same
  Hermite decay hypothesis.
- If `e^(a|T|)f in L2`, spectral calculus gives
  `||T^(2m)f||_2 <= (2m/(ae))^(2m)||e^(a|T|)f||_2`; the reciprocal series
  dominates a constant multiple of the harmonic series.

## Novelty/status checks

- Cheap indexes: no hit for arXiv:2204.10017 or the exact open-set question.
- Local parsed arXiv corpus: checked exact title, authors, `Chernoff` with
  `sublaplacian`, and the exact open-set language.
- Web search: arXiv-indexed exact/near-exact searches through 2026-08-11.
- Closest sources checked: arXiv:2009.14230, 2106.02704, and 2011.09940.
- No later full answer was found.  The promoted claim is only the stated
  added-central-Carleman subcase.

## Artifact QA

- Source question crop visually inspected.
- LaTeX compiled with no undefined references.
- Every rendered packet page visually inspected at full-page and detail view.
