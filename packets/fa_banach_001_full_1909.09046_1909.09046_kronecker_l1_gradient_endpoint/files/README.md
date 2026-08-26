# Full Result: The Kronecker `L^1`-Gradient Endpoint

Status: `full` (candidate; subject to human review)

Source: Louis Brown and Stefan Steinerberger, *On the Wasserstein Distance between Classical Sequences and the Lebesgue Measure*, arXiv:1909.09046, published in *Transactions of the AMS* 373 (2020), 8943--8962.

## Answered Questions

Following Theorem 7, the source asks:

1. Can the Kronecker-sequence integration estimate replace the `L^2` gradient factor by the sharper `L^1` factor proved for regular grids?
2. Does any single infinite sequence attain that regular-grid endpoint uniformly in `N`?

## Full Answer

Yes to both. If `d>=2`, `α in R^d` is badly approximable, and `x_j=jα mod 1`, then uniformly in `N`,

```text
| integral f - (1/N) sum_{j=1}^N f(x_j) |
  <= C_{α,d} N^{-1/d}
     ||grad f||_infinity^((d-1)/d) ||grad f||_1^(1/d).
```

Thus the same badly approximable Kronecker sequence supplies the requested infinite sequence.

## Proof Mechanism

At heat time `t=N^{-2/d}`, decompose the discrepancy measure into its atomic-to-smoothed and smoothed-to-uniform parts. Both are divergences:

- the source's Fourier estimate puts the smoothed field in `L^2` with norm `O(N^{-1/d})`;
- bad approximability separates the first `N` points at scale `N^{-1/d}`, and heat-kernel packing puts the truncated Coulomb field in weak `L^{d/(d-1)}` with the same norm.

Their sum is paired with `grad f` using Lorentz duality. The elementary interpolation

```text
||g||_{L^{d,1}} <= C_d ||g||_infinity^((d-1)/d) ||g||_1^(1/d)
```

gives the endpoint.

## Files

- `solution_packet.pdf`: rendered full proof.
- `source_paper.pdf`: the original paper.
- `figures/open_problem_crop.png`: crop of Theorem 7 and both exact questions on source page 8.
- `code/make_open_problem_crop.py`: reproducible crop script.
- `verification.md`: proof and novelty audit.

## Novelty Status

Bounded local and web searches on August 11, 2026 found the source, its journal version, adjacent Wasserstein work, and later quasi-uniformity results for Kronecker sequences, but no claimed answer to this endpoint or the critical heat-field proof. Novelty is plausible, not certified.

## Scope

The result covers the source range `d>=2` and badly approximable `α`. It does not classify every endpoint sequence or prove bad approximability necessary.
