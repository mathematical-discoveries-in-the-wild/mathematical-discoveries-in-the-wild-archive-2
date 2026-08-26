# Hartman/WAP Strictness: Full LCA Classification

Status: `counterexample_likely_valid`.

Source: Gabriel Maresch and Reinhard Winkler, "Compactifications, Hartman functions and (weak) almost periodicity," arXiv:math/0510064; *Dissertationes Mathematicae* 461 (2009), 1--72.

Problem 5.4.7 asks for which topological groups

`H_c(G) superset H(G) intersection W(G)`

is strict and requests a function in the difference.

## Claimed result

For locally compact abelian groups, the inclusion is strict exactly when `G` is infinite. More generally, strictness holds for every infinite maximally almost periodic abelian topological group.

The proof recursively constructs two sequences `x_n,y_n` and a countable family of continuous characters such that:

- the images of `x_n` and `y_n` converge to the identity in the resulting metrizable compactification;
- all selected sums `x_n+y_m` have distinct images.

For

`S={iota(x_n+y_m):n<=m}`

the closure of `S` is countable. Thus `F=1_S` is Riemann integrable and supported on a meager Haar-null set. Consequently `f=F o iota` belongs to `H_0(G) subset H_c(G)`. But

`f(x_n+y_m)=1` exactly when `n<=m`,

so its two iterated limits are 1 and 0. Grothendieck's double-limit criterion gives `f notin W(G)`.

Every LCA group is maximally almost periodic by Pontryagin duality. For finite groups every bounded function is almost periodic, giving the converse.

## Novelty search

The local run indexes contained no result for arXiv:math/0510064 or this problem. Exact-phrase, title/citation, and topic searches combining `H_c(G)`, `H_0(G)`, Hartman measurability, and weak almost periodicity found the source and related surveys, but no later answer to Problem 5.4.7 or the LCA classification above. This is a bounded novelty check, not a claim of exhaustive bibliographic priority.

## Verification

`VERIFICATION.md` gives an adversarial step check with verdict `valid` and confidence 97/100. The reusable script `code/verify_z_instance.py` constructs an explicit irrational-rotation instance from Pell denominators and checks 120 distinct two-term sums plus an `8 x 8` upper-triangular translate matrix.

Command:

`conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/counterexamples/0510064_hc_strict_exactly_infinite_lca_groups/code/verify_z_instance.py`

Result: `PASS`.

## Files

- `source_paper.pdf`: source paper
- `figures/open_problem_crop.png`: Problem 5.4.7 on source PDF page 54
- `main.tex`: full proof packet
- `solution_packet.pdf`: rendered review packet
- `VERIFICATION.md`: adversarial verification report
- `code/verify_z_instance.py`: finite smoke check

Attempt record: `runs/fa_banach_001/attempts/0510064_hc_not_wap_on_z_upper_triangular_hartman_set_lane08.md`.

Ledger: `runs/fa_banach_001/ledger/results/0510064_hc_strict_exactly_infinite_lca_groups.json`.
