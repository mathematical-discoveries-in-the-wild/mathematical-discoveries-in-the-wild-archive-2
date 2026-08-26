# Literature answer: the polarity principle fails

Status: `literature_already_answered (negative)`

## Original question

Beznea, Cornea, and Röckner ask after Remark 4.15 in Section 4.8,
page 19 of arXiv:1007.2379v2, whether the axiom of polarity holds for
infinite-dimensional Brownian motion. Equivalently, must every semipolar
Borel set be polar?

## Decisive later answer

Patrick J. Fitzsimmons, *Gross' Brownian Motion Fails to Satisfy the Polarity
Principle*, Rev. Roumaine Math. Pures Appl. 59 (2014), no. 1, 87-91,
explicitly cites the Beznea-Cornea-Röckner paper and states in Theorem 1 that
Gross' Brownian motion does not satisfy the axiom of polarity.

Fitzsimmons defines a Borel unit quadratic-variation shell. It is hit from the
origin at time one, so it is not polar. Quadratic variation then evolves as an
internal clock, `Q(X_t)=Q(X_0)+t`, and the shell is visited at most once; this
makes it semipolar. The formal theorem is written for the classical Wiener
space, which already gives a negative answer to the general validity question.
The supporting paper also states that the construction extends to a general
abstract Wiener space, although it does not write out that extension.

## Files

- `source_paper.pdf`: arXiv:1007.2379v2.
- `supporting_paper_fitzsimmons_2014.pdf`: the decisive 2014 paper.
- `solution_packet.pdf`: compact status and identification note.
- Ledger: `runs/fa_banach_001/ledger/results/1007.2379_polarity_principle_fitzsimmons_2014.json`.

