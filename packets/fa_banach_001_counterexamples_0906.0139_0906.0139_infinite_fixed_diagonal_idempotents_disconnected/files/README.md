# A nonzero fixed diagonal has disconnected infinite-dimensional idempotent fiber

Status: **candidate counterexample, likely valid; human review pending**.

Source: Julien Giol, Leonid V. Kovalev, David Larson, Nga Nguyen, and
James E. Tener, *Projections and idempotents with fixed diagonal and the
homotopy problem for unit tight frames*, arXiv:0906.0139, Operators and
Matrices 5 (2011), 139--155.

The source asks whether its finite-dimensional path-connectedness theorem for
idempotents with arbitrary fixed diagonal has a full norm-topology analogue on
a separable infinite-dimensional Hilbert space.  The answer is no over both
real and complex scalars.  There is an orthonormal basis and a fixed nonzero
diagonal

```text
(1, 0, 0, ...)
```

whose fiber contains a rank-one idempotent and an infinite-rank idempotent.
Rank is invariant along norm-continuous idempotent paths, so the fiber has at
least two path components.

The infinite-rank witness is completely explicit.  Start with the block
idempotent `R u_i=-u_i-2v_i`, `R v_i=u_i+2v_i`, and regroup two `u`-vectors
with one `v`-vector using a fixed-point-free countable pairing.  A fixed real
orthogonal 3-by-3 change of basis makes every diagonal entry zero.  Adding a
one-dimensional identity summand gives the claimed nonzero diagonal.

The packet is intentionally scoped.  It does not settle the source's separate
infinite-dimensional question for projections with constant diagonal 1/2.
The finite FUNTF conjectures were explicitly settled by arXiv:1311.4748, and
the arbitrary complex finite projection fiber follows from arXiv:1804.05899.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `source_paper.pdf`: original paper.
- `figures/open_problem_crop_part1.png` and `part2.png`: the two-page source
  context containing Theorem 1.2 and the infinite-dimensional question.
- `code/verify_construction.py`: sanity checker for the block algebra, change
  of basis, pairing, and 6,000 initial diagonal values.
- `../../../../attempts/0906.0139_fixed_diagonal_upgrade_attempts.md`: eight
  focused upgrade attempts, including the unresolved projection route.

Verification command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/0906.0139_infinite_fixed_diagonal_idempotents_disconnected/code/verify_construction.py
```

Human review should focus on the countable regrouping/basis completeness and
on whether the source intended to exclude rank-degenerate infinite fibers.
Under the literal analogue of Theorem 1.2 as stated, the counterexample is
decisive.
