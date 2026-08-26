# Norm-one periodic decompositions for generic systems and noncommensurable triples

This packet gives a strong partial answer to the constant problem posed in
arXiv:1312.3798, *The periodic decomposition problem* by Bálint Farkas and
Szilárd Gy. Révész.

Let `P_alpha` be the bounded continuous `alpha`-periodic real functions on
the line.  The packet proves:

1. if `1/alpha_1,...,1/alpha_n` are linearly independent over the rationals,
   every `f` in `P_alpha_1+...+P_alpha_n` has a decomposition whose every
   summand has norm at most `||f||_infinity`;
2. for three periods, the same norm-one conclusion holds whenever the three
   periods are not all commensurable.

Both assertions are sharp.  The second includes the rational-rank-two case,
where the one-parameter orbit lies in a proper subtorus and the elementary
full-product extrema argument is unavailable.

The proof uses compact orbit closures, Haar conditional expectations, and a
pair-extrema constant-allocation argument.  It uses only the source's known
sharp two-period bound in the case of one commensurable pair.

The fully commensurable three-period case and dependent systems with four or
more commensurability classes remain open in this packet.  Exact and sampled
finite-dimensional searches found no counterexample; those computations are
recorded as evidence only.

Files:

- `main.tex` and `solution_packet.pdf`: theorem and proof;
- `source_excerpt.tex` and `source_excerpt.pdf`: exact transcribed source
  problem with cached-TeX line references;
- `code/`: finite cyclic, finite-torus, and continuous ridge searches;
- `verification.md`: proof, computation, literature, and visual audit.
