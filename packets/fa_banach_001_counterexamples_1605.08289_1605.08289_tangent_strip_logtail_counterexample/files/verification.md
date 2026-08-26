# Verification report

Verdict: candidate full negative answer, likely valid.

## Exact target

Question 34 on PDF page 13 of arXiv:1605.08289 asks whether, for finite
integer `p`, some `F in A^p(Omega)` fails to lie in
`A^p(D) + A^p_0(C-hat \ closure(D'))` when the two circles are internally
tangent.  The source screenshot is `figures/open_problem_crop.png`.

## Proof checks completed

1. Direct algebra verifies that `w=(1-z)^(-1)` sends the crescent to
   `1/2 < Re w < 1/(2r)`.
2. The exponential map sends this strip to the upper half-plane; the cutoff
   denominator has its only zero at `-i`, outside the closed image.
3. `Log(2-iw)` is analytic and nonzero on a neighborhood of the closed strip:
   `2-iw` has strictly negative imaginary part, and `Log(2-iw)=0` would force
   `Re w=0`.
4. Applying `T=w^2 d/dw` at most `p` times gives limits zero at both strip
   ends.  At the positive end the `p`-th derivative is
   `(-1)^p p!/Log(2-iw) + O(Log^{-2}|w|)`; the negative end is exponentially
   small up to polynomial factors.
5. On the outer circle, `w(e^{it})=1/2+(i/2)cot(t/2)`, giving the claimed
   one-sided `1/log(1/t)` trace.
6. The exact imaginary part of the Cauchy kernel isolates
   `-integral dt/(t log(1/t))`; all omitted pieces are uniformly bounded.
7. Differentiating a hypothetical decomposition `p` times is legitimate, and
   the exterior summand has zero outer-circle Cauchy integral inside `D`.

## Numerical sanity check

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1605.08289_tangent_strip_logtail_counterexample/code/check_asymptotics.py
```

For `p=0,1,2,3`, the positive-end normalized derivative approaches its
predicted coefficient, the negative-end values decay exponentially, and the
shrinking positive-arc integral tracks the log-log model.  This computation
is not part of the proof.

## Artifacts

- Source PDF SHA-256:
  `1263627447a4abf422b0c8cc35a551f1ef4db1d7ac67862b047df5f0f1389b6d`
- Question crop SHA-256:
  `b977c6697e87812d38c059e6a1205d4d4076ac89c926d91aedaa680431e5ca7b`
- Solution packet SHA-256:
  `66080b9103f9a6d96d5f3f19f3d838d30cc08df82d29bb9e4b1028eb37a38406`

The five-page packet compiled without warnings, overfull boxes, underfull
boxes, or undefined references.  All five pages were rendered at 130 dpi and
visually inspected; the source crop is readable and no content is clipped.
