# Counterexample to the `p=0,q=1` asymptotic-tightness endpoint

This packet identifies a false endpoint in Theorem 2 of arXiv:2306.12288.
For the binary Bonami--Beckner semigroup, every function satisfying the
positive order-zero entropy constraint has proper support.  Connectedness
then forces a boundary edge, on which the continuous `q=1` Dirichlet form
diverges.  Consequently

```text
Xi_{0,1}^{(n)}(alpha)=+infinity
```

for every `n>=1` and `0<alpha<ln 2`, contrary to the claimed finite limit
`Xi_1(alpha)`.  The packet also identifies the false boundedness fact in the
proof and the analogous obstruction to including `p=0` when `q<1`.

Files:

- `solution_packet.pdf`: self-contained theorem, proof, intuition, and audit.
- `source_paper.pdf`: official latest arXiv PDF (v2).
- `evidence/*.png`: unaltered RGB crops of the theorem, finite binary formula,
  and failing proof fact.
- `code/verify_endpoint.py`: finite-cube and regularization regression checks.
- `main.tex`: packet source.
- `VERIFICATION.md`: independent proof, computation, and render audit.
