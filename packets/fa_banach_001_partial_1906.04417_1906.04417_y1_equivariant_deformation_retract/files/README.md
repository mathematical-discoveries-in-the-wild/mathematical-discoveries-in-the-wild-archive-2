# The first Lazarev--Lieb phase sublevel retracts to the circle

Status: `partial result likely valid`.

Frick and Superdock ask for the homotopy type of the spaces

`Y_n = {h in C^infty([0,1],S^1): ||h||_{W^{1,1}} <= 1+pi*n}`

with the topology induced by the `L^1` norm. This packet completely determines
the first nontrivial space. The normalized mean of every `h in Y_1` is nonzero
and never antipodal to a value of `h`. Taking the principal phase relative to
that mean and scaling it to zero gives an explicit `Z/2`-equivariant strong
deformation retraction of `Y_1` onto the constant functions. Consequently,
`Y_1` is equivariantly homotopy equivalent to `S^1` and has coindex one.

The same proof works for every real variation threshold `0 <= L <= pi`.
The all-`n` problem remains open in this packet; the accompanying attempt note
records four deeper upgrade routes and the phase-slip obstruction that appears
at `L=2*pi`.

Files:

- `main.tex` and `solution_packet.pdf`: theorem and complete proof.
- `source_paper.pdf` and `source_paper.tex`: source paper.
- `figures/source_problem_page14.png`: source Theorem 6.2 and Problem 6.3.
- `code/check_mean_contraction.py`: numerical stress test on smooth phase
  families.
- `verification.md`: proof audit, novelty search, and packet QA.
