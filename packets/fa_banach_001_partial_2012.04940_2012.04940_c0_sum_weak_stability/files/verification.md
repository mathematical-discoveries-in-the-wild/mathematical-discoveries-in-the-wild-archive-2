# Verification Report

Candidate: discrete-`K` subcase of the `C_0(K,X)` weak-stability converse in
arXiv:2012.04940.

## Verdict

`likely valid`

Confidence: 95/100.

## Step audit

| Step | Status | Notes |
| --- | --- | --- |
| Dual identification | valid | The dual of an arbitrary `c0`-sum is the `ell_1`-sum of the coordinate duals. |
| Finite-support reduction | valid | Each of finitely many `ell_1` functionals is approximated in norm by a finitely supported functional; the unit-ball diameter bounds the approximation error by twice the dual-norm error. |
| Product neighborhood refinement | valid | After fixing the finite support, small coordinatewise weak inequalities make every coupled finite-support functional small. |
| Coordinate convex combinations | valid | Weak stability of `B_{X_gamma}` makes each finite convex combination of the selected coordinate neighborhoods relatively weakly open. |
| Global target neighborhood | valid | Finite coordinate projections are weak-to-weak continuous, so the intersection of their inverse images is relatively weakly open in `B_Z`. |
| Patching decompositions | valid | On the finite relevant set use coordinate decompositions; outside it copy the target coordinate into every component. |
| Patched vectors lie in the unit ball | valid | Every coordinate has norm at most one. |
| Patched vectors lie in the c0-sum | valid | They differ from the target vector at only finitely many coordinates. |
| Patched vectors return to the original weak opens | valid | The coordinate product neighborhoods were chosen as sufficient subneighborhoods. |
| Necessity | valid | Each coordinate is a norm-one complemented subspace; the packet includes the standard projection argument showing weak stability descends. |
| Injective tensor identification | valid | On finitely supported tensors the injective norm equals the supremum coordinate norm; completion gives `c0(Gamma,X)`. |

## Adversarial checks

- No finite-dimensionality is used: coordinate neighborhoods remain weak, not
  norm neighborhoods.
- The index set need not be countable.  Every individual dual functional has
  countable support and admits finite-support norm approximation; only finitely
  many functionals occur at a time.
- The proof handles arbitrary finite convex combinations, not only midpoints.
- Copying the target off the finite support is legitimate even when the fiber
  spaces vary, because the same target coordinate belongs to every component
  of that coordinate's convex combination.
- The result does not claim the non-discrete scattered case.  At a limit point,
  arbitrary pointwise splittings need not assemble into norm-continuous
  functions; this is precisely where the source used norm stability and a
  Michael selection argument.

## Relation to prior work

Theorem 5.2 of arXiv:1806.10693 proves `c0(X_n)` has CWO when the `X_n` are
finite-dimensional and satisfy the stronger norm-selection property `(co)`.
The present coordinate-weak argument removes both restrictions and allows an
arbitrary index set.  The nearby run packet for that paper does not contain
this theorem.

## Human review recommendation

Check the finite-support neighborhood lemma first; after that, the patching
argument is purely coordinatewise.  If accepted, register this as a substantial
partial solution to the 2020 `C_0(K,X)` converse and as a separate positive
subcase of the injective-tensor CWO question.

