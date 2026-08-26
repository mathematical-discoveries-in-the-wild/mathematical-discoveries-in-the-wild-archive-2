# Verification report

Verdict: likely valid candidate full solution, pending expert review.

## Scope match

Remark 2.5 of arXiv:2509.08547v3 asks whether Theorem 2.3 extends from the
squared Euclidean cost to general continuous costs. The packet keeps the
source's compact-support, normalization, connectedness, and step-size
hypotheses, replaces the cost by an arbitrary continuous function, and proves
the same eventual linear `L^2` convergence. The proof actually does not use
the condition that the marginals avoid boundaries of convex sets.

## Proof audit

1. **Preconvergence is cost-agnostic.** The source explicitly identifies
   negligible zero-level sections as the only use of the quadratic form. The
   positive-part inequalities, the `2/epsilon` gradient Lipschitz bound, and
   the Arzelà--Ascoli argument require only continuity of the cost. A direct
   secant-slope calculation gives a common modulus of continuity for all
   iterates.
2. **Uniformly thick active core.** From
   `integral (xi_*)_+ dQ = epsilon`, with
   `B = ||(xi_*)_+||_infinity`, one obtains
   `Q{xi_* > epsilon/2} >= epsilon/(2B)` uniformly in `x`; the symmetric bound
   holds uniformly in `y`.
3. **Core kernel.** Vanishing core energy gives `f(x)+g(y)=0` almost everywhere
   on the open core. Every point of the connected support has a product
   neighborhood inside the core. On each such neighborhood `g` is almost
   everywhere constant; overlapping neighborhoods have the same constant.
   Connectedness makes `g` globally constant, and normalization forces both
   components to vanish.
4. **Spectral gap.** The core operator is a positive multiplication operator
   with diagonal bounded below, plus a Hilbert--Schmidt cross operator. Its
   compression to the normalized space is Fredholm. Trivial kernel therefore
   gives a lower spectral bound `kappa > 0`.
5. **Exact recurrence.** The positive-part secant slope is a measurable weight
   `w_n in [0,1]`. Uniform convergence of `xi_n` to `xi_*` implies `w_n=1` on
   the fixed core for all sufficiently large `n`. Hence the exact weighted
   operator has spectrum in `[kappa,2]`.
6. **Contraction.** With `a=eta/epsilon in (0,1)`, the exact error operator has
   spectrum in `[1-2a,1-a kappa]`, a compact subinterval of `(-1,1)`.

## Computational sanity check

The included script constructs connected finite bipartite cores with positive
vertex weights. It computes the core gap on the normalized subspace, samples
larger secant weights, and checks both spectral domination and the claimed
contraction bound.

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2509.08547_general_continuous_cost_linear_convergence/code/verify_weighted_core.py
```

The finite checks are sanity tests only; the formal proof uses the compact
cross-operator/Fredholm argument.

Output on 2026-08-09:

```text
configurations=216
weight_samples=4320
status=PASS
```

## Principal review risk

The highest-value review point is the measure-theoretic kernel argument:
confirm that local almost-everywhere constancy on the product neighborhoods of
the strictly active core patches globally across the connected topological
support. Full support ensures every nonempty relative-open overlap has
positive measure.
