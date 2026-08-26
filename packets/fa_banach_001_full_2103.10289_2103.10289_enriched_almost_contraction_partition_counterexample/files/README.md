# Enriched almost contraction partition counterexample

Status: candidate full negative answer; human review requested.

For the step map `S(x)=-1` on the negative half-line and `S(x)=1` on the
nonnegative half-line, `S` is a `(1/2,2)`-almost contraction. The de-averaged
map

    T = 3S - 2I

is therefore an enriched `(2,3/2,2)`-almost contraction on `R`.

Any meaningful partition in the source problem must be `T`-invariant. The
orbit segment `8/5 -> -1/5 -> -13/5` forces the first two points into one
cell, where the positive secant slope is `4/3`. This violates both
nonexpansiveness and the defining strict inequality for every possible
enriched-contraction parameter pair.

Files:

- `main.tex`, `solution_packet.pdf`: complete construction and proof.
- `source_target_2103.10289.pdf`: target paper.
- `VERIFICATION.md`: source, algebra, and artifact checks.
