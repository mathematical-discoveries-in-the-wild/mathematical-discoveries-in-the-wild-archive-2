# The bidual Ruelle eigenspace can be infinite-dimensional with a unique eigenmeasure

Status: `counterexample` (candidate full negative answer, pending human review)

## Source question

L. Cioletti, A. van Enter, and R. Ruviaro, *The Double Transpose of the
Ruelle Operator*, arXiv:1710.03841v4; published in *Monatshefte für
Mathematik* 200 (2023), 523–544.

Section 1.1, arXiv PDF page 4, asks whether, for the barycenter `nu` of the
maximal-eigenmeasure set `G*(f)`,

```text
dim_R H = # ex(G*(f)),
H = {xi in L1(nu)** : L_f** xi = rho(L_f) xi}.
```

## Counterexample

Take the full one-sided two-symbol shift, the uniform a priori measure, and
the zero potential. The maximal eigenmeasure is uniquely the fair Bernoulli
product measure, so the right-hand side is `1`.

Nevertheless, `H` is infinite-dimensional. For every periodic point `y`,
normalize Bernoulli measure on the shrinking prefix cylinders about `y` and
take a weak-star cluster point in `L1(nu)** = L∞(nu)*`. This state restricts
to point evaluation at `y` on continuous functions. Cesàro-average its
translates under the double transpose. A second weak-star cluster point is a
positive fixed state whose restriction to `C(X)` is the uniform probability
measure on the periodic orbit of `y`. States arising from distinct periodic
orbits are linearly independent, because their restrictions are mutually
singular finite-orbit measures.

Thus

```text
# ex(G*(0)) = 1,  but  dim_R H = infinity.
```

The mechanism uses precisely the extra purely finitely additive states in
the bidual; it disappears if `H` is replaced by the eigenspace inside the
canonical copy of `L1(nu)`.

## Files

- `source_paper.pdf`: arXiv:1710.03841v4.
- `figures/dimension_question_crop.png`: the exact source passage on PDF page 4.
- `main.tex`, `solution_packet.pdf`: construction and proof.

Ledger:
`runs/fa_banach_001/ledger/results/1710.03841_bernoulli_bidual_eigenspace_infinite.json`.
