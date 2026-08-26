# Verification Report

Candidate: arXiv:2003.13573, Remark 5.4

## Claim Checked

For `p_s(z)=|z|^s`, the integration operator has noncanonical closed invariant
hyperplanes on both `A_p_s` and `A_p_s^0` when `0<s<1`, and on `A_|z|^0`
when `s=1`.

## Verdict

`likely valid`

Confidence: 97/100.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Cauchy derivative estimate | valid | Optimizing `exp(ar^s)r^-n` gives `r^s=n/(as)` and the displayed bound. |
| Absolute convergence for `0<s<1` | valid | The majorant is `[C n^(-(1/s-1))]^n`, which is summable after any geometric multiplier. |
| Continuity on `A_p_s^0` | valid | One defining seminorm controls the functional for `s<1`; for `s=1`, choose `a` with `ea|mu|<1`. |
| Continuity on `A_p_s` for `s<1` | valid | The restriction is bounded on every normed step; the inductive-limit topology is final. |
| Eigenfunctional identity | valid | `(Jf)^(n)(0)=f^(n-1)(0)` for `n>=1`, with zero constant term. |
| Closed invariant hyperplane | valid | `Lambda_mu(1)=1`, so the continuous kernel is proper and codimension one; the eigenidentity gives invariance. |
| Noncanonical form | valid | `z-mu` lies in the kernel and has nonzero constant term, unlike every proper vanishing-jet tail. |
| Scope match | valid | This disproves the proposed extension and settles all cases explicitly highlighted except the source's already-positive `Exp(C)` case. |

## Counterexample Search

No numerical search is needed: the counterexamples are explicit linear
hyperplanes. Testing on monomials gives
`Lambda_mu(z^k)=mu^k k!`, which is consistent with the proof and with
`Lambda_mu(Jz^k)=mu Lambda_mu(z^k)`.

## External Dependencies

- Cauchy's integral estimate: standard and used explicitly.
- The descriptions of `A_p` and `A_p^0` as inductive/projective limits:
  stated in the source paper immediately before Theorem 5.1.

## Gaps Sought

- The series might fail to define a functional on finite-type spaces. It does
  fail at exponential order, explaining why the source's `Exp(C)` theorem is
  safe, but the supergeometric decay for `s<1` closes this concern.
- A codimension-one invariant subspace might accidentally be a canonical
  tail. The element `z-mu` rules this out.
- Inductive-limit continuity might require a uniform bound across all steps.
  It does not: the locally convex inductive limit uses the final topology, so
  continuity on every step is the correct criterion.

## Human Review Recommendation

Send to human. The proof is short and self-contained. The only point worth
checking against the source's conventions is the final-topology continuity
criterion for its chosen (LB)-realization of `A_p_s`.

