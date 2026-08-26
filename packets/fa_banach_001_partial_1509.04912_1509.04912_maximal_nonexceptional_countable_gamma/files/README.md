# One countable non-dense scalar set for every nonexceptional spectral class

Status: **candidate full theorem, likely valid; sharp maximal spectral partial
answer to Question 3; human review recommended**.

Source: Stephane Charpentier, Romuald Ernst, and Quentin Menet,
*Gamma-supercyclicity*, arXiv:1509.04912.

## Result

Let `Q(i) = Q + iQ`, and define

```text
Gamma_* = Q(i) intersect (
    {|z| < 1} union {|z| > 2} union {Re z > 0}
).
```

This is countable and non-dense. The packet proves that on every
infinite-dimensional complex Banach space, for every bounded operator `T`
with `sigma_p(T*) != {1}`, and every vector `x`,

```text
x is supercyclic for T  iff  x is Gamma_*-supercyclic for T.
```

The only excluded singleton spectral class is unavoidable: Theorem C of the
source at eigenvalue `1` says that any scalar set working uniformly for that
class must be dense in the complex plane. Thus no non-dense scalar set can
extend the theorem to `sigma_p(T*) = {1}`.

The proof combines three mechanisms:

- if the adjoint point spectrum is empty, positive supercyclicity and
  supercyclicity have the same vectors, and `Gamma_*` contains the positive
  rationals;
- for every nonunit eigenfunctional multiplier `mu`, `Gamma_*` is
  tail-universal because `mu^{-n}c` eventually enters the inner disk or the
  exterior region;
- for every nontrivial unimodular eigenvalue, cyclic rotations of the closed
  right half-plane cover the complex plane, so the source's exact Theorem C
  applies.

This is a complete, sharp theorem about maximal uniform spectral coverage by
one small scalar set. It remains a partial answer to the source's broader
request to characterize every admissible `Gamma`.

## Verification

The self-contained proof is in `main.tex`. `VERIFICATION.md` records the
adversarial audit, bounded novelty check, build checks, and recommended human
focus. Run the analytic sanity checker with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1509.04912_maximal_nonexceptional_countable_gamma/code/verify_gamma_star.py
```

Ledger: `ledger/results/1509.04912_maximal_nonexceptional_countable_gamma.json`.
