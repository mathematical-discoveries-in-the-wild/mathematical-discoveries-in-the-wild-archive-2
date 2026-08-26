# arXiv:1504.02445 — Devaney chaos implies dense distributional chaos

Status: `candidate_full_solution`, pending expert review.

Source: D. Bongiorno, U. B. Darji, and L. Di Piazza,
*Rolewicz-type chaotic operators*, arXiv:1504.02445, conjecture on printed
page 4.

## Result

Let `1 <= p < infinity`, let `f_1,...,f_t:N->N` be strictly increasing and
pairwise almost disjoint in the source paper's sense, and let
`T=sum_i c_i T_{f_i}` on `ell_p`.  If `T` is hypercyclic, then a power `T^N`
has a bounded right inverse of norm less than one.  Consequently `T` has the
positive (hence finite) shadowing property.  If `T` is Devaney chaotic, the
Bernardes--Peris theorem then makes `T` densely distributionally chaotic.
This proves the source conjecture and strengthens “distributionally chaotic”
to “densely distributionally chaotic.”

The mechanism is quantitative.  On the collision-free tail, the branching
row norm is `C=||(c_i)||_{p'}`.  Hypercyclicity forces `C>1`.  Each of the
finitely many exceptional initial rows has a nonzero finite escape coefficient
into that tail, after which dual-norm minimization yields right inverses
`R_N` with `||R_N|| <= K C^{-N}`.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained packet source.
- `source_paper.pdf`: official arXiv PDF of the question source.
- `supporting_paper_2305.02714.pdf`: Bernardes--Peris theorem used in the last step.
- `figures/open_problem_crop.png`: full-width source screenshot of the conjecture.
- `verification.md`: proof and novelty audit.
- `code/verify_right_inverse.py`: exact rational check of the finite-tree normalization.

Associated attempt:
`attempts/1504.02445_contracting_power_right_inverse_shadowing_full.md`.
