# Random-semigroup weak law on every separable Banach space

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- S. Dzhenzher and V. Sakbaev, “Quantum law of large numbers for Banach
  spaces,” arXiv:2410.07417 (2024).
- Open problem: Conjecture 2.5, PDF page 4.
- Local source: `source_paper.pdf`.
- Source evidence: `figures/open_problem_crop.png`.

## Claimed contribution

Under the standard random-element meaning of i.i.d., the packet proves a
strict strengthening of Conjecture 2.5. For every separable Banach space `X`,
every SOT-measurable i.i.d. sequence with `||A_i|| <= rho`, every `x in X`,
and every `T > 0`,

```text
E sup_{0 <= t <= T}
  ||exp(t A_1/n)...exp(t A_n/n)x - exp(t E[A])x||  -> 0.
```

Thus the convergence is uniform in time in `L1`, hence in probability. The
proof replaces exponentials by Euler factors with deterministic `O(1/n)`
error, expands the Euler product into ordered nonsymmetric Banach-valued
U-statistics, proves their fixed-order `L1` law by an overlap-variance and
simple-kernel argument, and sums the limits using factorial bounds.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: source theorem and conjecture.
- `code/verify_euler_ustat.py`: noncommutative finite-matrix sanity check;
  not part of the proof.
- `verification.md`: commands, output, and review priorities.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Terminology caveat

The proof uses ordinary independence of the SOT-valued operator random
elements. The source describes “i.i.d. generators” but also gives a bespoke
definition involving one rank-one scalar observation from each operator.
Taken literally, that observation class does not visibly generate all finite
joint SOT cylinders. The standard interpretation resolves the intended
conjecture; a reviewer should decide whether the source sentence was intended
as shorthand or needs a hypothesis correction.

## Literature and novelty check

A bounded index, local-corpus, and web search on 17 August 2026 found the
authors’ later arXiv:2507.07658. It proves an almost-sure SOT theorem for
uniformly smooth spaces, an all-Banach WOT theorem, and states an ell_1
consequence, but assumes Bochner measurability in the operator norm. That does
not cover the source’s weak/SOT-measurable hypothesis. No all-separable
uniform-L1 theorem or this ordered-U-statistic proof was located. Novelty
confidence is moderate pending specialist review.

## Human review focus

Please check:

- the nonsymmetric ordered U-statistic lemma and its `L1` approximation step;
- SOT measurability/continuity of ordered composition on a fixed norm ball;
- the precise independence convention intended by the source paper.
