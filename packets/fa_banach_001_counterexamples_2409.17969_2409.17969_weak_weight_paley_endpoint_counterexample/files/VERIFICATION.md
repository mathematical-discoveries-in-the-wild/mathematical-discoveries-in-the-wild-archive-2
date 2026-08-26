# Verification record

Verified at: 2026-08-17T21:20:02Z

Verdict: `candidate_counterexample_likely_valid` — a full negative answer to
the literal all-exponent weak-weight upgrade in Remark 5.2(1), together with
an affirmative theorem for the strict interior `1<p<2`, `p<q<p'`.

## Mathematical audit

- The source's Theorem 1.11 is stated for `1<=p<=2`, so `p=q=1` is inside
  the literal scope of the question.
- The source's rank-one estimate
  `|c(lambda)|^{-2} asymp lambda^2(1+|lambda|)^{n-3}` implies that Plancherel
  intervals of radius `R>=1` have measure comparable to `R^n`.
- For `u(lambda)=(1+|lambda|)^{-n}`, the distribution estimate
  `mu{u>alpha}<=C/alpha` proves finite weak c-norm.  On `[1,R]`, the weighted
  Plancherel mass is bounded below by `c int_1^R dlambda/lambda=c log R`.
- Nonnegative normalized smooth functions supported in `B(o,1/R)` exist.
  The standard Iwasawa-projection bound `|H(x^{-1}k)|<=d(o,x)` and
  `|exp(z)-1|<=exp(|z|)|z|` imply that their Helgason transforms at
  `lambda+i rho` are uniformly within `1/2` of one for every `k` and
  `|lambda|<=bR`, for one fixed sufficiently small `b>0`.
- The scalar ratio at `q=1` is bounded below away from zero for large real
  `lambda`.  Hence the proposed `p=q=1` left side grows at least as `log R`,
  while its right side is constant because both the weak norm of `u` and the
  `L^1` norm of the test function are fixed.
- For `1<p<2` and `p<q<p'`, the interval
  `(p,min(q,q'))` is nonempty.  Choosing `r` there gives `r<q<r'`.
- Theorem 2.3 reproduced in the source gives the sublinear map
  `G_q:L^1->L^infinity`; Theorem 2.2 gives `G_q:L^r->L^{r'}` on the same
  non-unitary line.  Real interpolation gives
  `G_q:L^p->L^{p',p}` because `theta/r'=1/p'`.
- Lorentz power identities give
  `G_q^p in L^{1/(p-1),1}` and
  `u^{2-p} in L^{1/(2-p),infinity}`.  These exponents are conjugate, so
  Lorentz Holder yields exactly the requested weak-weight power
  `||u||_{1,infinity}^{2/p-1}` after taking the pth root.
- The omitted scalar factor is at most one since
  `(rho_q+2rho)^2-rho_q^2=8rho^2/q>0`.
- The packet does not claim the edge lines `q=p,p'` for `1<p<2`; the
  auxiliary interpolation exponent ceases to exist there.

## Upgrade record

Eight focused stages were completed: exact-scope audit, later-literature
audit, critical-weight scaling, approximate-identity counterexample,
generalization to every rank-one space, interior Lorentz refinement,
weak-weight Lorentz pairing, and edge plus broad-question obstruction audit.
The endpoint counterexample was upgraded to a positive classification of the
entire strict interior.

## Literature audit

Bounded primary-source searches through 2026-08-17 found arXiv:2409.17969 and
adjacent 2024 Fourier-inequality papers, but no later arXiv work stating the
endpoint counterexample or the strict-interior Lorentz upgrade.  The latter is
short enough to be folklore; this is a novelty screen, not a definitive
priority determination.

## Computational and packet checks

- `conda run --no-capture-output -n sandbox python code/verify_exponents.py`
  passed.  It verifies the auxiliary-exponent interval, interpolation and
  Lorentz conjugacy identities, logarithmic critical model, weak-norm scaling,
  and the scalar-factor inequality.
- LaTeX compiled without matched warnings, overfull boxes, underfull boxes,
  undefined references, or errors in the final log.
- The final packet has three A4 pages.  Every page was rendered at 180 dpi
  and visually inspected; the question crop, theorem, counterexample,
  Lorentz proof, limitations, and references are readable and unclipped.
- Text extraction from the final PDF contains both results, the exact
  remaining boundary, and the references.

SHA-256:

- `solution_packet.pdf`: `e0a936afda4f359ae86977a5e35a58a0862aa8f3ab5c9fae70062ded8188214b`
- `source_paper.pdf`: `94277264576fbbfe532478b605bc8de7d9b1207c2b41d92538f92c0fea81f83f`
- `figures/open_problem_crop.png`: `bedc0992feaf9e11bd479122b6eec828d3fd63827f290bc7264f00bee6b7d3b2`
- `code/verify_exponents.py`: `15bb05235da80bc9045f8712a8e3658a440953b020acf930ba9030b16029b934`

## Human review priorities

1. Confirm the Iwasawa-projection normalization and uniform transform-flatness
   estimate for the chosen shrinking approximate identities.
2. Recheck the real interpolation of the sublinear mixed-norm transform and
   the Lorentz power/Holder step.
3. Decide whether the source intended Remark 5.2 only for `1<p<=2` despite
   Theorem 1.11's displayed `p=1` scope; the strict-interior theorem remains
   new mathematical content either way.
4. Repeat the novelty search beyond arXiv before dissemination.

