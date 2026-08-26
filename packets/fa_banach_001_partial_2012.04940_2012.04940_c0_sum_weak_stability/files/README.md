# Arbitrary c0-sums preserve weak stability exactly

This packet gives a substantial positive subcase of the `C_0(K,X)` converse
question in arXiv:2012.04940.

For any nonempty index set `Gamma` and arbitrary Banach spaces `X_gamma`,

`(oplus X_gamma)_{c0}` has a weakly stable unit ball

if and only if every `X_gamma` has a weakly stable unit ball.  Thus the open
converse holds for every discrete locally compact `K`, with no norm-stability,
finite-dimensionality, separability, or identical-fiber assumption.  It also
gives the injective-tensor consequence

`c_0(Gamma) tensor_epsilon X = c_0(Gamma,X)`

for every weakly stable `X`.

The proof uses finite-support approximation in the `ell_1`-sum dual.  Only
finitely many coordinates matter to a shrunken weak neighborhood; weak
stability splits those coordinates, while all untouched coordinates are copied
from the target vector into every component.

## Files

- `main.tex` / `solution_packet.pdf`: theorem, proof, comparison, and scope.
- `verification.md`: adversarial proof audit.
- `source_paper.pdf`: arXiv:2012.04940.
- `supporting_paper_1806.10693.pdf`: earlier finite-dimensional `(co)` theorem.
- `figures/open_problem_crop.png`: the exact converse question.

## Status

`partial_result_likely_valid`; human Banach-geometry review recommended.  The
general case of non-discrete scattered `K` remains open.

