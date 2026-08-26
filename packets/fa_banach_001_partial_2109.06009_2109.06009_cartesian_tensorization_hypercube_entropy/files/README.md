# Cartesian tensorization of the graph entropy constant

Status: candidate partial result, likely valid.

Source target: Alexandre Bristiel and Pietro Caputo, Entropy inequalities for random walks and permutations, arXiv:2109.06009.

## Result

For finite weighted graphs with uniform vertex measures and the standard
Cartesian-product conductances,

    kappa(G square H) = min{kappa(G), kappa(H)}.

The proof combines the exact coordinate decomposition of the entropy energy
with tensorization of entropy.  Test functions depending on one coordinate
give the reverse inequality.  Since the spectral gap obeys the same product
formula, the property kappa=lambda is closed under finite Cartesian products.

In particular, for the anisotropically weighted Boolean cube

    Q_d(w_1,...,w_d) = product_i K_2(w_i),

one obtains the exact formula

    kappa(Q_d) = lambda(Q_d) = 2 min_i w_i.

This proves the rectangular-box conjecture in the source for all Boolean
boxes and proves its cycle conjecture for C_4.

## Scope

This is a substantial partial result, not a full solution of the source
question.  It does not prove equality for paths with more than two vertices,
cycles other than C_4, or rectangular lattice boxes with a side length
greater than two.

## Files

- main.tex: self-contained proof packet.
- solution_packet.pdf: rendered proof packet.
- source_paper.pdf: source arXiv PDF.
- figures/open_problem_crop_page8.png and page9.png: the source question.
- code/verify_tensorization.py: deterministic finite-instance checks.
- VERIFICATION.md: proof and computational audit notes.

## Reviewer focus

The central checks are the normalization in the exact energy decomposition,
the entropy chain-rule/convexity proof of tensorization, and the factor of two
in the weighted two-point graph.

