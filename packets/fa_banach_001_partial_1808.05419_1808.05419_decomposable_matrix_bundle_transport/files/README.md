# Countable matrix-bundle transport metric

Status: **candidate partial result; likely valid; send to human review**.

Source: Melchior Wirth, *A Noncommutative Transport Metric and Symmetric
Quantum Markov Semigroups as Gradient Flows of the Entropy*,
arXiv:1808.05419.  Example 4.19 on source PDF page 26 asks how to extend the
transport metric to infinite-dimensional quantum Markov semigroups satisfying
detailed balance for a nontracial state or weight.

## Result

The packet gives a rigorous extension for every countable direct product of
finite-dimensional detailed-balance systems.  On

`M = product_n M_{d_n}`

with a faithful normal nontracial reference state and the decomposable quantum
Markov semigroup, each invariant central-mass fibre of the normal state space
is equipped with the weighted `ell_2` product of the Carlen--Maas metrics.  The
distance is an extended nondegenerate metric, and the predual semigroup is the
gradient flow of global relative entropy.  The entropy splits into a weighted
sum of the block entropies plus a classical central term; the latter is
constant on each invariant fibre.

This is genuinely infinite dimensional whenever infinitely many blocks are
present, and the reference state is nontracial whenever one block density is
nonscalar.  It is partial: it requires the semigroup to preserve every central
block and does not address mixing semigroups, type II/III factors, or weights.

## Files

- `solution_packet.pdf`: theorem, proof, limitations, and review request.
- `source_paper.pdf`: original paper.
- `figures/open_problem_crop.png`: source PDF page 26.
- `verification_report.md`: proof audit.
- `novelty_search.md`: bounded literature/status search.
- `../../../../attempts/1808.05419_nontracial_transport_direct_product_attempt.md`:
  upgrade-attempt log and obstruction to the full problem.

No computation is used as proof.
