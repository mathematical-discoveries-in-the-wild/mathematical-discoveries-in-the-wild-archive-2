# Verification Report

Candidate: arXiv:1508.00667, Section 10, Question 10.6

## Claim Checked

If the integer Kalton map `K_A` of a subset `A` of a Hausdorff real
topological vector space is a topologically isomorphic embedding, then its
linear Kalton map `lK_A` is also a topologically isomorphic embedding.

## Verdict

`likely valid`

This is an adversarial reread performed in the same working context, not an
independent external verification.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Reduction to topological independence and absolute Cauchy summability | valid | This is exactly the reverse implication of source Theorem 5.1. It also gives algebraic independence. |
| Continuity of the linear Kalton map | valid | This is source Proposition 10.1. |
| Discontinuous coordinate takes every real value on every neighbourhood | valid | After identifying `R a_0` with `R`, this is the standard linear-functional criterion stated as source Lemma 9.6. |
| Discreteness of `Z a_0` | valid | Every one-dimensional subspace of a Hausdorff real topological vector space has its Euclidean topology, so its integer cyclic subgroup is discrete. |
| Tail-span absorption | valid | Source Proposition 9.2(i) gives `span_R(A\F) subset U_3`, which permits arbitrary real tail coefficients. |
| Simultaneous rounding | valid | The packet proves the finite-dimensional Dirichlet lemma by putting `Q^m+1` torus points in `Q^m` boxes. |
| Order of choices | valid | `F` is selected first, then the head tolerance and denominator bound `N`, then discontinuity supplies `x in N^{-1}U_1`. There is no dependence of `F` on `x`. |
| Rounded combination | valid | It has finite support; its distinguished coefficient is the positive denominator `q`, while its three error pieces lie in `U_1`, `U_2`, and `U_3`. |
| Contradiction with topological independence | valid | A witness neighbourhood forces `q a_0` into a neighbourhood meeting `Z a_0` only at zero, impossible for `q>=1`. |
| Openness and final embedding | valid | Source Proposition 10.2 says continuity of all canonical coordinate projections is equivalent to openness of `lK_A`; injectivity and continuity were already established. |
| Match to source question | valid | This is exactly the implication asked in Question 10.6. |

## Counterexample Search

The source's Example 9.4 was checked as the obvious obstruction: its canonical
real projections are discontinuous, but its generating set is not
topologically independent. The proof explains why any attempt to make the
real cancellation small also produces a small integer cancellation after
finite-head simultaneous approximation.

No computational check was performed; none is relevant to the general
topological statement.

## Failed Attack Routes

1. Controlling a tail only after selecting the discontinuity vector leads to
   a circular exceptional set. The final proof fixes the tail and denominator
   bound before choosing that vector.
2. Rounding every coefficient directly gives an uncontrolled sum of errors.
   The final proof separates the finite head from a tail whose entire real
   span is already small.
3. Algebraic independence alone is insufficient, as source Example 9.4
   shows. The contradiction uses the full neighbourhood-witness definition of
   topological independence.

## Recommended Human Focus

- Check the use of the noncontinuous-linear-functional criterion on the
  subspace `span_R(A)`.
- Check that the finite-head approximation is made before the discontinuity
  vector is selected.
- Check the sign convention in `y = qx + sum(z_b-q r_b)b`; it does not affect
  the neighbourhood estimate, and the distinguished error is exactly zero.
