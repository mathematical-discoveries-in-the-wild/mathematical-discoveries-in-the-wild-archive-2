# Literature-implied affirmative answer: exact simultaneous bisection

status: `literature_implied_answer (full affirmative answer to Remark 3.4)`

source: Rainis Haller, Paavo Kuuseok, and Mart Poldvere, *On convex
combinations of slices of the unit ball in Banach spaces*, arXiv:1703.02919v2.

supporting theorem: Lyapunov's convexity theorem, as stated explicitly in
Peng Dai and Eugene A. Feinberg, *Extension of Lyapunov's Convexity Theorem to
Subranges*, arXiv:1102.2534, PDF page 1.

packet: `runs/fa_banach_001/solutions/literature_implied_answers/1703.02919_exact_simultaneous_bisection_lyapunov/`

ledger: `runs/fa_banach_001/ledger/results/1703.02919_exact_simultaneous_bisection_lyapunov.json`

## Identification

Remark 3.4 on PDF page 12 of arXiv:1703.02919 asks whether atomless finite
nonnegative measures `mu_1,...,mu_n` can bisect a measurable set `E` exactly
and simultaneously when `n >= 2`.

Apply Lyapunov's convexity theorem to the finite-dimensional vector measure

```text
nu(C) = (mu_1(C),...,mu_n(C)),  C subset E.
```

Its range is convex because all coordinate measures are atomless. Since the
range contains both `0` and `nu(E)`, it contains their midpoint. Thus there is
a measurable `A subset E` with `nu(A)=nu(E)/2`. For `B=E\A`, every coordinate
satisfies `mu_i(A)=mu_i(B)`.

This gives a full affirmative answer, but it is not a new theorem: it is a
direct specialization of the classical Lyapunov theorem, already restated in
arXiv:1102.2534 six years before the source question.

## Search and scope

The cheap run indexes had no packet or attempt for arXiv:1703.02919 or this
exact-bisection question. Bounded exact-phrase, title-plus-Lyapunov, and
lemma-plus-author searches found the source paper and general literature on
Lyapunov convexity, but no paper explicitly identifying Remark 3.4 as an open
question or announcing its resolution. The conservative provenance label is
therefore `literature_implied_answer`.

The conclusion concerns only the measure-theoretic question in Remark 3.4; it
does not add a new Banach-space theorem beyond what follows from the source
paper once its approximate lemma is strengthened.

## Files

- `main.tex`: compact status note with the exact implication.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1703.02919v2.
- `supporting_paper_1102.2534.pdf`: Dai--Feinberg's explicit statement of
  Lyapunov's theorem.
- `VERIFICATION.md`: audit notes for the source location, theorem hypothesis,
  and PDF rendering.
