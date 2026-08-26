# Verification report

Verdict: `candidate_counterexample_likely_valid`.

## Exact checks

1. Source page 16, Question 5.1, asks about nondegenerate positive
   semidefinite continuous kernels on a transitive continuous group action.
   It does not require strict positive definiteness or analyticity.
2. Source page 17, Question 5.4, asks about a separately continuous positive
   semidefinite nondegenerate kernel and allows any continuous homomorphism
   `alpha:G->R`; `alpha=0` is permitted.
3. The Gram form of `K_a` is the sum of two squared moduli, so positivity is
   exact.
4. `K_a(z,z)=1+a>0`, establishing the source's nondegeneracy condition.
5. For `0<a<1`, `|K_a(z,w)|>=1-a>0`.  This justifies cancellation in the
   multiplier-class argument.
6. Rotation invariance is exact.  Any multiplier is therefore constant
   unimodular, and this family is independent of `a`.
7. Evaluations at `(1,1)` and `(1,-1)` rule out scalar proportionality when
   `a!=b`.
8. The same two evaluations prove that `K_a` is not constant for Question
   5.4.

## Numerical sanity check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1711.05211_rotation_invariant_kernel_rigidity_counterexamples/code/verify_rotation_kernels.py
```

The script checks 32-point Gram matrices for `a=0.2,0.5,0.8`, 41 rotations,
and the nonproportionality of `K_0.25` and `K_0.5`.  Expected output ends in
`all checks passed`.

The computation is not part of the proof.

## Reviewer focus

Confirm that the source's phrase “equal multipliers” is interpreted modulo
the constant phase ambiguity described before Proposition 4.6.  The packet
is robust to either interpretation: both kernels admit the identical
representative `1`, and their entire multiplier families are identical.

