# Inverse-free Gram block dilations for every C_A operator

This packet gives a candidate full answer to Question 5.9 of Bhat, Ghatak,
and Pamula, *Operator moment dilations as block operators*
(arXiv:2302.13873, page 28 of the compiled source PDF).

## Result

Every operator `T` in `C_A` has a canonical minimal isometric block dilation
obtained from the finite Toeplitz Gram matrices

```text
G_n = [zeta_A(j-i)]_(i,j=0)^n.
```

The quotient-completions of these Gram spaces form an inductive system.
Coordinate shift gives the isometry, and successive orthogonal differences of
the nested stages give an upper-Hessenberg block decomposition. Column `j` is
computed entirely inside `G_(j+1)`. No inverse, pseudoinverse, closed-range
assumption, or nonsingularity assumption is used.

The wandering defect `K_+ minus V K_+` then supplies a negative identity-shift
tail. Together with one coupling column and the positive Hessenberg corner,
this gives an explicit minimal unitary block dilation.

## Files

- `main.tex`: exact question, theorem, proof, scope, and novelty audit.
- `solution_packet.pdf`: compiled human-review packet.
- `source_paper.pdf`: locally compiled arXiv source paper.
- `figures/open_problem_crop.png`: Question 5.9 from source page 28.
- `verification.md`: independent proof and render checks.
- `tmp/`: LaTeX intermediates and rendered audit pages.

Status: candidate full answer, likely valid. The construction is classical in
spirit, so mathematical novelty confidence is moderate; independent expert
review should focus on whether canonical Gram coordinates meet the intended
notion of an explicit block decomposition.
