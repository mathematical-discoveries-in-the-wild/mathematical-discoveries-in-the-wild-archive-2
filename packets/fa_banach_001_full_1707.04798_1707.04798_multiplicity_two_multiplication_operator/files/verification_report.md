# Verification Report

Candidate: arXiv:1707.04798, Section 4, Problem 1

## Claim Checked

For every `1 < p < infinity`, multiplication by the coordinate on `L^p[0,1]`
with multiplicity two is similar to a compact perturbation of its
multiplicity-one copy.

## Verdict

`likely valid`

This report is an adversarial reread performed in the same working context,
not an independent external verification.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Haar diagonal `D` | valid | On Haar level `n`, multiplication by `t-c_I` has norm at most `2^(-n-1)` because the intervals are disjoint. Uniform boundedness of Haar level projections makes the tail summable in operator norm. |
| Upper bound for `T_epsilon h_I=h_(I epsilon)` | valid | The target square function is pointwise at most `2^(1/p)` times the source square function. |
| Lower bound for `T_epsilon` | valid, external | With `F_n` supported on the chosen children, `E(F_n | F_n-dyadic)=1/2` times the parent-level coefficient function. Stein's vector-valued conditional-expectation inequality gives the required reverse square-function bound for all `1<p<infinity`. |
| Construction of `U` | valid | The constant and root Haar function take the two constant coordinates; left-child and right-child Haar families are disjoint and exhaust every deeper Haar coordinate. Unconditional coordinate projections and the lower bounds for the child maps give a bounded inverse. |
| Diagonal comparison | valid | The conjugated value on `h_(I epsilon)` is `c_I`, while the target diagonal value is `c_(I epsilon)`; their difference has magnitude `abs(I)/4`, tending uniformly to zero by level. |
| Compactness of the null diagonal | valid | On an unconditional Schauder basis, truncating a diagonal multiplier whose coefficients tend to zero converges in operator norm. |
| Final similarity identity | valid | If `M=D+C`, then `U(M direct-sum M)U^(-1)=M+[U(C direct-sum C)U^(-1)+(UD-direct-sum-D U^(-1)-D)-C]`, a compact perturbation. |
| Match to the source question | valid | The source asks exactly for such a compact perturbation and similarity for Lebesgue measure on `[0,1]`, `p!=2`. |

## Failed Attack Routes

1. The child map might have been unbounded because it destroys some nesting.
   The square-function/Stein calculation supplies bounds in both directions,
   so that objection fails.
2. Small errors on individual Haar vectors might not imply compactness. The
   proof instead obtains a summable operator-norm estimate on Haar levels, so
   it does not make that invalid inference.
3. The two image families might fail to form an `L^p` direct sum. They are
   disjoint Haar-coordinate subsets, and unconditional projections recover
   each component; only two components are involved, so the product norm is
   equivalent to the inherited sum norm.
4. A permutation of an arbitrary unconditional basis need not be bounded.
   The proof does not use arbitrary permutability: it proves boundedness for
   these two particular child rearrangements.

## Recommended Human Focus

- Check the normalization in the identity relating the square functions of
  `x`, `T_epsilon x`, and the sequence `F_n`.
- Check that the stated form of Stein's inequality applies to the varying
  conditional expectations used here.
- Check the finite coordinates in the definition of `U`; all other steps are
  uniform tail arguments.

