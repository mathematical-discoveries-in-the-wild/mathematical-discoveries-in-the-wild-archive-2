# Full Result: Gaussian Multi-Set Concentration

Status: `full` (candidate; subject to human review)

Source: Nathaël Gozlan and Ronan Herry, *Multiple sets exponential concentration and higher order eigenvalues*, arXiv:1804.06133, published in *Potential Analysis* 52 (2020), 203--221.

## Answered Question

Section 5.1 asks whether every probability measure `dμ=e^{-V}dx` on `R^n` with `Hess V >= ρ I > 0` satisfies the multi-set concentration property of every order `k` with a Gaussian profile `exp(-C_{k,ρ,n} r^2)`.

## Full Answer

Yes. One may take the stronger, dimension- and order-independent constant

```text
C_{k,ρ,n} = ρ/2.
```

For every admissible family of separated sets with union `A`,

```text
1 - μ(A_r) <= (1 - μ(A)) exp(-ρ r^2 / 2).
```

The estimate actually holds for every `r >= 0`, not only until the sets' enlargements meet.

## Proof Mechanism

The `Δ_k` mass constraints force `μ(A) >= k/(k+1) >= 1/2`. Caffarelli's contraction theorem realizes `μ` as a 1-Lipschitz image of the Gaussian with covariance `ρ^{-1}I`. Gaussian isoperimetry gives

```text
μ(A_r) >= Φ(Φ^{-1}(μ(A)) + sqrt(ρ) r).
```

For `z=Φ^{-1}(μ(A)) >= 0`, the elementary tail shift

```text
barΦ(z+t) <= exp(-t^2/2) barΦ(z)
```

produces exactly the multiplicative complement factor required in the source definition.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper containing the conjecture.
- `figures/open_problem_crop.png`: readable crop of Section 5.1 from source page 15.
- `code/make_open_problem_crop.py`: reproducible crop script.
- `verification.md`: independent proof and novelty audit notes.

## Novelty Status

Local and bounded web searches on August 11, 2026 found the source, its published version, a thesis reproducing the open question, and adjacent higher-eigenvalue work, but no later answer to this exact Gaussian multi-set question or use of this contraction argument. Novelty is plausible, not certified.

## Scope

This answers the Gaussian profile conjecture in Section 5.1. It does not answer the separate Section 5.2 converse problem for higher eigenvalues or construct new modified log-Sobolev/transport inequalities.
