# Positive `r`-logSob constants separate from `0` on bounded-degree expanders

Status: `candidate partial result, likely valid`.

Open Problem (I) of arXiv:1108.1210 asks which intervals of normalized
`r`-logSob inequalities are uniformly equivalent over all finite reversible
Markov semigroups.  The source proves that `0` and `1` are not equivalent.
This packet extends its expander mechanism to every fixed `0<r<1`:

```text
C_r(G) >= c(r,d) log |V(G)|
```

for connected `d`-regular graphs of fixed degree, while bounded-degree
spectral expanders have uniformly bounded `C_0`.  Consequently, no interval
containing `0` and any positive point can have the requested equivalence
property.  Intervals contained in `(0,1)` remain open here.

Files:

- `solution_packet.pdf`: theorem, proof, scope, novelty search, and review notes.
- `source_paper.pdf`: official arXiv:1108.1210 PDF.
- `figures/open_problem_crop.png`: full-width source crop of Open Problem (I).
- `code/verify_expander_algebra.py`: regression check for the exponent and
  Chernoff-constant algebra.
- `VERIFICATION.md`: independent proof and artifact audit.
- `main.tex`: packet source; all build outputs are under `tmp/`.
