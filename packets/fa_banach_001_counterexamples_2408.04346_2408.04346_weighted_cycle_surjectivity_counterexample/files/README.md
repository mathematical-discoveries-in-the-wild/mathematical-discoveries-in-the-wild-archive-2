# Weighted-cycle counterexample to the orthogonal surjectivity conjecture

The conjecture on source page 5 of arXiv:2408.04346 asserts that

    Theta_ij^2 = (O_ij^2 + O_ji^2)/2

maps SO(n) onto all symmetric nonnegative matrices Theta whose Hadamard
square is doubly stochastic.

The packet disproves this in dimension 6. Let P be supported on a 6-cycle
with successive edge weights alternating 1/3 and 2/3, and set
Theta=P^(circ 1/2). Then P is symmetric doubly stochastic. Its zeros would
force any preimage O to be supported on the same cycle. Orthogonality of
rows at distance two forces each column of O to have one entry of modulus
one, so O is a signed permutation. Its symmetrized square can have only
entries 0, 1/2, and 1, contradicting the chosen weights.

The proof upgrades to a one-parameter family on every even cycle of length
at least 6 and, by block embedding, disproves surjectivity in every
dimension n >= 6.

Files:

- solution_packet.pdf: final proof packet;
- main.tex: packet source;
- source_paper.pdf: official arXiv PDF;
- figures/source_candidate-05.png: complete source page containing the
  conjecture;
- code/verify_weighted_cycle.py: exact rational and finite-enumeration check;
- verification.md: proof, novelty, build, and render audit.

Status: candidate counterexample, likely valid. Novelty confidence is
moderate after a bounded primary-source search found no explicit resolution.

