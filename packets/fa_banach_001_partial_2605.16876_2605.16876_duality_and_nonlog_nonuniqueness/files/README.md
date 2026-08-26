# Duality and non-logarithmic nonuniqueness

Status: `candidate_substantial_partial_likely_valid`

Source: Sejong Kim and Vatsalkumar N. Mer, *A multivariable mean equation
arising from the spectral geometric mean*, arXiv:2605.16876 (2026).

Source location: Section 4, Open problem, page 21 of the arXiv PDF.

## Result

For `g` in the normalized operator-monotone class `L`, the source asks for a
classification of when

```text
sum_i w_i g(A_i # X^{-1}) = 0
```

has a unique positive-definite solution for every input tuple.

This packet proves three advances:

1. The duality `g^vee(x)=-g(x^{-1})` preserves the global uniqueness
   property and gives an exact inversion formula for solution sets.
2. Besides the source's Wasserstein endpoint `g(x)=x-1`, the dual endpoint
   `g(x)=1-x^{-1}` is globally unique, with solution
   `Omega(omega; A_1^{-1},...,A_m^{-1})^{-1}`.
3. Nonuniqueness is not special to `log x`.  The explicit non-logarithmic
   operator-monotone function

   ```text
   g(x)=200 (x^(1/100)-1)/(x^(1/100)+1)
   ```

   admits a three-input real `2x2` example with two distinct solutions.
   More generally, nonuniqueness persists for all sufficiently small positive
   parameters in the self-dual family

   ```text
   g_s(x)=(2/s)(x^s-1)/(x^s+1).
   ```

The full necessary-and-sufficient classification remains open.

## Verification

The second solution is obtained by Poincare–Miranda on an explicit rectangle.
The included interval-arithmetic verifier checks all four face inequalities
for both the logarithmic limit and `s=1/100`, using 8,000 exact-decimal
subintervals per face.  For `s=1/100`, the smallest certified sign margin is
greater than `2.7e-5`.

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2605.16876_duality_and_nonlog_nonuniqueness/code/verify_faces.py
```

The proof is otherwise exact.  The code certifies the face signs; it does not
replace the operator-monotonicity, calibration, or duality proofs.

## Novelty and scope

The local indexes and a bounded web/arXiv search on 11 August 2026 found the
May 2026 source, generalized Karcher background, and operator-monotonicity
literature, but no later classification, no duality theorem for this outer
equation, and no nonuniqueness result for the displayed `g_s` family.
Novelty confidence is moderate because the source is very recent and search
coverage is bounded.

## Packet contents

- `main.tex`: theorem statements and proofs.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: page-21 question crop.
- `code/verify_faces.py`: reusable interval certificate.
- `verification.md`: adversarial proof and render audit.

Human review recommendation: **review as a substantial partial theorem**,
focusing on the Pick-function proof, the exact `B_3` calibration, and the
interval implementation.

