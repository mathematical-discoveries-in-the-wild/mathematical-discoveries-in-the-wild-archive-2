# Verification Report

Candidate: arXiv:2404.19540, exact norm question in Remark 1, PDF page 14.

## Claim Checked

The exact complex-order endpoint, `C_0`, and `L^p -> C_0` norm formulas stated
in `README.md` and `main.tex`.

## Verdict

Likely valid.  This is a partial result, not a solution of the full interior
`L^p` problem.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Kernel modulus and source upper bound | valid | `|k_x(u)|=(x-u)^(tau-1)/|Gamma(xi)|`; Tonelli gives the square `L^1` bound and row integration gives the `L^infinity` bound. |
| `L^1` lower bound | valid | With `h(s)=1_(0,1)(s)s^(xi-1)/Gamma(xi)`, translation continuity in `L^1(R)` implies the normalized average of `h(.-u)`, `0<u<epsilon`, converges to `h`. |
| `L^p -> C_0` exact value | valid | Hölder computes every row norm.  Evaluation at `x=1` gives the matching lower bound by `L^p-L^{p'}` duality. |
| Image lies in `C_0` | valid | For finite `p`, translate the zero extension of `f` in `L^p`; for `p=infinity`, translate the `L^1` kernel.  At `p=1`, `tau>=1`, translating `f` in `L^1` against the bounded kernel gives continuity.  The Volterra support gives value `0` at the left endpoint. |
| `p=1` threshold into `C_0` | valid | The row at `x=1` is in `L^infinity` exactly for `tau>=1`; annular inputs near `u=1` show unboundedness when `tau<1`. |
| `C_0 -> C_0` lower bound | valid | The phase of the row at `x=1` is continuous away from `u=1`. Continuous cutoffs supported in `(0,1)` align this phase and converge in the weighted `L^1` integral. |
| Compactness and norm attainment | valid | The singular convolution kernel is approximable in `L^1` by continuous kernels; Young transfers this to operator norm. Compactness plus reflexivity gives a norming vector for `1<p<infinity`. |
| Strict phase rigidity | valid | Equality in the pointwise triangle inequality gives a common row phase. Fubini produces distinct `u,v` for which `exp(i eta(log(x-u)-log(x-v)))` would be constant in `x`, contradicting its nonzero logarithmic derivative. |
| Strict real-order Young bound | valid | A norming vector exists. Right shifts lose a positive amount of its `L^p` mass for a positive-measure set of large shifts, making the Minkowski integral strict. |
| Scope classification | valid | The theorem closes `p=1`, `p=infinity`, and the adjacent `C_0` problem only; it does not compute the general square norm for `1<p<infinity`. |

## Counterexample Search

The included numerical checker evaluates the explicit `L^1` concentration
family and continuous phase cutoffs for several genuinely complex orders.  No
contradiction was found.  These checks are sanity tests, not proof.

Executed command:

`conda run --no-capture-output -n sandbox python code/check_endpoint_norms.py`

Tested orders were `0.35+1.2i`, `1+2.5i`, and `2.2-0.7i`, with four
concentration/cutoff scales down to `0.01`; the final values approached the
claimed constants from below.  A separate `p=2`, `xi=0.8+0.9i` row-norm
quadrature agreed with the closed formula to the displayed ten digits.

The principal false strengthening was also checked: the Young upper bound is
not the exact square norm for all interior `p`; at `xi=1`, `p=2`, the classical
Volterra norm is `2/pi`, not `1`.

The second false strengthening---equality with the scaled real-order norm for
nonreal `xi`---is ruled out by the formal phase-rigidity proof.  The companion
discretization gives a separate numerical sanity check at `p=2`.

Executed command:

`conda run --no-capture-output -n sandbox python code/check_strict_phase_loss.py`

With 320 cells, the ratios of the discretized complex norm to the scaled
real-order norm were approximately `0.8992`, `0.8949`, and `0.9954` for orders
`0.8+0.9i`, `1+1.5i`, and `1.7-0.6i`, respectively; all were strictly below
one as predicted.

## External Dependencies

None beyond elementary measure theory and `L^p` duality.  The source paper is
used only for the open-problem statement and notation.

## Gaps

No proof gap found in the scoped theorem.  Novelty is uncertain: the formulas
are elementary enough to be folklore even though the bounded search described
in the packet did not locate the complex-order statement.

## Confidence

Score: 96/100.

Reason: all lower bounds are explicit norm-saturating sequences/functionals,
all boundary cases have been checked, and the proof does not rely on a
nontrivial external theorem.

## Human Review Recommendation

Send to a human.  Review the three lower-bound mechanisms, then decide whether
the result is publishably novel or best treated as a useful endpoint lemma.
