# Verification Record

- Target: the quantitative sharpness and finite-k question in the concluding
  paragraph of arXiv:2603.03549v1, source PDF page 12.
- The source convention that `R^n` has coordinatewise order, the definitions
  of `e_up`, `e_{k,up}`, metric poset, and radiality, and the scalar theorem
  equating constant-one extension with radiality were cross-checked against
  the parsed TeX and source PDF.
- The literature audit covered the cheap run indexes, exact source sentence,
  title, arXiv id, monotone extension constants, radial metric posets, and
  coordinatewise Euclidean order through 17 August 2026. It found arXiv v1
  and the scalar predecessor but no later answer or correction.
- Proof audit:
  1. the height-three finite poset has the discrete metric and is radial;
  2. the middle antichain data `+/-e_j/2` have diameter exactly one;
  3. isotonicity forces every top coordinate to be at least `1/2` and every
     bottom coordinate to be at most `-1/2`;
  4. the top-bottom domain distance is one, forcing Lipschitz constant at
     least `sqrt(n)` for every extension;
  5. coordinatewise scalar extension gives the matching radial upper bound;
  6. restricting to `m` coordinate pairs gives the finite-k lower bound;
  7. the three-point nonradial metric satisfies all triangle inequalities,
     and its separated countable union is a discrete metric poset with
     infinite two-point extension constant.
- Arithmetic command:

  `conda run --no-capture-output -n sandbox python code/verify_extremizers.py`

  Result: pairwise image distances and all restricted coordinate gaps passed
  for `n=1,...,128`; 1000 nonradial blow-up scales passed. These are
  consistency checks only; the finite proof is exact.
- `solution_packet.pdf` was compiled after the required PDF artifact marker.
  The final LaTeX pass has no warnings, errors, overfull boxes, underfull
  boxes, duplicate destinations, or undefined references.
- The final PDF has 3 letter-size pages. Text extraction confirmed the source
  question, Theorem 1, Proposition 1, scope correction, human-review section,
  and references.
- Every final page was rendered at 150 dpi and visually inspected after the
  latest source edit. The source crop is legible and there is no clipping,
  overlap, malformed equation, or bad page break.

Final SHA-256: `9f3734b267878a3c1667d1a09fd513593779cb920d47df8e111899148064a1c6`.

