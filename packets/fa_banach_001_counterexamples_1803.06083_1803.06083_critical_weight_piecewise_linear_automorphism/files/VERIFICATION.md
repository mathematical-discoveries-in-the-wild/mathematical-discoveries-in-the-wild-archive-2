# Verification notes

Verdict: **likely valid claimed counterexample**, pending expert review.

Checks performed:

1. The source statement was checked in the published PDF, page 864.
2. The explicit lift is continuous, increasing, degree one, and has inverse
   with slopes `1/2` and `2`.
3. The rational-branch Fourier formula was derived by splitting input
   frequencies modulo the denominator of the slope.
4. The BV multiplier argument was reduced to modulation conjugates of the
   discrete Hilbert transform on `ell^p(Z)`, valid for `1<p<infinity`.
5. The derivative argument is made first on trigonometric polynomials; no
   unproved chain rule for general Fourier--Lebesgue distributions is used.
6. The critical weighted norm controls the uniform norm by Holder's
   inequality, which identifies the completion with literal continuous
   functions and validates composition/inverse identities after completion.
7. A finite Fourier smoke test was run for `p=1.25, 1.5, 3, 5` and truncation
   sizes through 128. Sample norm ratios remained bounded. This is a sanity
   check only, not proof.

Primary reviewer focus:

- Verify the Stieltjes-integral representation in the BV multiplier lemma.
- Verify the residue-class formula for a rational affine branch.
- Confirm that the source's terse sentence is correctly interpreted as asking
  whether its preceding canonical automorphism classification persists at
  `a=1`.

