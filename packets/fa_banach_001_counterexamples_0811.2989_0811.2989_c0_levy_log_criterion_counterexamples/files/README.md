# Counterexample packet: no general C0 logarithmic-moment criterion

Status: `candidate_counterexample_likely_valid`

Source: Zbigniew J. Jurek, *On Relations Between Urbanik and Mehler
Semigroups*, arXiv:0811.2989, open problem on printed page 12.

## Result

The logarithmic condition on `Y(1)` is neither necessary nor sufficient for
convergence of `integral T_s dY(s)` under general strongly stable
`C0`-semigroups.

- Necessity fails on `L2(0,1)` for the nilpotent left-shift semigroup and a
  compound-Poisson driver with infinite logarithmic moment. The integral is
  constant after time one.
- Sufficiency fails on `ell2` for the bounded diagonal generator
  `A e_n = -e_n/n` and deterministic Lévy drift `Y(t)=t(1/n)_n`. The source
  defines operator topology as the strong topology, so this also corrects its
  preceding bounded-generator formulation. The later literature states that
  classical iff with operator-norm stability.

The packet also proves:

- the exact deterministic criterion `y in Range(-A)`;
- an exact reduction at integer times to the iid operator series
  `sum T_n xi_(n+1)`, including the one-block characteristic exponent;
- a sharp logarithmic iff for the block law under two-sided exponential
  operator bounds;
- the exact Hilbert-space Gaussian Hilbert--Schmidt energy criterion and a
  Gaussian all-moments divergence example.

This is a full negative answer to a universal log-moment extension, not a
claimed classification of every Banach-space Lévy triplet.

## Files

- `main.tex`: self-contained statements, proofs, literature boundary, and
  limitations.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: official arXiv source paper PDF.
- `figures/open_problem_crop.png`: readable crop of the source question.
- `verification.md`: proof and render audit.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Review focus

The two counterexamples and the deterministic range theorem are elementary.
Human review should additionally check the source's strong-topology
convention, the standard Lévy-measure argument relating the one-block and
`Y(1)` logarithmic moments, and the explicit uniform-tightness hypothesis in
the real-time form of the block criterion.

Novelty is plausible, not certified. The run indexes and a bounded arXiv/web
search through 2026-08-17 found the known Hilbert triplet theorem and the
operator-norm classical result, but no later paper explicitly answering the
stated general Banach-space question.

Ledger:
`runs/fa_banach_001/ledger/results/0811.2989_c0_levy_log_criterion_counterexamples.json`
