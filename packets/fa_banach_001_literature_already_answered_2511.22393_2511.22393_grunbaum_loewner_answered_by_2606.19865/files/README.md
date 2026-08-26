# Literature answer: the Grünbaum–Löwner centroid-section problem

status: `literature_already_answered`

source: J. Haddad, C. Jiménez, and R. Villa, *Centroids of sections of
convex bodies and Lusternik–Schnirelmann category*, arXiv:2511.22393.

supporting answer: X. Ge and K.-W. Yang, *A complete solution to questions
of Grünbaum and Loewner*, arXiv:2606.19865.

packet: `runs/fa_banach_001/solutions/literature_already_answered/2511.22393_grunbaum_loewner_answered_by_2606.19865/`

ledger: `runs/fa_banach_001/ledger/results/2511.22393_grunbaum_loewner_answered_by_2606.19865.json`

## Identification

The source asks whether the centroid of every convex body in `R^n` is the
centroid of at least `n+1` distinct central hyperplane sections, and asks for
the exact minimum `mu(n)` of the number of such sections. It records the
known values `mu(2)=3` and `mu(n)=1` for `n>=5`, leaving `n=3,4` open.

Ge–Yang explicitly cite arXiv:2511.22393, restate both exact questions as
Problems 1 and 2, and prove in Theorem 1.1 that `mu(n)=1` for every `n>=3`.
Together with the planar result, the complete answer is

```text
mu(2) = 3,
mu(n) = 1 for every n >= 3.
```

Thus Grünbaum's proposed `n+1` conclusion is true for `n=2` and false in
every dimension `n>=3`.

## Scope

The packet resolves the formally stated Grünbaum and Löwner questions. It
does not claim an answer to the source's separate arbitrary-point question
in dimensions `n>=4` or its separately stated Barker–Larman problem.

## Files

- `solution_packet.pdf`: compact literature-resolution note.
- `source_paper.pdf`: arXiv:2511.22393.
- `supporting_paper_2606.19865.pdf`: exact later answer.

