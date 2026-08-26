# Verifier notes

## Claim checked

For every fixed finite `q >= 1`, Theorem 1.5 of arXiv:2507.16516 is false
under the paper's printed definition of a weight.  The scalar map
`F(z) = conjugate(z)` is real analytic and vanishes at zero, while there is
an admissible regular-growth weight (also a q-algebra weight when `q > 1`)
and an `f` in the corresponding weighted Fourier algebra for which
`conjugate(f)` is not in that algebra.

## Proof audit

1. The source definition on PDF page 3 imposes no symmetry or reflection
   comparison on the weight.
2. For `a > b >= 0`, the piecewise polynomial function
   `w0(x)=(1+x)^a` on the positive half-line and
   `w0(x)=(1+|x|)^b` on the negative half-line is submultiplicative.
   Same-sign pairs use `1+s+t <= (1+s)(1+t)`; opposite-sign pairs reduce
   to one of the two factors.
3. It has regular growth and satisfies the Beurling-Domar condition.
4. If `q>1`, set `r=q'` and choose `a>b>1/r`.  The packet partitions the
   convolution integral into three intervals and proves
   `(w0^{-r}*w0^{-r})(x) <= C w0(x)^{-r}` with explicit constants on each
   half-line.  Scaling `w=Lw0`, `L>=C^(1/r)`, gives the paper's normalized
   inequality `w^{-r}*w^{-r} <= w^{-r}`.  Both tails are integrable.
5. With `s=(a+b)/2+1/q`, the function
   `g(x)=1_{x<-1}|x|^{-s}` is in `L^q_w`, but
   `Jg(x)=conjugate(g(-x))` is not.  The two tail exponents are respectively
   `1+q(a-b)/2 > 1` and `1-q(a-b)/2 < 1`.
6. Since the stated hypotheses imply `L^q_w` is contained in `L^1`, Fourier
   transforms are defined and injective.  The identity
   `conjugate(Fourier(g)) = Fourier(Jg)` completes the counterexample.
7. The exact characterization follows from the closed graph theorem and
   the norm identity
   `||Jg||^q = integral |g(x)|^q w(-x)^q dx`.  Boundedness is equivalent to
   essential boundedness of `w(-x)/w(x)`; reflecting once more gives
   two-sided comparability.

## Computational check

Run from the repository root:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2507.16516_asymmetric_weight_conjugation_counterexample/code/verify_asymmetric_weight.py
```

The script checks representative parameters for `q=1,2,3`, performs
50,000 deterministic random submultiplicativity checks in each case,
evaluates the exact constants, and numerically samples the convolution
ratio.  These checks are redundant; the packet's proof is exact.

## Scope cautions

- The result refutes the theorem as written and identifies a necessary and
  sufficient condition for the conjugation step.
- It does not claim that reflection comparability alone makes the entire
  proof of Theorem 1.5 valid; other localization/scaling steps were not
  re-proved here.
- It does not settle the separate Beurling-Domar versus GRS question.
- If the authors intended "weight" to include symmetry by convention, the
  explicit definition must be corrected and this packet identifies the
  missing hypothesis rather than refuting that intended symmetric theorem.
