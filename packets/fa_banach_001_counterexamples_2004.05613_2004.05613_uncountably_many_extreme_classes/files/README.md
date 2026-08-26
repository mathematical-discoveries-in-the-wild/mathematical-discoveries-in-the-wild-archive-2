# Uncountably many extreme-point classes for D-majorization

Status: `candidate_counterexample_likely_valid`

Source: Frederik vom Ende, *Strict Positivity and D-Majorization*,
arXiv:2004.05613; Linear and Multilinear Algebra 70:19 (2022), 4023–4048.

Source location: Section 5 (Conclusion and Outlook), pages 20–21 of the arXiv
PDF.

## Result

The source asks whether the extreme points of `M_D(A)` fall into finitely
many classes after quotienting by conjugation with unitaries commuting with
`D`.  The answer is **no in general**, already for qubits.

Take

```text
D = diag(1/3,2/3),   A = |e_1><e_1|.
```

For every qubit state `rho`, the state

```text
tau = (D-(1/3)rho)/(2/3)
```

is positive, and the measure-and-prepare channel

```text
T_rho(X) = <e_1,Xe_1>rho + <e_2,Xe_2>tau
```

fixes `D` and sends `A` to `rho`.  Consequently `M_D(A)` is the entire
qubit state space.  Its extreme points are all pure states.  The commutant of
`D` consists of diagonal unitaries, so the pure-state invariant
`|<e_1,psi>|^2` parametrizes uncountably many inequivalent extreme points.

The packet proves the stronger statement that for every nonscalar full-rank
density matrix `D`, choosing `A` pure in a minimum-eigenvalue eigenspace makes
`M_D(A)` the full state space; the quotient of its extreme points is exactly
the simplex of spectral weight vectors of `D`.

## Scope and novelty

This fully refutes general finiteness as the concluding question is written.
It does not classify which restricted or nonmaximal pairs `(D,A)` may still
have finitely many classes.

The local indexes and a bounded web/arXiv search were checked using the exact
question, arXiv id, `D-majorization`, `M_D(A)`, commutant, and extreme-point
terms.  No stated resolution was found.  The author's 2020 dissertation
repeats the question.  Novelty confidence is moderate: the counterexample is
a short, apparently unnoticed consequence of the maximal-state mechanism in
the source itself.

## Packet contents

- `main.tex`: self-contained theorem, proof, scope, and novelty audit.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv v4 PDF.
- `figures/open_problem_crop_page20.png` and
  `figures/open_problem_crop_page21.png`: readable source crops.
- `verification.md`: adversarial mathematical and render checks.

Human review recommendation: **review as a full negative answer**.  The
primary semantic check is whether the informal question intended to exclude
maximal initial states; no such exclusion appears in the source.

