# Hilbert--Schmidt operators with increasing standard-compression spectrum

Status: `candidate_partial_likely_valid`

Source: Roman Drnovšek, *Triangularizability of trace-class operators with
increasing spectrum*, arXiv:1508.07766, Question 3 (PDF page 3).

## Result

This packet proves an affirmative answer to the source question for every
Hilbert--Schmidt operator on `L^2[0,1]`:

> If `K` is Hilbert--Schmidt and has increasing spectrum relative to standard
> compressions, then `K` is quasinilpotent and admits a standard
> triangularization.

Writing `k` for the measurable `L^2` kernel of `K`, the positive
Hilbert--Schmidt operator with kernel `|k|` is also quasinilpotent.  Its
de Pagter triangularizing chain is invariant for `K` by pointwise domination.

The source's interval theorem required `K` to be trace class, `k` to be
continuous, and the lattice modulus to be trace class.  All three conditions
are removed here.  The key replacement is a Boolean inclusion--exclusion
identity for the traces of powers of localized Hilbert--Schmidt operators;
it isolates genuine cycles without evaluating a measurable kernel on the
diagonal.

## Scope and obstruction

This is a substantial partial answer, not a solution of Question 3 for all
compact operators.  A compact operator may belong to no finite Schatten
class and need not have an `L^2` kernel.  In that regime no power-trace or
positive-kernel argument is available, and invariant standard subspaces are
not stable under arbitrary finite-rank approximation.

Four focused upgrade attempts are recorded in
`attempts/1508.07766_hilbert_schmidt_interval_triangularization.md`: removing
the modulus trace-class assumption, removing trace class of `K`, removing
continuity, and finally testing the route against arbitrary compact
operators.  The first three succeeded; the fourth met the structural
obstruction above.

## Evidence and verification

- `source_paper.pdf`: arXiv:1508.07766.
- `figures/open_problem_crop.png`: full-width rendering of source PDF page 3,
  including Question 3.
- `main.tex`, `solution_packet.pdf`: formal proof packet.
- `code/check_cycle_combinatorics.py`: finite verification of the Boolean
  coefficient and shortest-cycle combinatorics through length 8.

Bounded searches on 2026-08-11 used the exact source title, the phrases
`increasing spectrum relative to standard compressions`, `Hilbert-Schmidt`,
and `standard triangularization`, plus the run's cheap indexes.  They found
the 2009 and 2017 source papers but no later result with this scope.  Novelty
confidence is moderate pending expert review.

