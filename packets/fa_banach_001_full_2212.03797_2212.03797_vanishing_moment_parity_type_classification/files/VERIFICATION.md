# Verification Report

Candidate: arXiv:2212.03797, Remark 3.18

## Claim Checked

The vanishing-(k)th-moment inequality (3.18) characterizes Rademacher type
(p) exactly for odd (k); for even (k) it is vacuous over real Banach
spaces.

## Verdict

`likely valid`

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Even moment forces zero | valid | Repeated dual evaluation gives a nonnegative scalar even moment; strong measurability supplies a separable essential range and hence a countable norming family. |
| Odd Rademacher variables are admissible | valid | For deterministic (z_j), \(\eta_j=r_jz_j\) are independent and \(\mathbb E[r_j^k]=0\) when (k) is odd. |
| Linear coefficient extraction | valid | Lagrange differentiation at nodes (0,1,\ldots,k) gives \(c_0=-H_k\), \(c_\ell=(-1)^{\ell-1}\binom{k}{\ell}/\ell\), and extracts the coefficient of (t). |
| Symmetrization factor | valid | The coefficient of (t) in \((y+tu)^{\otimes k}\) is (k\operatorname{sym}(y^{\otimes(k-1)}\otimes u)\). |
| Balanced scaling | valid | With (a=\|x\|^{1/k}\), both (ay_0) and (a^{-(k-1)}x) have norm (a), so the (kp)-power cost is \(\|x\|^p\). |
| Tensor lower bound | valid | A norming functional on (H=\ker\psi\) extends as (f(x)=\phi(Px)+\psi(x)), with \(\|f\|\le3\) and (f(y_0)=1), recovering the Rademacher sum after (k)-fold evaluation. |
| Passage from hyperplane to (E) | valid | (E=H\oplus\mathbb Ry_0); type (p) is stable under this finite-dimensional extension, and the packet supplies the direct estimate. |

## Counterexample Search

No numerical counterexample search is required. The even-order case gives an
explicit structural counterexample: (E=\ell_1), which lacks type (p>1),
satisfies the inequality because every admissible random variable is zero.

The interpolation checker verifies the exact coefficient formula for all
(1\le k\le20).

## External Dependencies

- Corollary 3.17 of the source paper: checked in the local PDF, pages 14--15;
  it supplies the already-proved sufficiency direction.
- No later theorem is used in the necessity proof.

## Gaps and Scope

- No proof gap is presently known.
- The result answers the necessity question for (3.18). It does not by itself
  prove sharpness of the distinct i.i.d. Monte Carlo estimate (3.13).
- Novelty was checked only within the bounded sources listed in the README.

## Confidence

Score: 94/100.

Reason: all reductions are finite, explicit, and norm-controlled. The main
human-review risks are convention-level: whether the source's symmetric tensor
normalization agrees with the factor (k), and whether the question intended
to exclude the degenerate even-order formulation.

## Human Review Recommendation

Send to a Banach-space/tensor-products specialist.

