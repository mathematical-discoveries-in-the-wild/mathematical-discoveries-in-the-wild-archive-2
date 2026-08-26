# A strong Riccati solution whose graph is not reducing

Status: `candidate_counterexample_likely_valid`

Source: Konstantin A. Makarov, Stephan Schmitz, and Albrecht Seelmann,
*Reducing graph subspaces and strong solutions to operator Riccati equations*,
arXiv:1307.6439 (2013), unpublished preprint.

Target: the open problem in the introduction, page 3 of the source PDF.  The
authors ask whether the requirements

1. `G(H0,X)` is reducing for `A+V`, and
2. the associated skew operator `Y` is a strong Riccati solution

are equivalent or logically independent; in particular, they report no
example in which only one holds.

## Result

The packet constructs an explicit example satisfying (2) but not (1).
Let `K=l2(N0)`, let `S` be the unilateral shift, and put

```text
A e_n = 200^n e_n,
X = (3/100) I + (1/100)(S+S*).
```

Then `X` is bounded, positive, and maps `D=Dom(A)` into itself.  Nevertheless,
`(I+X^2)^(-1)` does not map `D` into itself.  The obstruction is explicit:
on the graph-norm realization of `D`,

```text
A X A^(-1) = (3/100)I + 2S + (1/20000)S*,
```

and `i` lies in its spectrum.

Define `C=AX-XA` on `D` and

```text
W = sum_{n>=0} (-1)^n X^n C X^n.
```

The series converges from `D` with its graph norm into `K`, because its ratio
is at most `40601/400000<1`.  It gives a densely defined skew-symmetric
operator satisfying `W+XWX=C`.  With equal diagonal entries `A0=A1=A` and
off-diagonal entries `W,W*`, the associated `Y` is therefore a strong solution
of the Riccati equation.  But the graph-domain splitting would force
`(I+X^2)^(-1)D` to be contained in `D`, which is false.

Thus strong solvability does not imply that the graph is reducing.  This is a
complete counterexample to one implication and disproves equivalence in full
generality.  It does not settle the converse implication; if “logical
independence” is interpreted as failure of both implications, that remaining
direction stays open.

## Files

- `solution_packet.pdf`: review-ready statement and proof.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original paper.
- `figures/open_problem_crop.png`: source-PDF page-3 crop.
- `code/check_parameters.py`: deterministic checks of the contraction,
  convergence, Rouché, and characteristic-root inequalities.
- `VERIFICATION.md`: verification commands and review focus.

## Novelty and review

The run's cheap indexes had no hit for the paper or problem.  Bounded searches
on 2026-08-09 used the exact open-problem sentence, exact title, authors, and
“strong solution / reducing graph / counterexample.”  They found the source
paper and the authors' later arXiv:1509.07984, which still states the
corresponding domain-splitting/domain-invariance question as open, but no later
resolution or this construction.  Novelty remains subject to expert review.

Human review should focus on the graph-domain spectral argument, the
graph-norm convergence of the series defining `W`, and the two block signs in
the Riccati identity.
