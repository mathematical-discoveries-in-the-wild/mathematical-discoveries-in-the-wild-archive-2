# A degree-gap obstruction to joint complete monotonicity

This packet gives a full negative answer to Question 4.6 of arXiv:2506.08447v2,
*Joint Complete Monotonicity of reciprocal of a polynomial in two variables*,
by Mandar N. Khasnis and Vinayak M. Sholapurkar.

## Files

- `solution_packet.pdf`: review-ready theorem and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: official current arXiv v2 PDF (17 October 2025).
- `figures/question_4_6_crop.png`: source PDF page 10, including Question 4.6.
- `VERIFICATION.md`: source, proof, novelty, build, and visual-QA record.
- `code/crop_source.py`: reproducible source-crop helper.

## Result

For arbitrary positive sequences `a_m,b_m`, put `r_m=b_m/a_m`.  The net

```text
beta(m,n) = 1 / (b_m + a_m n)
```

is jointly completely monotone if and only if, for every `0<t<1`,

```text
h_m(t) = a_m^(-1) t^(r_m-1)
```

is a one-variable Hausdorff moment sequence in `m`.  Consequently joint
complete monotonicity forces `Delta^2 r_m <= 0` for every `m` (and also forces
`a_m` to be log-concave).

If `a,b` are positive polynomials with positive leading coefficients and
`deg(b)-deg(a)>=2`, the rational function `b/a` is eventually strictly
convex.  Its sampled sequence therefore has a positive second difference for
all sufficiently large indices, contradicting the necessary concavity.

Question 4.6 has a cubic `b` and linear `a`, so its degree gap is two.  The
answer is therefore **no for every parameter choice**, including every
`0<b_1<a_1<b_2<b_3`; the ordering plays no role.

## Review focus

The decisive checks are Hausdorff determinacy of the explicit vertical slice,
the converse construction integrating the one-variable representing
measures, and the sign in the log-convexity ratio.  These are all proved in
the packet rather than deferred to an unproved lemma.
