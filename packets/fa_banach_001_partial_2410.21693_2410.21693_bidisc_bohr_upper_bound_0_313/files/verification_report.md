# Verification report

Status: `candidate_partial_likely_valid`

## Mathematical checks

- The source definition and open-status statement were checked in
  arXiv:2410.21693v3, PDF pages 1 and 4.
- The identity
  `|p|^2-|p_tilde|^2 = x(1-|w|^2)|1-z|^2 + (1-x)(1-|z|^2)|1-w|^2`
  was independently expanded symbolically; the residual is exactly zero.
- The identity proves denominator stability and the Schur/rational-inner
  hypothesis without invoking an external rational-inner theorem.
- The disk-automorphism step preserves the Schur class and supremum norm one.
- The relation `F=a-(1-a^2)Q` was checked algebraically.
- Every coefficient through total degree eight was checked against the exact
  denominator recurrence.
- The final finite subsum is strictly greater than one, so omitted terms can
  only strengthen the violation.
- Strictness and continuity produce failure at some radius below `313/1000`,
  which justifies the strict conclusion `K_2 < 313/1000`.

## Exact computational checks

- Runtime: Python standard library `fractions.Fraction`; no floating point is
  used by the verifier.
- Parameters: `x=1/6`, `a=999/1000`, `r=313/1000`.
- Coefficients checked: all 44 nonconstant bivariate coefficients with total
  degree at most eight.
- All eight displayed homogeneous layer norms were reproduced exactly.
- The weighted resolvent subsum was reproduced exactly and shown to exceed
  `1/(1+a)=1000/1999`.
- The finite Bohr-mass margin is exactly
  `187683844396959398701315353549825634829908046335607 /
  839808000000000000000000000000000000000000000000000000000`,
  which is positive.
- Command:
  `conda run --no-capture-output -n sandbox python code/verify_certificate.py`
- Result: `PASS: exact finite certificate proves K_2 < 313/1000`.

## Scope and novelty checks

- The result narrows the interval but does not determine the exact value of
  `K_2`.
- Bounded web/arXiv searches on 2026-08-12 found the post-source paper
  arXiv:2504.03236, Theorem 6.4, proving `K_2 < 0.3177` via a different
  degree-(1,1) rational-inner example and exact degree-twelve calculation.
- Searches found no bound `K_2 < 0.313` and no use of this asymmetric
  one-parameter reflected-linear-polynomial family.
- Novelty is plausible but not certified; specialist bibliographic review is
  recommended.

## Rendering checks

- The final packet compiled cleanly with `latexmk`; all references and
  citations are resolved.
- The final log contains no overfull boxes, underfull boxes, undefined
  references, or warnings.
- All four final PDF pages were rendered at 150 dpi and inspected at original
  resolution after the last LaTeX edit.
- No clipping, overlap, malformed mathematics, illegible text, or bad page
  break was found.  The source-problem crop is readable at normal review zoom.
- Final packet SHA-256:
  `0cda18feca8e8c5b84a19cec3c628dae0bbb1baa47c79633a082222bd29827fb`.
- Source-paper SHA-256:
  `7243d3b55b68380dd4d274c52226311748f8aaf0a4c3f52ed5c836bbd46868c5`.
- Supporting-paper SHA-256:
  `116f25611fcfe21fab6505cd8c4c941ed78d13a1a47302508319a6bfbb330a12`.
