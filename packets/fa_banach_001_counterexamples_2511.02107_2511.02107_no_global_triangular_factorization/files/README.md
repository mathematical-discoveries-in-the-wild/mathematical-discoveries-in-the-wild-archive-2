# No global triangular factorization in `GL^p(H)`

Status: `candidate counterexample likely valid`.

This packet answers Remark 7.4 of Goliński and Tumpach,
*Banach Poisson--Lie groups, Lax equations and the AKS theorem in infinite
dimensions* (arXiv:2511.02107).  For every `1 < p < infinity`, the global
factorization map from the unit upper-triangular and invertible
lower-triangular Schatten groups is not surjective.

The counterexample is the finite-rank perturbation of identity that rotates
the first two basis vectors through `pi/2`.  The obstruction is visible on a
single vector and cannot be repaired using the infinite-dimensional tail.
An explicit factorization for all nearby rotations with `cos(theta) != 0`
shows its factors blowing up at the exceptional angle, sharply illustrating
the gap between local and global factorization.

Files:

- `main.tex` and `solution_packet.pdf`: full proof packet.
- `source_paper.pdf` and `source_paper.tex`: official arXiv source copies.
- `figures/source_page_32.png`: Proposition 7.3 and open Remark 7.4.
- `code/verify_rotation_factorization.py`: exact symbolic block checks.
- `verification.md`: audit, scope, and novelty-search record.

