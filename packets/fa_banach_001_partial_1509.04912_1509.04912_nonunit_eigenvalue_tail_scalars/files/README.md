# Tail-universal scalar sets for nonunit adjoint eigenvalues

Status: **candidate substantial partial result, likely valid; human review recommended**.

This packet is superseded by the stronger common-set theorem in
`solutions/partial/1509.04912_maximal_nonexceptional_countable_gamma/`, which
uses one countable non-dense scalar set for all nonunit multipliers and also
covers the empty-spectrum and nontrivial unimodular regimes.

Source: Stephane Charpentier, Romuald Ernst, and Quentin Menet,
*Gamma-supercyclicity*, arXiv:1509.04912, published in 2016.

## Result

Fix a nonzero complex multiplier `mu`. Call `Gamma` tail-universal for
`mu` when

```text
dist(c, mu^n Gamma) -> 0 for every c in C.
```

The packet proves that if `f(Tx) = mu f(x)` for a nonzero functional `f`,
then every supercyclic vector for `T` is Gamma-supercyclic whenever `Gamma`
is tail-universal for `mu`. The reverse implication is automatic, so the
two notions coincide throughout this spectral class.

This eigenfunctional formulation avoids a convention-dependent conjugation:
under the usual complex-linear dual convention `mu` is an adjoint eigenvalue;
under the source paper's conjugate-dual notation the adjoint eigenvalue is
`conjugate(mu)`. Its modulus is the same in either convention.

For every `|mu| != 1`, there is an explicit countable, non-dense scalar
set with this property. Let

```text
F_n = {(j+ik)/n : j,k in Z and j^2+k^2 <= n^4},
Gamma_mu = union_{n>=1} mu^{-n} F_n.
```

Then `mu^n Gamma_mu` contains the increasingly fine lattice disk
`F_n`, hence is asymptotically dense at every fixed scalar. If
`|mu|>1`, the unscaled blocks shrink to zero; if `|mu|<1`, their
nonzero points escape every bounded disk. Thus `Gamma_mu` is not dense.

This gives a uniform positive theorem in the nonunit-eigenvalue regime that
the source explicitly leaves unclear. It does not characterize every scalar
set in that regime, and it does not address the empty adjoint point-spectrum
case.

## Verification

The formal proof is in `main.tex`. `VERIFICATION.md` records the adversarial
audit, numerical sanity check, PDF review, novelty bounds, and recommended
human focus.

Run the checker with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1509.04912_nonunit_eigenvalue_tail_scalars/code/verify_tail_scalars.py
```

Ledger: `ledger/results/1509.04912_nonunit_eigenvalue_tail_scalars.json`.
