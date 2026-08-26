# Verification report

Verdict: `candidate_full_negative_answer_likely_valid`

## Source audit

The locally compiled source PDF is arXiv:2209.05619, An--He--Lai,
*Classification of spectral self-similar measures with four-digit elements*.
Example 5.2 on source page 23 considers `D={0,1,3,5,6}`, records that every
mask-zero phase is irrational, and says the authors believe none of the
measures `mu_(rho,D)` is spectral. The paper does not subsequently answer the
example.

## Fourier-zero audit

For fixed frequency, the mask-product tail differs summably from 1. Thus the
infinite product vanishes exactly when a factor vanishes, giving
`Z(mu_hat)=union q^k(theta+Z)`. Orthogonality puts every nonzero frequency
difference in this zero set. Coloring a pair by one of finitely many phases is
therefore legitimate, and infinite Ramsey supplies a monochromatic infinite
subfamily.

## Transcendence audit

For a mask-zero phase `theta`, `z=exp(-2 pi i theta)` is algebraic. If the
source's irrational `theta` were algebraic, Gelfond--Schneider applied to
`(-1)^(-2 theta)` would make `z` transcendental. Hence all phases are
transcendental.

## Algebraic-contraction audit

For algebraic `q`, a difference identity has the form `a theta+b=0` with
algebraic `a,b`, so both vanish. This yields pairwise power-difference
identities. Along an increasing monochromatic sequence the scale exponents
strictly increase. After division by the larger power, the left side tends to
1 from below while the right side is at most `q^(-1)`, a contradiction.

## Transcendental-contraction audit

One triple gives `theta=R(q)`. The coefficient denominator cannot vanish at
transcendental `q`, and `R` is nonconstant because `theta` is irrational.
Evaluation at transcendental `q` is injective on `Q(X)`, so every later
difference relation lifts to the rational-function field.

The formal clique lemma was checked case by case at infinity:

- a pole of `R` makes degree equal to level plus a fixed positive order;
- at a finite limit, normal integer translates have degree equal to level;
- only the translate cancelling a rational integer limit is exceptional, and
  three exceptional scale relations would make a ratio of distinct binomials
  constant.

Every possible infinite subsequence contradicts one of these degree facts.

## Computational sanity check

`code/sanity_checks.py` confirms the mask-polynomial structure and searches
bounded formal examples for unexpectedly large cliques. It found no clique
larger than three in the tested window. This is only a regression/sanity check;
the theorem is proved symbolically for all parameters.

## Novelty and scope audit

Bounded local-index, exact-digit-set, exact-sentence, title/citation, and close
web searches on 2026-08-11 found no later answer to Example 5.2 and no matching
general irrational-mask obstruction. The result settles the explicit example
for every contraction and generalizes to masks having no rational zero phase.
It does not settle mixed rational/irrational masks or the entire modified
Laba--Wang conjecture.

## Render audit

The final packet compiled without LaTeX warnings, overfull boxes, or
underfull boxes. All five pages were rendered to PNG and inspected at full
resolution on 2026-08-11: the source-problem crop is legible, mathematical
displays are unclipped, and no overlap, overflow, or missing glyphs were
found. SHA-256 of the inspected PDF:
`582847bb90d2f8b40854ef12406ace827ebd6c36ab59939cc96918fe2f46201f`.

## Human verifier focus

1. Check the exceptional finite-limit case in the formal clique lemma.
2. Check that numerical identities at transcendental `q` lift to `Q(X)`.
3. Recheck exactness of the infinite-product zero set.
