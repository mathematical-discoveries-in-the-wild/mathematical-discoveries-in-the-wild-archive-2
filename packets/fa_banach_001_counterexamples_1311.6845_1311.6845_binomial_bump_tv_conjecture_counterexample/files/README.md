# Alternating-binomial bump counterexample

Status: **candidate counterexample, likely valid; expert review requested**.

This packet gives a full negative answer to the exponential total-variation
conjecture in Alaifari--Pierce--Steinerberger, *Lower bounds for the truncated
Hilbert transform* (arXiv:1311.6845), equations (2.1) and the conjecture after
Theorem 2.1.  The decisive source statement is on printed page 7, Section 2.2.

For every interval pair in Case 3 or Case 4, it constructs real functions
`f_m` in `C_c^infty(I)` such that

```text
||f_m'||_1 / ||f_m||_2 = O(m^(3/4)),
||H f_m||_{L2(J)} / ||f_m||_{L2(I)} = O(q^m),  0 < q < 1.
```

Consequently, if `S(K)` denotes the best normalized lower stability envelope
among functions with total-variation ratio at most `K`, then

```text
S(K) <= C exp(-c K^(4/3))
```

for all sufficiently large `K`.  This rules out every proposed lower bound
`c1 exp(-c2 K)`.  Together with Theorem 2.4 of the source paper, it places the
unknown sharp envelope between exponential powers `4/3` and `2`.

The construction is a fixed-width train of disjoint smooth bumps with
alternating binomial coefficients.  The coefficients give exact cancellation
of the first `m-1` terms of the smooth Hilbert kernel away from the observation
interval.  A repeated finite-difference identity supplies the rigorous bound.

Packet contents:

- `solution_packet.pdf`: complete theorem, proof, source evidence, and scope;
- `main.tex`: reproducible LaTeX source;
- `source_paper.pdf`: the source paper;
- `figures/open_problem_crop.png`: real crop of the conjecture on page 7;
- `code/verify_binomial_bumps.py`: exact algebraic sanity checks;
- `verifier_notes.md`: independent line-by-line proof audit;
- `novelty_search.md`: bounded literature-search record.

The computation is not used as a proof.  The principal human-review points
are the Case 4 localization, the finite-difference estimate, and the conversion
from `m` to the `K^(4/3)` envelope.
