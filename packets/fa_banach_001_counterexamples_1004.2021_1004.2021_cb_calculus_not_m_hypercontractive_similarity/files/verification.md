# Verification Record

- Target: the open converse in arXiv:1004.2021v2 asking whether, for radial
  noncommutative varieties of order `m>=2`, complete boundedness of the
  variety-algebra polynomial calculus implies joint similarity to a tuple
  in the variety.
- The question, the definition of the domain, the universal weighted-shift
  coefficients, the variety algebra, and the nearby strong-purity condition
  were checked against the local parsed arXiv source.
- Cheap indexes and bounded exact-wording, title, arXiv-id,
  `m`-hypercontraction, completely-bounded-calculus, Bergman-shift, and
  later-similarity searches through 17 August 2026 found no resolution of
  this exact converse.  No priority claim is made.
- Proof audit:
  1. for `f=X`, `b_k^(m)=binomial(k+m-1,m-1)` and the universal weight is
     `sqrt((k+1)/(k+m))`;
  2. the model is multiplication by `z` on the kernel space
     `(1-z wbar)^(-m)`;
  3. weighted Bergman integration and reproducing kernels give the exact
     matrix norm `||P(W_m)||=sup_D ||P(z)||`;
  4. the Hardy shift has the same matrix polynomial norm, so the calculus
     map is a unital complete isometry;
  5. similarity to an order-`m` domain element, `m>=2`, yields the positive
     order-two defect for `R=Y^(-1)Y^(-*)`;
  6. diagonal entries make the first differences of
     `r_k=<R e_k,e_k>` nondecreasing and start them at least at `r_0`;
  7. invertibility gives `r_0>0`, hence linear growth, contradicting
     boundedness of `R`;
  8. `S^k S*^k` are tail projections and converge strongly to zero.
- Auxiliary command:

  `conda run --no-capture-output -n sandbox python code/verify_shift_obstruction.py`

  Result: all exact shift and defect checks passed.
- `solution_packet.pdf` was compiled after the required PDF artifact marker.
  The final LaTeX pass has no warnings, errors, overfull boxes, underfull
  boxes, duplicate destinations, or undefined references.
- The final PDF has three letter-size pages.  Text extraction confirmed the
  source question, matrix-norm lemma, full counterexample, scope, novelty
  statement, human-review recommendation, and references.
- Every final page was rendered at 150 dpi and visually inspected after the
  latest source edit.  There is no clipping, overlap, malformed equation,
  or bad page break.

Final SHA-256: `cad29497f1913a3ebf712d78567b24d590cdf3501bc97277118cfada20d24796`.
