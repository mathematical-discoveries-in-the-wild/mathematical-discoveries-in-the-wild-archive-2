# Strict p-Dirichlet positivity for Poisson-type generators

Status: `candidate_partial_likely_valid_poisson_generators`.

Source: Bowen Li and Jianfeng Lu, *Interpolation between modified logarithmic
Sobolev and Poincare inequalities for quantum Markovian dynamics*, Journal of
Statistical Physics 190 (2023), 161, arXiv:2207.06422.

## Result

Let `Phi_k` be unital completely positive maps whose duals fix the faithful
state `sigma`, let `gamma_k>0`, and put

```text
L = sum_k gamma_k (Phi_k - id).
```

For every `1<p<infinity`, the source's `p`-Dirichlet form is nonnegative, and
it vanishes at a positive `X` exactly when every `Phi_k` fixes `X`. If `L` is
primitive, this gives

```text
E_{p,L}(Gamma_sigma^{-1}(rho)) > 0
```

for every full-rank density `rho != sigma`.

The proof combines weighted noncommutative `Lp` contractivity with the strict
equality case of Schatten Holder. It does not require detailed balance. In
particular, it settles the source question for the paper's explicit primitive
`[sigma]_{p,0}`-DBC qubit family that is not GNS detailed balanced.

## Scope

This does not solve the question for an arbitrary primitive Lindbladian.
Uniformization fails for some primitive boundary generators even in the full
qubit `[sigma]_{p,0}`-DBC cone: `id+epsilon L` need not be completely positive
for any `epsilon>0`. The packet gives an explicit example and explains the
remaining infinitesimal equality obstruction.

## Verification

The scripts in `code/` implement both Appendix B non-GNS constructions and a
direct GKSL parameterization of the qubit detailed-balance cone. Numerical
global minimization found only the invariant-state zero in 35 appendix-family
regimes and 20 sampled general qubit generators. These computations support
the scope assessment but are not used in the theorem's proof.

Run the principal probes with:

```bash
conda run --no-capture-output -n sandbox python code/numerical_probe.py
conda run --no-capture-output -n sandbox python code/generator_space_probe.py
```

Packet PDF: `solution_packet.pdf`.
